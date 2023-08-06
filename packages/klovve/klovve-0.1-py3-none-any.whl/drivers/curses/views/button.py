#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import asyncio
import contextlib
import traceback

import klovve.application
import klovve.pieces.button
import klovve.drivers.curses

import viwid.widgets.button
import viwid.widgets.box
import viwid.screen


class View(klovve.pieces.button.View, klovve.drivers.curses.View):

    def get_native(self, model, model_bind):
        button = viwid.widgets.button.Button()

        @klovve.reaction(owner=button)
        def TODO():
            button.text = model.text

        button.on_click.append(lambda: asyncio.get_running_loop().call_soon(
            lambda: klovve.application.call_with_kwargs_maybe_async(
                model.action, asyncio.get_running_loop(),
                context=Context(self._view_factory, button),
                model=model,
                model_bind=klovve.view.BindFactory(model),
                pieces=self._view_factory
            ) and False# TODO needed for idle_add
        ))

        return button


class Context:

    def __init__(self, fabric, button):
        self.__fabric = fabric
        self.__button = button

    @contextlib.asynccontextmanager
    async def error_message_for_exceptions(self, *exception_types):
        try:
            yield
        except Exception as ex:
            if isinstance(ex, exception_types):
                await self.dialog(self.__fabric.interact.message(message=str(ex)))
                traceback.print_exc()#TODO weg
            else:
                raise ex

    async def dialog(self, view):
        view = view.view()

        popover = viwid.widgets.box.Box(children=[view.get_native_stuff()])
        closer = self.__button.screen.popup(popover,
                                    alignment=viwid.screen.RootAlignment(
                                        viwid.screen.AnchorRootAlignmentPositioning(self.__button),
                                        viwid.screen.AnchorRootAlignmentPositioning(self.__button),
                                        viwid.screen.AutoRootAlignmentSizing(),
                                        viwid.screen.AutoRootAlignmentSizing()
                                    ))
        done_future = asyncio.Future()
        @klovve.reaction(owner=None)
        def _():
            nonlocal done_future
            if view._model.is_answered:
                done_future.set_result(None)
                closer()
        await done_future
        return view._model.answer

    @property
    def fabric(self):
        return self.__fabric
