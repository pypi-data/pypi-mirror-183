#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import typing as t

import klovve.debug
import klovve.data.deps
import klovve.data.value_holder

if t.TYPE_CHECKING:
    import klovve.drivers
    import klovve.type_loader


_TViewSpec = t.Callable[["ViewFactory"], "ViewTreeNode"]


_TGoo = t.TypeVar("_TGoo", bound="klovve.Model")#TODO


class BaseView(t.Generic[_TGoo]):

    def __init__(self, model: _TGoo, view_factory: "ViewFactory"):
        klovve.debug.memory.new_object_created(self, BaseView.__name__)
        self._model: _TGoo = model
        self._view_factory = view_factory
        self.__result = None

    def get_native(self, model: _TGoo, model_bind: _TGoo) -> object:
        raise NotImplementedError(f"TODO {type(self).__qualname__} {type(self).__module__}")
        raise NotImplementedError()

    def get_native_stuff(self):
        if not self.__result:
            bind_factory = BindFactory(self._model)
            # noinspection PyTypeChecker
            self.__result = self.get_native(self._model, bind_factory)
        return self.__result


class ComposedView(BaseView, t.Generic[_TGoo]):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__result = self._view_factory.create_view(("placeholder",))
        self.__tree = None

    def get_native(self, model, model_bind):
        @klovve.reaction(owner=self)
        def _ui():
            # noinspection PyTypeChecker
            compo = self.get_composition(model, model_bind, self._view_factory)
            with klovve.data.deps.no_dependency_tracking():
                compo.create_or_update_view(self._model, self.__result, self.__tree)
                self.__tree = compo

        return self.__result.get_native_stuff()

    def computed(self, func) -> "klovve.data.value_holder.ValueHolder":
        return klovve.data.value_holder.ComputedValue(func, self._model, BindFactory(self._model), self._view_factory)

    def get_composition(self, model, model_bind: _TGoo, pieces: "ViewFactory") -> "ViewTreeNode":
        raise NotImplementedError()


class BindFactory:

    def __init__(self, model, twoway=True, converter_in=None, converter_out=None):
        self.__model = model
        self.__twoway = twoway
        self.__converter_in = converter_in
        self.__converter_out = converter_out

    def __getattr__(self, prop_name):
        if self.__twoway:
            return klovve.data.value_holder.TwoWayBinding(self.__model, prop_name,
                                                          converter_in=self.__converter_in,
                                                          converter_out=self.__converter_out)
        else:
            return klovve.data.value_holder.OneWayBinding(self.__model, prop_name,
                                                          converter_in=self.__converter_in,
                                                          converter_out=self.__converter_out)

    def __call__(self, *, model=None, twoway=True, converter_in=None, converter_out=None):
        return BindFactory(model or self.__model, twoway=twoway,
                           converter_in=converter_in or self.__converter_in,
                           converter_out=converter_out or self.__converter_out)


class ViewTreeNode:

    def __init__(self, view_factory, name_tuple, model, data: t.Iterable[tuple[str, t.Any]]):
        klovve.debug.memory.new_object_created(self, ViewTreeNode.__name__)
        self.__view_factory = view_factory
        self.__name_tuple = name_tuple
        self.__model = model
        self.__data = dict(data)
        self.__view = None

    def __str__(self):
        return f"<{self.__name_tuple}>" # TODO

    @property
    def name_tuple(self) -> t.Iterable[str]:
        return self.__name_tuple

    @property
    def model(self) -> t.Optional["klovve.Model"]:
        return self.__model

    @property
    def data(self) -> dict[str, t.Any]:
        return dict(self.__data)

    def view(self) -> "klovve.BaseView":
        if not self.__view:
            zeug = []
            value_holders = []
            rk = {}
            if not self.model:
                for k, v in self.data.items():
                    if isinstance(v, klovve.data.value_holder.ValueHolder):
                        value_holders.append((k, v))
                    else:
                        rk[k] = v
            self.__view = self.__view_factory.create_view(self.name_tuple, model=self.model, **rk)

            for value_holder in value_holders:
                zeug.append(_connect_value_holder(self.__view._model, *value_holder))

            self.__view.__zeug = zeug

        return self.__view

    def create_or_update_view(self, model: "klovve.Model", placeholder, old_tree: "ViewTreeNode"):
        self.__create_or_update_view(old_tree, self, model, placeholder, "item")

    def __create_or_update_view(self, old_tree: "ViewTreeNode", new_tree: "ViewTreeNode", model: "klovve.Model",
                                parent_view: "klovve.BaseView", parent_view_prop_name: str):
        with klovve.data.deps.defer_value_propagation(): # TODO xx xxxxx

            if (not old_tree) or not hasattr(new_tree, "name_tuple") or not hasattr(old_tree, "name_tuple") or (new_tree.name_tuple != old_tree.name_tuple) or (new_tree.model != old_tree.model):  # TODO EQU  TODO sleutel
                setattr(parent_view._model, parent_view_prop_name, self)
            else:
                existing_view = getattr(parent_view._model, parent_view_prop_name).view()
                zeug = new_tree._zeug = []
                for prop_key, prop_value in new_tree.data.items():  # TODO remove/reset other keys
                    # TODO all odd
                    if isinstance(prop_value, ViewTreeNode):
                        Xold_tree = old_tree.data.get(prop_key, None)
                        self.__create_or_update_view(Xold_tree, prop_value, model, existing_view, prop_key)
                    elif isinstance(prop_value, klovve.data.value_holder.ValueHolder):
                        zeug.append(_connect_value_holder(existing_view._model, prop_key, prop_value))
                    else:
                        setattr(existing_view._model, prop_key, prop_value)


class ViewFactory:
    class _Node:

        def __init__(self, view_factory: "ViewFactory", view_name: t.Iterable[str]):
            self.__view_factory = view_factory
            self.__view_name = view_name

        def __getattr__(self, item: str) -> "ViewFactory._Node":
            return ViewFactory._Node(self.__view_factory, (*self.__view_name, item))

        def __call__(self, model_or_model_type=None, /, **kwargs):
            model = model_or_model_type() if isinstance(model_or_model_type, type) else model_or_model_type
            return ViewTreeNode(self.__view_factory, self.__view_name, model, kwargs)

    def create_view(self, name_tuple: t.Iterable[str], /, *, model=None, **kwargs) -> "klovve.View":
        model_type = model or self.__type_loader.model_type(name_tuple, driver=self.__driver)
        if not model_type:
            raise ViewError(f"Unable to find the model type for {name_tuple}")
        model = model_type()
        for key, value in kwargs.items():
            setattr(model, key, value)
        return self.__type_loader.view_type(name_tuple, driver=self.__driver)(model, self)

    def __getattr__(self, item) -> "ViewFactory._Node":
        return ViewFactory._Node(self, (item,))

    def __init__(self, type_loader: "klovve.type_loader.TypeLoader", driver: "klovve.drivers.Driver", TODO: "app"):
        self.__type_loader = type_loader
        self.__driver = driver
        #self.TODO = TODO


class ViewError(Exception):
    pass


def _connect_value_holder(target_model: "klovve.Model", target_prop_name: str,
                          value_holder: "klovve.data.value_holder.ValueHolder") -> object:

    @klovve.reaction(owner=None)
    def _handle_to_target():
        value = value_holder.get_value()
        with klovve.data.deps.no_dependency_tracking():
            setattr(target_model, target_prop_name, value)

    @klovve.reaction(owner=_handle_to_target)
    def _handle_from_target():
        if value_holder.is_settable():
            value = getattr(target_model, target_prop_name)
            with klovve.data.deps.no_dependency_tracking():
                value_holder.set_value(value)

    return _handle_to_target
