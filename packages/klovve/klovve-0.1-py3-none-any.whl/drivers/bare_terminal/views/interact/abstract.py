#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import sys
import klovve.pieces.interact.abstract


class View(klovve.pieces.interact.abstract.View, klovve.BaseView):

    def get_native(self, model, model_bind):
        class AA:pass
        result = AA()

        # TODO
        print(model.message, file=sys.stderr)
        if len(model.triggers) == 1:
            model.answer = True

        return result
