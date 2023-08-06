#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import abc
import typing as t

import klovve.type_loader


class Driver:

    _mainloop = None

    @staticmethod
    def rank() -> float:
        raise NotImplementedError()

    @staticmethod
    def name() -> str:
        raise NotImplementedError()

    @property
    def mainloop(self):
        if not Driver._mainloop:
            Driver._mainloop = self._create_mainloop()
        return Driver._mainloop

    def show_window(self, window):
        raise NotImplementedError()

    def _create_mainloop(self):
        raise NotImplementedError()

    def view_type(self, name_tuple: t.Iterable[str], additional_packages: t.Iterable[str]) -> t.Type["klovve.View"]:
        for kind in [f"drivers.{self.name()}.views", "pieces"]:
            result = klovve.type_loader._try_find_type_per_name_tuple(name_tuple, kind, "View", additional_packages)
            if result:
                return result

    def model_type(self, name_tuple: t.Iterable[str], additional_packages: t.Iterable[str]) -> t.Type["klovve.View"]:
        for kind in [f"drivers.{self.name()}.views", "pieces"]:
            result = klovve.type_loader._try_find_type_per_name_tuple(name_tuple, kind, "Model", additional_packages)
            if result:
                return result
