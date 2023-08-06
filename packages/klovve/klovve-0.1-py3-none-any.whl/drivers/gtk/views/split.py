#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.gtk
import klovve.pieces.split


class View(klovve.pieces.split.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        gtk = klovve.drivers.gtk.Gtk
        paned = self.gtk_new(gtk.Paned)

        @klovve.reaction(owner=paned)
        def set_item1():
            if model.item1:
                ss = model.item1.view().get_native_stuff()
                paned.set_start_child(ss)
                fuh = ss.compute_expand(gtk.Orientation.HORIZONTAL)  # TODO
                paned.set_resize_start_child(fuh)
            else:
                paned.set_start_child(gtk.Label(visible=False)) #TODO paned.set_start_child(None)

        @klovve.reaction(owner=paned)
        def set_item2():
            if model.item2:
                ss = model.item2.view().get_native_stuff()
                paned.set_end_child(ss)
                fuh = ss.compute_expand(gtk.Orientation.HORIZONTAL)
                paned.set_resize_end_child(fuh)  # TODO
            else:
                paned.set_end_child(gtk.Label(visible=False)) #TODO paned.set_end_child(None)

        paned.set_shrink_start_child(False)
        paned.set_shrink_end_child(False)
        return paned
