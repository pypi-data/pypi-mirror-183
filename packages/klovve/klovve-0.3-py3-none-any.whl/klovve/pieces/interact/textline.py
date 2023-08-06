#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.pieces.interact


class Model(klovve.pieces.interact.Model):

    message = klovve.Property(default=lambda: "")

    suggestion = klovve.Property(default=lambda: "")


class View(klovve.ComposedView[Model]):

    class TModel(klovve.Model):  # TODO
        value = klovve.Property(default=lambda: "")

    def get_composition(self, model, model_bind, pieces):
        answer = View.TModel()
        @klovve.reaction(owner=self)
        def _():
            answer.value = model.suggestion
        # klovve.data.bind(answer, self.model.suggestion, one_way=True)
        linefield = pieces.text_field(text=model_bind(model=answer).value)
        return pieces.interact.abstract(
            message=model_bind.message,
            inner_view=linefield,
            triggers=["OK", "Cancel"],
            answer=model_bind.answer,
            is_answered=model_bind.is_answered,
            get_answer_func=lambda i: (answer.value if (i == 0) else None)
        )
