#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.gtk
import klovve.pieces.form.section


class View(klovve.pieces.form.section.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        gtk = klovve.drivers.gtk.Gtk
        result = self.gtk_new(gtk.Box, orientation=gtk.Orientation.VERTICAL)

        result.get_style_context().add_class("klovve_form_section")

        label = self.gtk_new(gtk.Label, label=model_bind(twoway=False).label)
        result.append(label)

        content = self.gtk_new(gtk.Box)
        result.append(content)

        @klovve.reaction(owner=self)
        def on_compute_label_visibility():
            label.set_visible(model.item and model.label)

        @klovve.reaction(owner=self)
        def on_item_changed():
            for old_child in klovve.drivers.gtk.children(content):
                content.remove(old_child)
            if model.item:
                content.append(model.item.view().get_native_stuff())

        return result
