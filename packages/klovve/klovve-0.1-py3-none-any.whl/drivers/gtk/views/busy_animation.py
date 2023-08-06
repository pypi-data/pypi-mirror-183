#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.gtk
import klovve.pieces.busy_animation


class Model(klovve.pieces.busy_animation.Model):

    @klovve.ComputedProperty
    def spinner_size(self):
        return {
            self.Size.TINY: (1, 1),
            self.Size.SMALL: (24, 24),
            self.Size.MEDIUM: (32, 32),
            self.Size.LARGE: (64, 64),
            self.Size.EXTRA_LARGE: (128, 128),
        }[self.size or self.Size.MEDIUM]

    @klovve.ComputedProperty
    def gtk_orientation(self):
        gtk = klovve.drivers.gtk.Gtk
        if self.orientation:
            v = self.orientation
        else:
            v = self.Orientation.HORIZONTAL if (self.size <= self.Size.TINY) else self.Orientation.VERTICAL
        return {
            self.Orientation.HORIZONTAL: gtk.Orientation.HORIZONTAL,
            self.Orientation.VERTICAL: gtk.Orientation.VERTICAL,
        }[v]


class View(klovve.pieces.busy_animation.View, klovve.drivers.gtk.View):

    model: Model

    def get_native(self, model, model_bind):
        gtk = klovve.drivers.gtk.Gtk
        box = self.gtk_new(gtk.Box, orientation=model_bind.gtk_orientation)
        spinner = self.gtk_new(gtk.Spinner, spinning=True, hexpand=True, vexpand=True, valign=gtk.Align.CENTER)
        box.append(spinner)
        label = self.gtk_new(gtk.Label, hexpand=True, vexpand=True,
                             label=model_bind(twoway=False, converter_in=lambda v: v or "").text,
                             visible=model_bind(twoway=False, converter_in=lambda v: bool(v)).text)
        box.append(label)

        @klovve.reaction(owner=box)
        def set_spinner_size():
            spinner.set_size_request(*model.spinner_size)

        return box
