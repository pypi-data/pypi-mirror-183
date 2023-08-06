#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.pieces.tabbed.tab


class View(klovve.pieces.tabbed.tab.View, klovve.ComposedView):

    def get_composition(self, model, model_bind, pieces):
        return pieces.placeholder(item=model.item)
