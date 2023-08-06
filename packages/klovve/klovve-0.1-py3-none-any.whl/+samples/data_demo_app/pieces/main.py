#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.data
import klovve.pieces.button


class Model(klovve.Model):

    text_a = klovve.observable_property(default=lambda: "Foo")

    text_b = klovve.observable_property(default=lambda: "Bar")


class View(klovve.ComposedView):

    model: Model

    def compose(self, v):

        @klovve.ComputedObservable(text_a=self.model.text_a)
        def computed1(text_a):
            return text_a.upper()

        @klovve.ComputedObservable(text_a=self.model.text_a, text_b=self.model.text_b)
        def computed2(text_a, text_b):
            return text_a + text_b

        @klovve.ComputedObservable(text_a=self.model.text_a)
        def computed3(text_a):
            return "".join([char for char in reversed(text_a)])

        @computed3.inverse
        def computed3(text):
            return dict(text_a="".join([char for char in reversed(text)]))

        return pieces.tabbed(
            items=[
                pieces.tabbed.tab(
                    item=pieces.form(
                        items=[
                            pieces.form.section(
                                label="Text A",
                                item=pieces.linefield(text=self.model.text_a),
                            ),
                            pieces.form.section(
                                label="Text B",
                                item=pieces.linefield(text=self.model.text_b),
                            ),
                            pieces.form.section(
                                label="Computed binding from Text A",
                                item=pieces.linefield(text=computed1),
                            ),
                            pieces.form.section(
                                label="Computed binding from Text A, two-way",
                                item=pieces.linefield(text=computed3),
                            ),
                            pieces.form.section(
                                label="Computed binding from Text A and B",
                                item=pieces.linefield(text=computed2),
                            ),
                        ],
                    ),
                    label="Computed bindings",
                ),
            ]
        )
