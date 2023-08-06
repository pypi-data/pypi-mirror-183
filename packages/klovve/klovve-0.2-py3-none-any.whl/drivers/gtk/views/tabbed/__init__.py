#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.pieces.tabbed
import klovve.drivers.gtk


class View(klovve.pieces.tabbed.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        gtk = klovve.drivers.gtk.Gtk
        #kind = self.get_hint("kind", "foo")#TODO
        result = self.gtk_new(gtk.Notebook)

        @klovve.reaction(owner=self)
        def handle():
            for old_child in range(result.get_n_pages()):
                result.remove_page(-1)
            for item in model.items:
                itemview = item.view()
                with klovve.data.deps.no_dependency_tracking():#TODO (otherwise studio tabs behave odd on first reload)
                    widget = itemview._model.item.view().get_native_stuff()

                #TODO even needed?!
                #if widget.props.parent:
                 #   widget.props.parent.remove(widget)

                result.append_page(widget)
                result.set_tab_label(widget, self.gtk_new(gtk.Label, label=model_bind(model=itemview._model, twoway=False).label))

        return result
