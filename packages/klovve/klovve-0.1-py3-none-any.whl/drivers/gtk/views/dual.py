#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.pieces.dual
import klovve.drivers.gtk


class View(klovve.pieces.dual.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        gtk = klovve.drivers.gtk.Gtk
        box = self.gtk_new(gtk.Box, orientation=gtk.Orientation.HORIZONTAL)
        inner_left_box = self._view_factory.placeholder(item=model_bind.side_item).view()
        inner_right_box = self._view_factory.placeholder(item=model_bind.main_item).view()
        inner_left_box.get_native_stuff().props.width_request = 200
        inner_left_box.get_native_stuff().props.height_request = 300
        inner_right_box.get_native_stuff().props.width_request = 300
        box.append(inner_left_box.get_native_stuff())
        box.append(inner_right_box.get_native_stuff())
        return box
