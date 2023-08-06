#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.pieces.headered_panel


class View(klovve.pieces.headered_panel.View, klovve.BaseView):

    def get_native(self, model, model_bind):
        class AA:pass
        result = AA()

        @klovve.reaction(owner=result)
        def _():
            if model.body:
                item = model.body
                if item:
                    result._foo = item.view().get_native_stuff()

        return result
