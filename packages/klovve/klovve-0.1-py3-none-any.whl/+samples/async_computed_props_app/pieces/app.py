#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import asyncio
import datetime
import threading
import time

import klovve


class Model(klovve.Model):

    bar = klovve.Property(default=lambda: 0)

    @klovve.ComputedProperty(initially=lambda: 0.000001, use_last_value_during_recompute=False)
    async def foo(self):  # recompute once bar changes
        x = self.bar * 2
        y = await f1(x)
        # if bar has changed meanwhile, cancel here and start again
        z = await f2(y)
        # if bar has changed meanwhile, cancel here and start again
        return f3(x, y, z)

    @klovve.ComputedProperty(initially=lambda: -1, use_last_value_during_recompute=False)
    async def baz(self):  # recompute once foo or bar changes
        x = self.foo * 2
        y = await f1(x)
        # if foo has changed meanwhile, cancel here and start again
        z = await f2(self.bar)
        # if foo or bar has changed meanwhile, cancel here and start again
        return f3(x, y, z)

    def __init__(self):
        super().__init__()
        def uuf():
            self.bar += 1
        loop = asyncio.get_running_loop()
        def fuh():
            while True:
                time.sleep(1)
                loop.call_soon_threadsafe(uuf)
        threading.Thread(target=fuh, daemon=True).start()


class View(klovve.ComposedView):

    model: Model

    def get_composition(self, model, model_bind, pieces):

        # noinspection PyUnusedLocal
        def tuff(factor):
            return self.computed(lambda: model.baz * factor)

        def view_for_bar():
            if model.baz:
                text = pieces.label(text=self.computed(lambda: f"Baz '{model.baz}' (bar: {model.bar})"))
                # TODO ,tuff_fct=tuff)
            else:
                text = pieces.label(text=self.computed(lambda: f"Foo '{model.foo}' (bar: {model.bar})"))
            return pieces.vertical_box(items=[text])

        return pieces.window(
            body=pieces.vertical_box(
                items=[pieces.label(text=str(datetime.datetime.now())), pieces.placeholder(item=self.computed(view_for_bar))]
            ),
        )


async def f1(v):
    await asyncio.sleep(0.1)
    return v * 2


async def f2(v):
    await asyncio.sleep(0.1)
    return v * 2


def f3(v, w, x):
    return v * w * x
