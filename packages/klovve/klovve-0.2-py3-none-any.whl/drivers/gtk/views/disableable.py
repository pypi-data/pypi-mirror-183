#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.gtk
import klovve.pieces.disableable


class View(klovve.pieces.disableable.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        box = self.gtk_new(klovve.drivers.gtk.Gtk.Box)

        @klovve.reaction(owner=box)
        def set_item():
            for old_child in klovve.drivers.gtk.children(box):
                box.remove(old_child)
            if model.item:
                box.append(model.item.view().get_native_stuff())

        @klovve.reaction(owner=box)
        def set_sensitive():
            box.set_sensitive(not model.is_disabled)

        return box
