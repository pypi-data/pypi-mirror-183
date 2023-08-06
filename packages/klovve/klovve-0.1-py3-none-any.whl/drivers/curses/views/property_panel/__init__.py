#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.curses
import klovve.pieces.property_panel

import viwid.widgets.label

class View(klovve.pieces.property_panel.View, klovve.drivers.curses.View):

    def get_native(self, model, model_bind):
        model.values["hostname"] = "nnn"
        return viwid.widgets.label.Label(text="TODO")
