#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import abc

import importlib.util
import pkgutil
import traceback
import typing as t

if t.TYPE_CHECKING:
    import klovve.drivers
    import klovve.data.value_holder


class TypeLoader(abc.ABC):

    @abc.abstractmethod
    def driver_type(self) -> t.Type["klovve.drivers.Driver"]:
        pass

    @abc.abstractmethod
    def view_base_type(self, name_tuple: t.Iterable[str]) -> t.Type["klovve.View"]:
        pass

    @abc.abstractmethod
    def view_type(self, name_tuple: t.Iterable[str], *, driver: "klovve.drivers.Driver") -> t.Type["klovve.View"]:
        pass

    @abc.abstractmethod
    def model_type(self, name_tuple: t.Iterable[str]) -> t.Type["klovve.Model"]:
        pass


class DefaultTypeLoader(TypeLoader):

    def __init__(self, additional_packages: t.Iterable[str]):
        self.__additional_packages = tuple(additional_packages)

    def driver_type(self):
        driver_types = []
        for package in ["", "klovve", self.__additional_packages]:  # TODO same order as in _find_modules ?!
            ppackage = f"{package}." if package else ""
            spec = importlib.util.find_spec(f"{ppackage}drivers")
            if spec:
                for module_info in pkgutil.iter_modules(spec.submodule_search_locations):
                    try:
                        driver_module = importlib.import_module(f"{ppackage}drivers.{module_info.name}")
                    except Exception:
                        #traceback.print_exc()  # TODO
                        continue
                    driver_types.append(driver_module.Driver)
        driver_types.sort(key=lambda driver_type: driver_type.rank())
        return driver_types[0]

    def view_base_type(self, name_tuple):
        return _try_find_type_per_name_tuple(name_tuple, "pieces", "View", self.__additional_packages)

    def view_type(self, name_tuple, *, driver):
        return driver.view_type(name_tuple, self.__additional_packages)

    def model_type(self, name_tuple, *, driver):
        return driver.model_type(name_tuple, self.__additional_packages)


def _try_find_type_per_name_tuple(name_tuple: t.Iterable[str], kind: str, typename: str,
                                  additional_packages: t.Iterable[str]):
    for module_name in _find_modules(name_tuple, kind, additional_packages):
        kind_type = _try_find_type_in_module(module_name, typename)
        if kind_type:
            return kind_type


def _try_find_type_in_module(module_name: str, typename: str):
    try:
        return getattr(importlib.import_module(module_name), typename, None)
    except ImportError:
        return


def _find_modules(name_tuple: t.Iterable[str], kind: str, additional_packages: t.Iterable[str]):
    yield f"klovve.{kind}." + ".".join(name_tuple)
    for i in range(len(tuple(name_tuple))):
        package_name_end = ".".join([*name_tuple[:i], kind, *name_tuple[i:]])
        for additional_package in ["", *additional_packages]:
            yield (f"{additional_package}." if additional_package else "") + package_name_end
