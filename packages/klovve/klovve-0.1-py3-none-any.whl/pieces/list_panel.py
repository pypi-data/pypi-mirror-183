#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve


class Model(klovve.Model):

    items = klovve.ListProperty()

    selected_item = klovve.Property()

    body = klovve.Property()

    item_label_func = klovve.Property()

    list_actions = klovve.ListProperty()

    item_actions = klovve.ListProperty()

    barz = klovve.ListProperty()


class View(klovve.ComposedView[Model]):

    def get_composition(self, model, model_bind, pieces):
        return pieces.split(
            item1=pieces.list(
                items=model_bind(twoway=False).items,   # TODO list bindings?!
                selected_item=model_bind.selected_item,
                list_actions=model_bind(twoway=False).list_actions,
                item_actions=model_bind(twoway=False).item_actions,
                item_label_func=model_bind(twoway=False).item_label_func,
                barz=model_bind(twoway=False).barz,
            ),
            item2=model_bind(twoway=False).body,
        )
