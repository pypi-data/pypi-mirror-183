#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.pieces.form
import klovve.drivers.gtk


class View(klovve.pieces.form.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        gtk = klovve.drivers.gtk.Gtk
        result = self.gtk_new(gtk.Box, orientation=gtk.Orientation.VERTICAL, hexpand=True, vexpand=True,
                              halign=gtk.Align.CENTER, valign=gtk.Align.CENTER)

        @klovve.reaction(owner=self)
        def on_items_changed():
            for old_child in klovve.drivers.gtk.children(result):
                result.remove(old_child)
            for item in model.items:
                result.append(item.view().get_native_stuff())

        return result
