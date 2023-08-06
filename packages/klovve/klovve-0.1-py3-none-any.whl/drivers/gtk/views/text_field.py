#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.gtk
import klovve.pieces.text_field


class View(klovve.pieces.text_field.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        return self.gtk_new(klovve.drivers.gtk.Gtk.Entry, text=model_bind.text,
                            placeholder_text=model_bind(twoway=False).hint_text)
