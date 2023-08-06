#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import asyncio
import functools
import inspect
import typing as t
import weakref

import klovve.data.deps
import klovve.data.lists
import klovve.data.observable_value
import klovve.debug
import klovve.threading_  # TODO rename


_TGetValueFunc = t.Callable[[], t.Any]


def _get_none_value_func():
    return None


#  TODO computed_list_model_property


class Model(klovve.data.deps.DependencySubject):

    def __init__(self, **kwargs):
        klovve.debug.memory.new_object_created(self, Model.__name__)
        self.__values = {}
        self.__head_versions = {}
        self.__available_versions = {}
        self.__changed_handlers = {}
        self.__dependencies = {}
        self.__dependencies_versions_useds = {}
        self.__dependencies_handlers = {}
        self.__value_changed_handlers = {}
        self.__next_version = 2
        for k, v in kwargs.items():
            setattr(self, k, v)

    def _value(self, prop: "PropertyBase"):
        klovve.data.deps.notify_dependency(self, prop)
        head_version = self.__head_version(prop)
        available_version = self.__available_version(prop)
        do_refresh = head_version != available_version
        if do_refresh:
            last_result = self.__values.get(prop, None)
            if isinstance(last_result, klovve.data.observable_value.ObservableValueProtocol) \
                    and (prop in self.__value_changed_handlers):
                last_result.remove_changed_handler(self.__value_changed_handlers.pop(prop))
            self.__compute(prop)
        result = self.__values[prop]
        if do_refresh and isinstance(result, klovve.data.observable_value.ObservableValueProtocol):
            trigger_changed = self.__value_changed_handlers[prop] = functools.partial(self._trigger_changed, prop)
            result.add_changed_handler(trigger_changed)
        return result

    def _trigger_changed(self, prop: "PropertyBase"):
        if not klovve.data.deps.notify_property_value_changed(self, prop):
            return
        changed_handlers = self.__changed_handlers.get(prop, None)
        if changed_handlers:
            for i, changed_handler_ in enumerate(reversed(changed_handlers)):
                changed_handler = changed_handler_()
                if not changed_handler:
                    changed_handlers.pop(i)
                    continue
                changed_handler()

    def _set_value(self, prop: "PropertyBase", value):
        if (prop in self.__values) and (self.__values[prop] == value) \
                and (not isinstance(self.__values[prop], klovve.data.observable_value.ObservableValueProtocol)):
            return
        self.__values[prop] = value
        self.__head_versions[prop] = self.__available_versions[prop] = self.__next_version
        self.__next_version += 1
        self._trigger_changed(prop)

    def __add_changed_handler(self, prop, func: t.Callable[[], None]) -> None:
        changed_handlers = self.__changed_handlers.get(prop, None)
        if changed_handlers is None:
            changed_handlers = self.__changed_handlers[prop] = []
        func_weak = weakref.ref(func)
        changed_handlers.append(func_weak)
        weakref.finalize(func, functools.partial(self.__remove_changed_handler, prop, func_weak))

    def __remove_changed_handler(self, prop: "PropertyBase", func: t.Callable[[], None]) -> None:
        changed_handlers = self.__changed_handlers.get(prop, None)
        if changed_handlers:
            for changed_handler_ in list(changed_handlers):
                changed_handler = changed_handler_()
                if not changed_handler or (changed_handler == func):
                    changed_handlers.remove(changed_handler_)

    # noinspection PyProtectedMember
    def __compute(self, prop: "PropertyBase"):
        with klovve.data.deps.detect_dependencies(self, prop):
            new_value = prop._compute(self)
        is_async = inspect.isawaitable(new_value)
        if is_async:
            async def xx():
                with klovve.data.deps.detect_dependencies(self, prop, append=True):
                    new_value_awaited = await new_value
                self._set_value(prop, new_value_awaited)

            if (not prop._use_last_value_during_recompute()) or (prop not in self.__values):
                self._set_value(prop, prop._initially())
            asyncio.get_event_loop().create_task(xx())
        else:
            self._set_value(prop, new_value)

    def _flush_dependency_handlers(self, prop):
        none_tuple = (None, ())
        old_func, old_dependencies = self.__dependencies_handlers.get(prop, none_tuple)
        if old_func:
            for old_dependency_obj, old_dependency_key in old_dependencies:
                old_dependency_obj.__remove_changed_handler(old_dependency_key, old_func)
            self.__dependencies_handlers[prop] = none_tuple

    def _get_dependencies(self, prop):
        return self.__dependencies.get(prop, ())

    def _set_dependencies(self, prop, new_dependencies):
        self.__dependencies[prop] = new_dependencies
        # TODO incorrect?! (not the actual versions)
        self.__dependencies_versions_useds[prop] = {(model, prop_name): model.__available_version(prop_name)
                                                    for model, prop_name in new_dependencies}
        recompute = functools.partial(self.__compute, prop)
        for new_dependency_obj, new_dependency_prop_name in new_dependencies:
            new_dependency_obj.__add_changed_handler(new_dependency_prop_name, recompute)
        self.__dependencies_handlers[prop] = (recompute, new_dependencies)

    def __invalidate(self, prop: "PropertyBase"):
        self.__head_versions[prop] = self.__next_version + 1
        self.__next_version += 1

    def __head_version(self, prop: "PropertyBase"):
        dependencies = self.__dependencies.get(prop, ())
        dependencies_versions_head = {(model, prop_name): model.__head_version(prop_name)
                                      for model, prop_name in dependencies}
        dependencies_versions_used = self.__dependencies_versions_useds.get(prop, {})
        if dependencies_versions_head != dependencies_versions_used:
            self.__invalidate(prop)
        result = self.__head_versions.get(prop, 1)
        return result

    def __available_version(self, prop: "PropertyBase"):
        return self.__available_versions.get(prop, 0)

    def __call__(self, *args, **kwargs):  # TODO  only helps the ide
        return self


# noinspection PyProtectedMember
class PropertyBase(property):

    def __init__(self):
        super().__init__(self._fget, self._fset)

    def _fget(self, obj):
        klovve.threading_.verify_correct_thread()
        return obj._value(self)

    def _fset(self, obj, value):
        klovve.threading_.verify_correct_thread()
        obj._set_value(self, value)

    def _compute(self, obj) -> t.Any:
        raise NotImplementedError()

    def _initially(self) -> t.Any:
        return None

    def _use_last_value_during_recompute(self) -> bool:
        return True


# noinspection PyProtectedMember
class Property(PropertyBase):

    def __init__(self, *, default: t.Callable[[], t.Any] = _get_none_value_func):
        super().__init__()
        self.__get_default = default

    def _compute(self, obj):
        return self.__get_default()


# noinspection PyProtectedMember
class ListProperty(Property):

    def __init__(self, *, default: t.Callable[[], t.Iterable[t.Any]] = lambda: ()):
        super().__init__(default=lambda: klovve.data.lists.List(default()))

    def _fset(self, obj, value):
        klovve.threading_.verify_correct_thread()
        self._fget(obj).update(value)


# noinspection PyProtectedMember
class _ComputedProperty(PropertyBase):

    def __init__(self, func, *, initially: _TGetValueFunc, use_last_value_during_recompute: bool):
        super().__init__()
        self._fct = func
        self.__initially = initially
        self.__use_last_value_during_recompute = use_last_value_during_recompute

    def _initially(self):
        return self.__initially()

    def _use_last_value_during_recompute(self):
        return self.__use_last_value_during_recompute

    def _fset(self, obj, value):
        klovve.threading_.verify_correct_thread()

    def _compute(self, obj):
        return self._fct(obj)


# noinspection PyPep8Naming
def ComputedProperty(func: t.Optional[_TGetValueFunc] = None, *,
                     initially: _TGetValueFunc = _get_none_value_func,
                     use_last_value_during_recompute: bool = True,
                     ) -> t.Callable[[_TGetValueFunc], _ComputedProperty]:
    def decorator(func_):
        return _ComputedProperty(func_, initially=initially,
                                 use_last_value_during_recompute=use_last_value_during_recompute)

    return decorator if (func is None) else decorator(func)


def observe_list(model: "Model", prop_name: str, observer: "klovve.data.lists.ListObserver", *,
                 initialize: bool = True) -> None:  # TODO remove observers?!
    with klovve.data.deps.no_dependency_tracking():
        # noinspection PyProtectedMember
        getattr(model, prop_name)._add_observer(observer, initialize=initialize)
