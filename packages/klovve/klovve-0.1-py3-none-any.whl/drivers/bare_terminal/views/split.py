#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.pieces.split


class View(klovve.pieces.split.View, klovve.BaseView):

    def get_native(self, model, model_bind):
        class AA:pass
        result = AA()

        @klovve.reaction(owner=result)
        def _():
            if model.item1:
                item = model.item1
                if item:
                    result._foo = item.view().get_native_stuff()
            if model.item2:
                item = model.item2
                if item:
                    result._fofo = item.view().get_native_stuff()

        return result
