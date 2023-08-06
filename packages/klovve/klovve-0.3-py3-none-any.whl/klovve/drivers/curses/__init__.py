#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import atexit
import os
import weakref
import selectors
import asyncio
import typing as t

import klovve
import klovve.debug
import klovve.drivers
import klovve.data.value_holder

import sys
sys.path.append( os.path.abspath(f"{__file__}/..") )#TODO

import viwid.loop
import viwid.drivers


TConverter = t.Callable[[t.Any], t.Any]


if not sys.stdin.isatty() or not sys.stdout.isatty():
    raise Exception("TODO")


class Driver(klovve.drivers.Driver):

    @staticmethod
    def rank():
        return 10_000

    @staticmethod
    def name():
        return "curses"

    def show_window(self, window):
        ody = window.get_native_stuff()

        #TODO
        ody.parent._children = []
        ody.set_parent(None)

#        self.__map22.original_widget = ody
        driver = viwid.drivers.get_driver()
        driver.add_widget_screen(ody)

        #  TODO  https://stackoverflow.com/questions/68716139/redirecting-current-runing-python-process-stdout
       # orig_stdout_fd = os.dup(1)
       # orig_stderr_fd = os.dup(2)
        devnull = open('/tmp/devnull', 'w')
#        devnull = open('/dev/null', 'w')
      #  os.dup2(devnull.fileno(), 1)
        os.dup2(devnull.fileno(), 2)


    def _create_mainloop(self):
        #
        driver = viwid.drivers.get_driver()
        driver.loop

        rloop = asyncio.new_event_loop()
        self.uloop = loop = driver.loop
        #rloop.run_until_complete(loop.run())
#        loop.run()
        #loop.screen.set_terminal_properties(colors=256)#TODO
        #loop.start()
        #atexit.register(lambda : loop.stop())#TODO
        # TODO
        ruc = rloop.run_until_complete
        async def asas(x):
            return await asyncio.gather(loop.run(), x)
        rloop.run_until_complete = lambda t: ruc(asas(t)) # ruc(t)
        return rloop


class View(klovve.BaseView):

    @staticmethod
    def bind(aobj, aprop_name, value: t.Any):
        if isinstance(value, klovve.data.value_holder.ValueHolder):
            View.__bind(aobj, aprop_name=aprop_name, value_holder=value)
        else:
            aobj.set_property(aprop_name, value)

    @staticmethod
    def __bind(aobj, *, aprop_name, value_holder: klovve.data.value_holder.ValueHolder):

        @klovve.reaction(owner=aobj)  # TODO or owner=obj?!
        def transfer():
            new_source_value = value_holder.get_value()
            setattr(aobj, aprop_name, new_source_value)
#            getattr(aobj, f"set_{aprop_name}")(new_source_value)
            #setattr(aobj, aprop_name, new_source_value)

        if value_holder.is_settable():
            def bar(_, __):
                value_holder.set_value(aobj.get_property(aprop_name))
            aobj.connect(f"notify::{aprop_name}", bar)

    @staticmethod
    def fizzwid_new(viewtype, **kwargs):  # TODO
        d1 = {}
        d2 = {}
        for k, v in kwargs.items():
            if isinstance(v, klovve.data.value_holder.ValueHolder): # TODO dedup *2?!
                d1[k] = v
            else:
                d2[k] = v
        widget = viewtype(**d2)
        klovve.debug.memory.new_object_created(widget, "Gtk.Widget")
        for k, v in d1.items():
            View.__bind(widget, aprop_name=k, value_holder=v)
        # TODO ?!
        #  widget._ref_sink()
        # widget._unref()
        return widget


def children(widget):
    result = []
    child = widget.get_first_child()
    while child:
        result.append(child)
        child = child.get_next_sibling()
    return result
