#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.curses
import klovve.pieces.placeholder

import viwid.widgets.box


class View(klovve.pieces.placeholder.View, klovve.drivers.curses.View):

    def get_native(self, model, model_bind):
        box = viwid.widgets.box.Box()  # TODO

        @klovve.reaction(owner=box)
        def set_item():
            box.children = [model.item.view().get_native_stuff()] if model.item else []

        return box
