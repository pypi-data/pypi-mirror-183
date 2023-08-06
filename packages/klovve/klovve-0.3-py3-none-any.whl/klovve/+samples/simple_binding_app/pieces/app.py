#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve


class Model(klovve.Model):

    my_text = klovve.Property(default=lambda: "Foo")


class View(klovve.ComposedView[Model]):

    def get_composition(self, model, model_bind, pieces):
        return pieces.window(
            title=klovve.computed_value(lambda: f"Length: {len(self.model.my_text)}"),
            body=pieces.vertical_box(items=[
                pieces.text_field(text=model_bind.my_text),
                pieces.label(text=model_bind.my_text),
                pieces.text_field(text=model_bind.my_text),
            ]),
        )
