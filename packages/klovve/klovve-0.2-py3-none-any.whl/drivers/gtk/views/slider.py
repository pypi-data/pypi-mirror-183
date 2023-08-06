#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.pieces.slider
import klovve.drivers.gtk


class View(klovve.pieces.slider.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        gtk = klovve.drivers.gtk.Gtk
        scale = self.gtk_new(gtk.Scale)
        self.bind(scale.props.adjustment, "step_increment", model_bind(twoway=False).step_value)
        self.bind(scale.props.adjustment, "lower", model_bind(twoway=False).min_value)
        self.bind(scale.props.adjustment, "upper", model_bind(twoway=False).max_value)
        self.bind(scale.props.adjustment, "value", model_bind.value)
        return scale
