#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.curses
import klovve.pieces.header

import viwid.widgets.label


class View(klovve.pieces.header.View, klovve.drivers.curses.View):

    def get_native(self, model, model_bind):
        result = viwid.widgets.label.Label()

        @klovve.reaction(owner=result)
        def TODO():
            result.text = model.text

        return result
