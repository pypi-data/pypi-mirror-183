#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.curses
import klovve.pieces.scrollable

import viwid.widgets.scrollable


class View(klovve.pieces.scrollable.View, klovve.drivers.curses.View):

    def get_native(self, model, model_bind):
        box = viwid.widgets.scrollable.Scrollable(
            horizontal_expand_greedily=True,
            vertical_expand_greedily=True,
        )

        @klovve.reaction(owner=box)
        def set_item():
            if model.item:
                box.item = model.item.view().get_native_stuff()
            else:
                box.item = None

        return box
