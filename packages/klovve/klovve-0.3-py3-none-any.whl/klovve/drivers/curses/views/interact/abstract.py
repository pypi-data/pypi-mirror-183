#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only

import klovve.pieces.interact.abstract
import klovve.drivers.curses

import viwid.widgets.label
import viwid.widgets.box
import viwid.widgets.button


class View(klovve.pieces.interact.abstract.View, klovve.drivers.curses.View):

    def get_native(self, model, model_bind):
        msg = viwid.widgets.label.Label()
        inner_box = viwid.widgets.box.Box()  # TODO
        btnbox = viwid.widgets.box.Box(
            orientation = viwid.widgets.box.Orientation.HORIZONTAL)
        box = viwid.widgets.box.Box(
            orientation = viwid.widgets.box.Orientation.VERTICAL,
            children=[msg, inner_box, btnbox])

        @klovve.reaction(owner=self)
        def on_message_changed():
            msg.text = model.message

        @klovve.reaction(owner=self)
        def on_inner_changed():
            inner_box.children = [model.inner_view.view().get_native_stuff()] if model.inner_view else []

        @klovve.reaction(owner=self)
        def on_triggers_changed():
#            for old_item in klovve.drivers.gtk.children(trigger_box):
 #               trigger_box.remove(old_item)
            def mkfoo(i):
                def foo():
                    model.set_answer(model.get_answer_func(i))
                return foo
            boxes = []
            for i, trigger_text in enumerate(model.triggers):
                btn = viwid.widgets.button.Button(text=trigger_text)
                #btn = self.gtk_new(gtk.Button, label=trigger_text)
                boxes.append(btn)
                btn.on_click.append(mkfoo(i))
            btnbox.children = boxes

        return box
