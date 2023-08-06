#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import abc
import inspect
import typing as t


class ValueHolder(abc.ABC):

    @abc.abstractmethod
    def get_value(self) -> t.Any:
        pass

    @abc.abstractmethod
    def set_value(self, value: t.Any) -> None:
        pass

    @abc.abstractmethod
    def is_settable(self) -> bool:
        pass


class OneWayBinding(ValueHolder):

    def __init__(self, model, prop_name, converter_in=None, converter_out=None):
        super().__init__()
        self.__model = model
        self.__prop_name = prop_name
        self.__converter_in = converter_in
        self.__converter_out = converter_out

    def get_value(self):
        result = getattr(self.__model, self.__prop_name)
        if self.__converter_in:
            result = self.__converter_in(result)
        return result

    def set_value(self, value):
        if self.is_settable():
            if self.__converter_out:
                value = self.__converter_out(value)
            setattr(self.__model, self.__prop_name, value)

    def is_settable(self):
        return False


class TwoWayBinding(OneWayBinding):

    def __init__(self, model, prop_name, converter_in=None, converter_out=None):
        super().__init__(model, prop_name, converter_in, converter_out)

    def is_settable(self):
        return True


class ComputedValue(ValueHolder):

    def __init__(self, func, model, model_bind, pieces):
        super().__init__()
        func_args_count = len(inspect.signature(func).parameters)
        func_args = (model, model_bind, pieces)[:func_args_count]
        self.__func = lambda: func(*func_args)

    def get_value(self):
        return self.__func()

    def set_value(self, value):
        pass

    def is_settable(self):
        return False
