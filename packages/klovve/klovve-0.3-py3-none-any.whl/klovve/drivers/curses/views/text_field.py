#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.curses
import klovve.pieces.text_field


import viwid.widgets.entry


class View(klovve.pieces.text_field.View, klovve.drivers.curses.View):

    def get_native(self, model, model_bind):

        result = viwid.widgets.entry.Entry()

        @klovve.reaction(owner=result)
        def TODO():
            result.text = model.text

        def tudo():
            model.text = result.text

        result.listen_property("text", tudo)

        return result

