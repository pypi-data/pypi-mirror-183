import logging
from typing import TYPE_CHECKING
from uuid import uuid4

from blockly_executor import ExtException
from blockly_executor.core.exceptions import LimitCommand, StepForward, DeferredOperation, ReturnFromFunction, \
    WorkspaceNotFound

if TYPE_CHECKING:
    from .executor import BlocklyExecutor


class Block:
    ns = {'b': 'https://developers.google.com/blockly/xml'}

    def __init__(self, executor: 'BlocklyExecutor', **kwargs):
        self.executor: BlocklyExecutor = executor
        self.block_id = None
        self.logger = kwargs.get('logger', logging)

    @classmethod
    def init(cls, executor, name, node, **kwargs):
        self = cls(executor, **kwargs)
        self.name = name
        self.node = node
        return self

    def _check_step(self, context, block_context):
        if self.executor.debug:
            if self.executor.breakpoints and self.executor.breakpoints.get('workspace'):
                if self.block_id in self.executor.breakpoints['workspace']:
                    raise StepForward(self.block_id, context, block_context, self.executor.workspace_name)
            elif self.executor.is_next_step:
                raise StepForward(self.block_id, context, block_context, self.executor.workspace_name)
            elif self.executor.step_by_step and self.block_id == self.executor.current_block \
                    and self.executor.current_workspace == self.executor.workspace_name:
                if self.executor.is_next_step is False:  # встаем на этом шаге
                    raise StepForward(self.block_id, context, block_context, self.executor.workspace_name)
                else:
                    self.executor.is_next_step = True  # встаем на следующем шаге

    def _set_next_step(self):
        if self.executor.step_by_step:
            if self.block_id == self.executor.current_block and self.executor.current_workspace == self.executor.workspace_name:
                self.executor.is_next_step = True

    def _set_step(self):
        if self.executor.step_by_step:
            # if self.executor.current_block != self.block_id:
            self.executor.is_next_step = False
            self.executor.current_block = self.block_id

    async def _before_execute(self, node, path, context, block_context):
        self.block_id = node.get('id')
        self.block_type = node.get('type')
        block_context['__id'] = self.block_id
        block_context['__path'] = f'{path}.{self.block_type}'
        # context.init_block_context(block_context, self.block_id, path)
        pass

    @classmethod
    def get_child_block(cls, node):
        child = None
        if node:
            child = node.find('./b:block', cls.ns)
            if child is None:
                child = node.find('./b:shadow', cls.ns)
        return child

    async def execute_all_next(self, node, path, context, block_context, statement=False):
        statement_number = 0
        child_context = context.get_child_context(block_context)
        result = None
        while True:
            if statement:
                try:
                    _child_context = child_context[
                        str(statement_number)]  # приводим к строке ключ потому что в json сохраняем
                except KeyError:
                    child_context[str(statement_number)] = {}
                    _child_context = child_context[str(statement_number)]
            else:
                _child_context = child_context

            child = self.get_child_block(node)

            next_node = None

            if child is not None:
                next_node = self.get_next_statement(child) if statement else None
                block_subtype = child.get('type')
                if '__result' not in _child_context:

                    # path = f'{path}.{block_subtype}'
                    _class = self.executor.get_block_class(block_subtype)
                    try:
                        result = await _class(self.executor, logger=self.logger).execute(
                            child, block_context['__path'], context, _child_context)
                    except LimitCommand as err:
                        raise err from err
                    except StepForward as err:
                        raise err from err
                    except ReturnFromFunction as err:
                        raise err from err
                    except WorkspaceNotFound as err:
                        raise err from err
                    except DeferredOperation as err:
                        raise err from err
                    except ExtException as err:
                        raise ExtException(parent=err)
                    except Exception as err:
                        raise ExtException(message='Ошибка в блоке',
                                           detail=f'{err} ({block_subtype})',
                                           parent=err,
                                           skip_traceback=1)
                else:
                    self.logger.debug(f'{child.get("id")} skip')
            else:
                result = None
                # raise Exception(f'{self.__class__.__name__} не хватает блока. path: {path} ')

            if next_node:
                node = next_node
                # помечаем блок который выполнили
                _child_context['__result'] = True
                statement_number += 1
            else:
                context.clear_child_context(block_context)
                return result

    async def _execute(self, node, path, context, block_context):
        return await self.execute_all_next(node, path, context, block_context)
        pass

    async def execute(self, node, path, context, block_context):
        try:
            await self._before_execute(node, path, context, block_context)
            self.logger.debug(f'{self.full_name} begin execute id="{self.block_id}"')
            return await self._execute(node, path, context, block_context)
        except LimitCommand as err:
            raise err from err
        except StepForward as err:
            raise err from err
        except ReturnFromFunction as err:
            raise err from err
        except DeferredOperation as err:
            raise err from err

    @property
    def full_name(self):
        # return f'{self.block_id}'
        return f'{self.__class__.__name__}'

    def command_send(self, command_name, command_params, context, block_context):
        command_uuid = str(uuid4())
        block_context['__deferred'] = command_uuid
        context.operation['commands'].append(
            {
                'name': command_name,
                'params': command_params,
                'uuid': command_uuid
            }
        )
        raise DeferredOperation(command_uuid, context, block_context)

    @staticmethod
    def command_sended(block_context):
        return '__deferred' in block_context

    def command_get_result(self, command_uuid):
        try:
            result = self.executor.commands_result.pop(command_uuid)
        except KeyError:
            raise ExtException(
                message='Command no response',
                detail=f'block {self.full_name} command_uuid {command_uuid}'
            )
        try:
            _status = result['status']
            _data = result['data']
        except KeyError:
            raise ExtException(
                message='Bad format command result',
                detail=f'block {self.full_name} command_uuid {command_uuid}',
                dump={'result': result}
            )
        if _status.upper() == 'COMPLETE':
            return _data
        if _status.upper() == 'ERROR':
            if isinstance(_data, dict):
                raise ExtException(parent=_data)
            else:
                raise Exception(_data)
        raise ExtException(
            message='Not supported command result type',
            detail=f'block {self.full_name} result type {_status}',
        )

    @classmethod
    def get_next_statement(cls, node):
        return node.find(f"./b:next", cls.ns)

    @classmethod
    def _get_mutation(cls, node, mutation_name, default=None):
        mutation = node.find(f'./b:mutation', cls.ns)
        if mutation is not None:
            return mutation.get(mutation_name, default)
        return default

    # async def _calc_all_mutation(self, node, path, context, block_context, mutation_name):
    #     mutation_count = self._get_mutation(node, mutation_name)
    #     if mutation_count:
    #         for j in range(mutation_count):
    #             # рассчитываем все мутации
    #             _key = f'{mutation_name}{j}'
    #             complete = _key in block_context
    #             if not complete:
    #                 result = await self._calc_mutation(node, path, context, block_context, j)
    #                 block_context[_key] = result
    #
    # async def _calc_mutation(self, node, path, context, block_context, _key):
    #     raise NotImplemented()

    # @classmethod
    # def set_thread_variable(cls, context, name, value):
    #     context.debug['__thread_vars'][name] = value
    #     cls.set_variable(context, name, value)

    @classmethod
    def defined_variable(cls, context, name):
        try:
            return name in context.block_context['__thread_vars'] or name in context.variables
        except KeyError:
            return False

    @classmethod
    def get_variable(cls, context, name):
        try:
            return context.block_context['__thread_vars'][name]
        except KeyError:
            return context.variables[name]

    def set_variable(self, context, name, value):
        if self.executor.multi_thread_mode:
            context.block_context['__thread_vars'][name] = value
        context.variables[name] = value
