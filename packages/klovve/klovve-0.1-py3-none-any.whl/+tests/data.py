#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only

import os
import sys

# The following hack makes Kloove tests work even without proper package installation. Do not copy that line!
sys.path += (os.path.abspath(__file__ + up * "/..") for up in (1, 3))

import klovve
import klovve.data.lists


def test_simple_model_with_property():

    class MyModel(klovve.Model):

        foo = klovve.Property()

    my_model = MyModel()

    assert my_model.foo is None

    my_model.foo = 2
    assert my_model.foo == 2

    my_model.foo = "bar"
    assert my_model.foo == "bar"


def test_model_property_with_default():

    class MyModel(klovve.Model):

        foo = klovve.Property(default=lambda: 10)

    my_model = MyModel()

    assert my_model.foo == 10

    my_model.foo = 2
    assert my_model.foo == 2


def test_computed_property():

    class MyModel(klovve.Model):

        foo = klovve.Property(default=lambda: 0)

        @klovve.ComputedProperty
        def double_foo(self):
            return self.foo * 2

        @klovve.ComputedProperty
        def quad_foo(self):
            return self.double_foo * 2

    my_model = MyModel()

    assert my_model.foo == 0
    assert my_model.double_foo == 0
    assert my_model.quad_foo == 0

    my_model.foo = 2
    assert my_model.foo == 2
    assert my_model.double_foo == 4
    assert my_model.quad_foo == 8


def test_reaction():

    class MyModel(klovve.Model):

        foo = klovve.Property(default=lambda: 0)

    my_model = MyModel()
    double_foo = -1

    @klovve.reaction(owner=None)
    def _compute_double_foo():
        nonlocal double_foo
        double_foo = my_model.foo * 2

    assert my_model.foo == 0
    assert double_foo == 0

    my_model.foo = 2
    assert my_model.foo == 2
    assert double_foo == 4


def test_list_property():

    class MyModel(klovve.Model):

        foo = klovve.ListProperty()

        @klovve.ComputedProperty
        def concatenated_foo(self):
            return "".join(self.foo)

    my_model = MyModel()

    assert my_model.foo == []
    assert my_model.concatenated_foo == ""

    my_model.foo = ["foo", "bar"]
    assert my_model.foo == ["foo", "bar"]
    assert my_model.concatenated_foo == "foobar"


def test_observing_list_property():

    class MyModel(klovve.Model):

        foo = klovve.ListProperty()

    my_model = MyModel()
    foo_copy = []

    class MyListObserver(klovve.ListObserver):

        def item_added(self, index, item):
            foo_copy.insert(index, item)

        def item_moved(self, from_index, to_index):
            foo_copy.insert(to_index, foo_copy.pop(from_index))

        def item_removed(self, index):
            foo_copy.pop(index)

    klovve.Model.observe_list(my_model, "foo", MyListObserver())  # TODO

    assert my_model.foo == []
    assert foo_copy == []

    my_model.foo.append("a")
    my_model.foo.insert(0, "b")
    my_model.foo.append("z")
    assert my_model.foo == ["b", "a", "z"]
    assert foo_copy == ["b", "a", "z"]

    my_model.foo.remove("a")
    assert my_model.foo == ["b", "z"]
    assert foo_copy == ["b", "z"]

    my_model.foo = ["g", "o"]
    assert my_model.foo == ["g", "o"]
    assert foo_copy == ["g", "o"]
