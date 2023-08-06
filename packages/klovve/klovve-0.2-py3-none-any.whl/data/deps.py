#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only

"""
Dependency tracking for model properties.

Klovve applications typically do not need anything from here.
"""

import contextlib
import contextvars
import typing as t

if t.TYPE_CHECKING:
    import klovve.data.model


_current_compute_dependencies: contextvars.ContextVar[
    t.Optional[list[tuple["klovve.data.model.Model", "klovve.data.model.PropertyBase"]]]] = \
    contextvars.ContextVar("_current_compute_dependencies", default=None)


@contextlib.contextmanager
def no_dependency_tracking() -> t.ContextManager[None]:
    """
    Stops dependency tracking of the current computation for a code block.

    Use it for a :code:`with` statement. Model property accesses do not count as a dependency in that :code:`with`
    block.

    It will not influence dependency tracking for other computations inside yours (i.e. if you access a computed
    property, the dependency tracking of this one will not break).
    """
    currently_computing_token = _current_compute_dependencies.set(None)
    try:
        yield
    finally:
        _current_compute_dependencies.reset(currently_computing_token)


_defer_value_propagation = 0
_defer_value_propagation_for: t.Optional[list[tuple["klovve.data.model.Model",
                                                    "klovve.data.model.PropertyBase"]]] = None


# noinspection PyProtectedMember
@contextlib.contextmanager
def defer_value_propagation() -> t.ContextManager[None]:
    """
    Defers the automatic refreshes on model property changes for a code block and applies them afterwards.

    Use it for a :code:`with` statement. Model property modifications do not instantly lead to updates on depending
    properties in that :code:`with` block.

    Computed properties will always return the right value on access, not an outdated one.
    """
    global _defer_value_propagation, _defer_value_propagation_for
    if _defer_value_propagation == 0:
        _defer_value_propagation_for = []
    _defer_value_propagation += 1
    try:
        yield
    finally:
        _defer_value_propagation -= 1
        if _defer_value_propagation == 0:
            changed_values = list(dict.fromkeys(_defer_value_propagation_for))
            _defer_value_propagation_for = None
            for obj, prop in changed_values:
                obj._trigger_changed(prop)


_TDependencyTuple = tuple["klovve.data.model.Model", "klovve.data.model.PropertyBase"]


class DependencySubject:
    """
    Base class for objects that can attend on dependency tracking.

    See :py:func:`detect_dependencies` and others.
    """

    def _flush_dependency_handlers(self, prop: "klovve.data.model.PropertyBase") -> None:
        pass

    def _get_dependencies(self, prop: "klovve.data.model.PropertyBase") -> t.Iterable[_TDependencyTuple]:
        pass

    def _set_dependencies(self, prop: "klovve.data.model.PropertyBase",
                          new_dependencies: t.Iterable[_TDependencyTuple]) -> None:
        pass


# noinspection PyProtectedMember
@contextlib.contextmanager
def detect_dependencies(subject: DependencySubject, prop: "klovve.data.model.PropertyBase", *,
                        append: bool = False) -> t.ContextManager[None]:
    """
    Detect dependencies for a code block.

    Use it for a :code:`with` statement.

    :param subject: The object to track dependencies for.
    :param prop: The property of that object to track dependencies for.
    :param append: If to append dependencies in this block to the known one (instead of replacing them).
    """
    if not append:
        subject._flush_dependency_handlers(prop)
    old_current_compute_dependencies = _current_compute_dependencies.set([])
    try:
        yield
    finally:
        new_dependencies = tuple(set(_current_compute_dependencies.get()
                                     + list(subject._get_dependencies(prop) if append else ())))
        _current_compute_dependencies.reset(old_current_compute_dependencies)
    subject._set_dependencies(prop, new_dependencies)


def notify_dependency(model: "klovve.data.model.Model", prop: "klovve.data.model.PropertyBase") -> None:
    """
    Notify the dependency tracking about a new dependency for the current computation (usually after a property read
    access).

    :param model: The new dependency model.
    :param prop: The dependency property in the model.
    """
    current_compute_dependencies = _current_compute_dependencies.get()
    if current_compute_dependencies is not None and (model, prop) not in current_compute_dependencies:
        current_compute_dependencies.append((model, prop))


def notify_property_value_changed(model: "klovve.data.model.Model", prop: "klovve.data.model.PropertyBase") -> bool:
    """
    Notify the dependency tracking about the change of a model property.

    :param model: The model that was changed.
    :param prop: The changed property in the model.
    """
    if _defer_value_propagation_for is not None:
        _defer_value_propagation_for.append((model, prop))
        return False
    return True
