#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.gtk
import klovve.pieces.checkable


class View(klovve.pieces.checkable.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        return self.gtk_new(klovve.drivers.gtk.Gtk.CheckButton, label=model_bind.text, active=model_bind.is_checked)
