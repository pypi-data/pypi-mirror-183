#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.curses
import klovve.pieces.viewer.pdf

import viwid.widgets.label

class View(klovve.pieces.viewer.pdf.View, klovve.drivers.curses.View):

    def get_native(self, model, model_bind):
        return viwid.widgets.label.Label(text=f"Please find the Krrez documentation here:\n\nfile://{model.path}")
