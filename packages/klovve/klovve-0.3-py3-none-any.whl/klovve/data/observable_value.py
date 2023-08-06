#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import typing as t


@t.runtime_checkable
class ObservableValueProtocol(t.Protocol):

    def _trigger_changed(self) -> None:
        pass

    def add_changed_handler(self, func: t.Callable[[], None]) -> None:
        pass

    def remove_changed_handler(self, func: t.Callable[[], None]) -> None:
        pass


class ObservableValue(ObservableValueProtocol):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__changed_handlers = []

    def _trigger_changed(self):
        for changed_handler in self.__changed_handlers:
            changed_handler()

    def add_changed_handler(self, func):
        self.__changed_handlers.append(func)

    def remove_changed_handler(self, func):
        self.__changed_handlers.remove(func)
