#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.curses.views._curses_private.box
import klovve.pieces.horizontal_box


class View(klovve.pieces.horizontal_box.View, klovve.drivers.curses.views._curses_private.box.View):

    def _orientation(self):
        return 1
