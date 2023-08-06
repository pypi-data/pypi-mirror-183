#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.pieces.list
import asyncio
import klovve.pieces.button
import klovve.drivers.gtk.views.button
import klovve.drivers.gtk


class View(klovve.pieces.list.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        gtk = klovve.drivers.gtk.Gtk
        box = self.gtk_new(gtk.Box, orientation=gtk.Orientation.VERTICAL, hexpand=False)
        scrolled_window = self.gtk_new(gtk.ScrolledWindow, hexpand=True, vexpand=True, width_request=100,
                                       hscrollbar_policy=gtk.PolicyType.NEVER, propagate_natural_height=True)
        box.append(scrolled_window)
        listbox = self.gtk_new(gtk.ListBox, visible=True)
        scrolled_window.set_child(listbox)
        list_actions_panel = self.gtk_new(gtk.Box, orientation=gtk.Orientation.VERTICAL)
        box.append(list_actions_panel)

        def on_row_activated(_, row):
            x = None
            if row:
                idx = row.get_index()
                if idx >= 0:
                    x = idx
            model.selected_item = model.items[x] if (x is not None) else None

            if (x is not None) and model.item_actions:
                popover = gtk.Popover()
                menu_box = self.gtk_new(gtk.Box, orientation=gtk.Orientation.VERTICAL)
                popover.set_child(menu_box)
                def goo(ia):
                    def x(_):
                        popover.popdown()  # TODO noh destroy/remove instead
                        klovve.drivers.gtk.GLib.idle_add(
                            lambda: klovve.application.call_with_kwargs_maybe_async(
                                ia, asyncio.get_running_loop(),
                                context=klovve.drivers.gtk.views.button.Context(self._view_factory, box),
                                model=model,
                                model_bind=klovve.view.BindFactory(model),
                                pieces=self._view_factory  # TODO
                            ) and False  # TODO needed for idle_add
                        )
                    return x
                for item_action in model.item_actions:
                    btn = self.gtk_new(gtk.Button, label=item_action.text)
                    menu_box.append(btn)
                    btn.connect("clicked", goo(item_action.action))
                popover.insert_after(row, None)
                popover.popup()

        listbox.connect("row-activated", on_row_activated)

        _refs = [] #TODO

        @klovve.reaction(owner=box)
        def _handle_selected_item():
            if model.selected_item:
                try:
                    v = model.items.index(model.selected_item)
                except ValueError:
                    return  # TODO
                row = listbox.get_row_at_index(v)
            else:
                row = None
            listbox.select_row(row)

        @klovve.reaction(owner=box)
        def _handle_items():
            with klovve.data.deps.no_dependency_tracking():
                selected_item = model.selected_item
            for old_item in klovve.drivers.gtk.children(listbox):
                listbox.remove(old_item)
            item_label_func = (model.item_label_func or str)
            select_row = None
            _refs.clear()
            def bla(ll, itm):
                @klovve.reaction(owner=None)
                def flg():
                    vv = item_label_func(itm)
                    ll.props.label = vv
                return flg
            for i, item in enumerate(model.items):
                row = gtk.Label(xalign=0, visible=True)
                _refs.append(row)
                _refs.append(bla(row, item))
                listbox.append(row)
                if item == selected_item:
                    select_row = i
            listbox.select_row(None if (select_row is None) else listbox.get_row_at_index(select_row))
            if select_row is None:
                with klovve.data.deps.no_dependency_tracking():
                    on_row_activated(None, None)

        @klovve.reaction(owner=box)
        def _handle_list_actions():
            for old_item in klovve.drivers.gtk.children(list_actions_panel):
                list_actions_panel.remove(old_item)
            for list_action in model.list_actions:
                list_actions_panel.append(self._view_factory.button(list_action).view().get_native_stuff())
            for barzz in model.barz:
                list_actions_panel.append(barzz.view().get_native_stuff())

        return box
