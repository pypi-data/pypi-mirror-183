#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.pieces.interact.abstract
import klovve.drivers.gtk


class View(klovve.pieces.interact.abstract.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        gtk = klovve.drivers.gtk.Gtk
        box = self.gtk_new(gtk.Box, orientation=gtk.Orientation.VERTICAL, hexpand=True,
                              css_classes=["klovve_interact_box"])
        box.append(self.gtk_new(gtk.Label, wrap=True, label=model_bind(twoway=False).message))
        inner_box = self.gtk_new(gtk.Box)
        box.append(inner_box)
        trigger_box = self.gtk_new(gtk.Box)
        box.append(trigger_box)

        @klovve.reaction(owner=self)
        def on_inner_changed():
            for old_item in klovve.drivers.gtk.children(inner_box):
                inner_box.remove(old_item)
            if model.inner_view:
                inner_box.append(model.inner_view.view().get_native_stuff())

        @klovve.reaction(owner=self)
        def on_triggers_changed():
            for old_item in klovve.drivers.gtk.children(trigger_box):
                trigger_box.remove(old_item)
            def mkfoo(i):
                def foo(_):
                    model.set_answer(model.get_answer_func(i))
                return foo
            for i, trigger_text in enumerate(model.triggers):
                btn = self.gtk_new(gtk.Button, label=trigger_text)
                box.append(btn)
                btn.connect("clicked", mkfoo(i))

        return box
