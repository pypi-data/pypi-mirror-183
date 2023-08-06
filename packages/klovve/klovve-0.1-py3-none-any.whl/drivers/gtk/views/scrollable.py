#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.gtk
import klovve.pieces.scrollable


class View(klovve.pieces.scrollable.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        gtk = klovve.drivers.gtk.Gtk
        scrolled_window = self.gtk_new(gtk.ScrolledWindow, hexpand=True, vexpand=True,
                                       hscrollbar_policy=gtk.PolicyType.NEVER, propagate_natural_height=True)
        box = self.gtk_new(gtk.Box)
        scrolled_window.set_child(box)

        @klovve.reaction(owner=scrolled_window)
        def _():
            for old_child in klovve.drivers.gtk.children(box):
                box.remove(old_child)
            if model.item:
                box.append(model.item.view().get_native_stuff())

        return scrolled_window
