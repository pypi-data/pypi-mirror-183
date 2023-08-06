#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.data


class Model(klovve.Model):

    def __init__(self, domain, **kwargs):
        super().__init__(**kwargs)
        self.__domain = domain

    id = klovve.Property()
    #TODO _set_id = id.writer

    name = klovve.Property()
    #TODO _set_name = name.writer

    comment = klovve.Property(default=lambda: "")
    #TODO _set_comment = comment.writer

    async def change_comment(self, context):
        view = context.fabric
        new_comment = await context.dialog(
            view.interact.textline(
                message="Please enter a new comment.",
                suggestion=self.comment or "",
            )
        )
        if new_comment is None:
            return
        async with context.error_message_for_exceptions(Exception):
            self.__domain.set_thing_comment(self.id, new_comment)

    async def rename(self, context):
        view = context.fabric
        new_name = await context.dialog(
            view.interact.textline(
                message="Please choose a new name.",
                suggestion=self.name,
            )
        )
        if not new_name:
            return
        async with context.error_message_for_exceptions(Exception):
            self.__domain.set_thing_name(self.id, new_name)

    async def remove(self, context):
        view = context.fabric
        if not await context.dialog(
                view.interact.yesno(message=f"Do you really want to remove '{self.name}'?")):
            return
        async with context.error_message_for_exceptions(Exception):
            self.__domain.remove_thing(self.id)


class View(klovve.ComposedView):

    model: Model

    def get_composition(self, model, model_bind, pieces):
        return pieces.form(items=[
            pieces.form.section(
                item=pieces.label(text=self.model.name),
                label="Name",
            ),
            pieces.form.section(
                item=pieces.label(text=self.computed(lambda v,m: self.model.comment or "-")),
                label="Comment",
            ),
            pieces.form.section(
                item=pieces.button(text="Change comment", action=self.model.change_comment),
                label="",
            ),
            pieces.form.section(
                item=pieces.button(text="Rename thing", action=self.model.rename),
                label="",
            ),
            pieces.form.section(
                item=pieces.button(text="Remove thing", action=self.model.remove),
                label="",
            ),
        ])
