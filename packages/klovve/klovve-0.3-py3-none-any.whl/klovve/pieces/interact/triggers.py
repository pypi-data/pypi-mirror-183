#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.pieces.interact


class Model(klovve.pieces.interact.Model):

    message = klovve.Property()

    triggers = klovve.Property()  # TODO rename


class View(klovve.ComposedView):

    model: Model

    def get_composition(self, model, model_bind, pieces):
        return pieces.interact.abstract(
            message=model_bind.message,
            triggers=model_bind.triggers,
            answer=model_bind.answer,
            is_answered=model_bind.is_answered,
        )
