#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import asyncio
import klovve.application
import klovve.drivers.gtk
import klovve.pieces.headered_panel


class Model(klovve.pieces.headered_panel.Model):

    @klovve.ComputedProperty
    def title_label_css_classes(self):
        if self.state == self.State.BUSY:
            return ["headered_title_busy"]
        elif self.state == self.State.SUCCESSFUL:
            return ["headered_title_successful"]
        elif self.state == self.State.SUCCESSFUL_WITH_WARNING:
            return ["headered_title_successful_with_warning"]
        elif self.state == self.State.FAILED:
            return ["headered_title_failed"]
        else:
            return []


class View(klovve.pieces.headered_panel.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        gtk = klovve.drivers.gtk.Gtk
        box = self.gtk_new(gtk.Box, orientation=gtk.Orientation.VERTICAL)
        header_bar = self.gtk_new(gtk.HeaderBar, show_title_buttons=False)
        box.append(header_bar)
        progressbar = self.gtk_new(gtk.ProgressBar, fraction=model_bind(twoway=False).progress)
        box.append(progressbar)
        ibox = self.gtk_new(gtk.Box)
        box.append(ibox)
        title_box = self.gtk_new(gtk.Box, orientation=gtk.Orientation.HORIZONTAL)
        state_box = self.gtk_new(gtk.Box, orientation=gtk.Orientation.HORIZONTAL, css_classes=["headered_state_box"])
        title_label = self.gtk_new(gtk.Label, label=model_bind(twoway=False).title,
                                   css_classes=model_bind.title_label_css_classes)
        title_box.append(state_box)
        title_box.append(title_label)
        header_bar.set_title_widget(title_box)
        header_bar.pack_end(self._view_factory.horizontal_box(items=model_bind.title_secondary_items).view().get_native_stuff())
        header_bar.pack_start(self._view_factory.horizontal_box(items=model_bind.actions).view().get_native_stuff())

        @klovve.reaction(owner=box)
        def _handle_state():
            for old_widget in klovve.drivers.gtk.children(state_box):
                state_box.remove(old_widget)
            if model.state == klovve.pieces.headered_panel.Model.State.BUSY:
                state_box.append(self.gtk_new(gtk.Spinner, spinning=True))
            elif model.state == klovve.pieces.headered_panel.Model.State.SUCCESSFUL:
                state_box.append(gtk.Image.new_from_icon_name("dialog-ok"))
            elif model.state == klovve.pieces.headered_panel.Model.State.SUCCESSFUL_WITH_WARNING:
                state_box.append(gtk.Image.new_from_icon_name("dialog-warning"))
            elif model.state == klovve.pieces.headered_panel.Model.State.FAILED:
                state_box.append(gtk.Image.new_from_icon_name("dialog-error"))
            else:
                title_label.set_css_classes([])

        @klovve.reaction(owner=box)
        def _set_body():
            for old_child in klovve.drivers.gtk.children(ibox):
                ibox.remove(old_child)
            if model.body:
                item = model.body
                if item:
                    ibox.append(item.view().get_native_stuff())

        return box
