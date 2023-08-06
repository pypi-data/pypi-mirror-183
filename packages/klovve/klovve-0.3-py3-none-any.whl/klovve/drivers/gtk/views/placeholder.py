#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.gtk
import klovve.pieces.placeholder


class View(klovve.pieces.placeholder.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        box = self.gtk_new(klovve.drivers.gtk.Gtk.Box)

        @klovve.reaction(owner=box)
        def set_item():
            for old_child in klovve.drivers.gtk.children(box):
                box.remove(old_child)
            if model.item:
                TODO = model.item.view().get_native_stuff()
                if not isinstance(TODO, klovve.drivers.gtk.Gtk.Window):
                    box.append(TODO)

        return box
