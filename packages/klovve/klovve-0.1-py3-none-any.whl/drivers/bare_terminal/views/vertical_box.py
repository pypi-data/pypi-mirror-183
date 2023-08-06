#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.pieces.vertical_box


class View(klovve.pieces.vertical_box.View, klovve.BaseView):

    def get_native(self, model, model_bind):
        class AA:pass
        result = AA()

        @klovve.reaction(owner=result)
        def _():
            self._ff = []
            for item in model.items:
                self._ff.append(item.view().get_native_stuff())

        return result
