#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.gtk
import klovve.pieces.header


class View(klovve.pieces.header.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        return self.gtk_new(klovve.drivers.gtk.Gtk.Label, wrap=True, label=model_bind(twoway=False).text,
                            css_classes=["klovve_header"])
