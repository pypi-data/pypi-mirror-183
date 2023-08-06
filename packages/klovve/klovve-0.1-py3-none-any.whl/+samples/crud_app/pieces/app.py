#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import asyncio
import dataclasses

import klovve.data
import klovve.pieces.button
import crud_app.pieces.thing


class Model(klovve.Model):

    def __init__(self, domain):
        super().__init__()
        self.__domain = domain

        # TODO unregister handlers later?!

        def on_thing_added(thing_id):
            domain_thing = self.__domain.get_thing_by_id(thing_id)
            self.things.append(crud_app.pieces.thing.Model(domain=domain, id=thing_id,
                                                           name=domain_thing.name, comment=domain_thing.comment))
        domain.thing_added_handlers.append(on_thing_added)

        def on_thing_modified(thing_id):
            thing = [x for x in self.things if x.id == thing_id][0]
            domain_thing = self.__domain.get_thing_by_id(thing_id)
            thing.name = domain_thing.name
            thing.comment = domain_thing.comment
        domain.thing_modified_handlers.append(on_thing_modified)

        def on_thing_removed(thing_id):
            pthing = [x for x in self.things if x.id == thing_id][0]
            self.things.remove(pthing)
        domain.thing_removed_handlers.append(on_thing_removed)

        for thing_id in domain.get_thing_ids():
            on_thing_added(thing_id)  # TODO threading

    things = klovve.ListProperty()

    selected_thing = klovve.Property()  # TODO selection models?!

    async def add_thing(self, context):
        view = context.fabric
        new_name = await context.dialog(
            view.interact.textline(message="Please enter a name for the new thing."))
        if not new_name:
            return
        async with context.error_message_for_exceptions(Exception):
            self.__domain.add_thing(new_name)


class View(klovve.ComposedView[Model]):

    def get_composition(self, model, model_bind, pieces):

        def view_for_thing():
            thing = self.model.selected_thing
            if thing:
                return pieces.form(items=[
                    pieces.form.section(
                        item=pieces.crud_app.thing(thing),
                        label=self.computed(lambda: f"Selected thing '{thing.name}'"),
                    ),
                ])
            else:
                return pieces.label(text=self.computed(lambda: "Select a thing, dude." if (len(self.model.things) > 0) else "Create a thing, dude."))

        def listpanel_item_label(thing):
            return thing.name + (f" ({thing.comment})" if thing.comment else "")

        async def close(context):
            view = context.fabric
            return await context.dialog(view.interact.yesno(message=f"Do you really want to close the app?"))

        return pieces.window(
            title="crud app",
            close_func=close,
            body=pieces.tabbed(
                items=[
                    pieces.tabbed.tab(
                        item=pieces.list_panel(
                            items=model_bind.things,
                            selected_item=model_bind.selected_thing,
                            item_label_func=listpanel_item_label,
                            body=self.computed(view_for_thing),
                            list_actions=[
                                klovve.pieces.button.Model(
                                    text="Add thing",
                                    action=self.model.add_thing,
                                )
                            ],
                        ),
                        label="Things",
                    ),
                    pieces.tabbed.tab(
                        item=pieces.form(
                            items=[
                                pieces.form.section(
                                    label="Number of things",
                                    item=pieces.label(text=self.computed(lambda: str(len(self.model.things)))),
                                ),
                            ],
                        ),
                        label="Statistics",
                    ),
                ],
            ),
        )
