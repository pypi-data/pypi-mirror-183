#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import pathlib
import klovve.drivers.curses
import klovve.pieces.viewer.image

import viwid.widgets.label


class View(klovve.pieces.viewer.image.View, klovve.drivers.curses.View):

    def get_native(self, model, model_bind):
        return viwid.widgets.label.Label()
