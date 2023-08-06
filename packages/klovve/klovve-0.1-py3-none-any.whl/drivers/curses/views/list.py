#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import asyncio
import klovve.pieces.list
import klovve.pieces.button
import klovve.drivers.curses.views.button
import klovve.drivers.curses

import viwid.widgets.button
import viwid.widgets.box
import viwid.widgets.list
import viwid.widgets.scrollable
import viwid.screen


class View(klovve.pieces.list.View, klovve.drivers.curses.View):

    def get_native(self, model, model_bind):
        listbox =  viwid.widgets.list.List(vertical_expand_greedily=True, horizontal_expand_greedily=True)
        list_actions_panel = viwid.widgets.box.Box(orientation=viwid.widgets.box.Orientation.VERTICAL)
        box = viwid.widgets.box.Box(
            orientation=viwid.widgets.box.Orientation.VERTICAL,
            children=[viwid.widgets.scrollable.Scrollable(item=listbox), list_actions_panel]
        )

        _refs = [] # TODO

        def on_selected_item_index_changed():
            x = listbox.selected_item_index
            model.selected_item = model.items[x] if (x is not None) else None
            if (x is not None) and model.item_actions:
                actions_box = viwid.widgets.box.Box(orientation=viwid.widgets.box.Orientation.VERTICAL)

                def goo(ia):
                    def x():
                        nonlocal podo
                        podo()
                        asyncio.get_running_loop().call_soon(
                            lambda: klovve.application.call_with_kwargs_maybe_async(
                                ia, asyncio.get_running_loop(),
                                context=klovve.drivers.curses.views.button.Context(self._view_factory, box),
                                model=model,
                                model_bind=klovve.view.BindFactory(model),
                                pieces=self._view_factory  # TODO
                            )
                        )

                    return x

                chlds = []  # TODO just .append instead?!
                for item_action in model.item_actions:
                    btn = viwid.widgets.button.Button(text=item_action.text)
                    chlds.append(btn)
                    btn.on_click.append(goo(item_action.action))
                actions_box.children = chlds
                podo = box.screen.popup(actions_box, alignment=viwid.screen.RootAlignment(
                    viwid.screen.AnchorRootAlignmentPositioning(listbox),
                    viwid.screen.AnchorRootAlignmentPositioning(listbox),
                    viwid.screen.AutoRootAlignmentSizing(),
                    viwid.screen.AutoRootAlignmentSizing()
                ))

        listbox.on_selection_activated.append(on_selected_item_index_changed)

        @klovve.reaction(owner=box)
        def _handle_items():
            with klovve.data.deps.no_dependency_tracking():
                selected_item = model.selected_item
            item_label_func = (model.item_label_func or str)
            select_row = None
            _refs.clear()
            def bla(ll, itm):
                @klovve.reaction(owner=None)
                def flg():
                    vv = item_label_func(itm)
                    ll.text = vv
                return flg
            itms = []
            for i, item in enumerate(model.items):
                row = viwid.widgets.list.ListRow()
                #row.on_click.append(mkon_row_activated2(i))
                _refs.append(row)
                _refs.append(bla(row, item))
                itms.append(row)
                if item == selected_item:
                    select_row = i
            listbox.items = itms

        @klovve.reaction(owner=box)
        def _handle_list_actions():
            children = []
            for list_action in model.list_actions:
                children.append(self._view_factory.button(list_action).view().get_native_stuff())
            for barzz in model.barz:
                children.append(barzz.view().get_native_stuff())
            list_actions_panel.children = children

        return box
