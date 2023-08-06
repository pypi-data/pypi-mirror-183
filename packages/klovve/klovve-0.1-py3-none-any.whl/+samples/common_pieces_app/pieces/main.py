#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.data
import klovve.pieces.button


class Model(klovve.Model):

    text_a = klovve.observable_property(default=lambda: "Foo")

    is_checked_a = klovve.observable_property(default=lambda: "Foo")


class View(klovve.ComposedView):

    model: Model

    def compose(self, v):
        return pieces.tabbed(
            items=[
                pieces.tabbed.tab(
                    item=pieces.form(
                        items=[
                            pieces.form.section(
                                label="linefield",
                                item=pieces.linefield(text=self.model.text_a),
                            ),
                        ],
                    ),
                    label="Text",
                ),
                pieces.tabbed.tab(
                    item=pieces.form(
                        items=[
                            pieces.form.section(
                                label="checkable",
                                item=pieces.checkable(text="Foo", is_checked=self.model.is_checked_a),
                            ),
                            pieces.form.section(
                                label="slider",
                                item=pieces.slider(value=10, min_value=0, max_value=100, step_value=5),
                            ),
                        ],
                    ),
                    label="Controls",
                ),
                pieces.tabbed.tab(
                    item=pieces.form(
                        items=[
                            pieces.form.section(
                                label="progress",
                                item=pieces.progress(value=0.73),
                            ),
                        ],
                    ),
                    label="Display",
                ),
            ]
        )
