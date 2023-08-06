#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.gtk
import klovve.pieces.label


class View(klovve.pieces.label.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        return self.gtk_new(klovve.drivers.gtk.Gtk.Label, wrap=True, hexpand=True, vexpand=True, label=model_bind.text)
