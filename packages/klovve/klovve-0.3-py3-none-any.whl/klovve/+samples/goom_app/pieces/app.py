#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import asyncio

import klovve


class Model(klovve.Model):

    counter = klovve.Property(default=lambda: 0)

    e = klovve.Property()

    @klovve.ComputedProperty
    def txt(self):
        return str(self.e)

    def __init__(self):
        super().__init__()

        @klovve.reaction(owner=self)
        async def afs():
            self.e = "good"
            await asyncio.sleep(2)
            self.e = self.counter

        self.__factor = 2

        def uuf():
            self.counter += 1
            asyncio.get_running_loop().call_later(4, uuf)
        uuf()


class View(klovve.ComposedView):

    def get_composition(self, model, model_bind, pieces):

        @klovve.reaction(owner=self, initially=lambda: "griff", use_last_value_during_recompute=False)
        async def foo():
            await asyncio.sleep(1)
            return self.model.txt

        @klovve.reaction(owner=self)
        def foo2():
            print(foo())

        return pieces.window(
            body=pieces.label(
                text=model_bind.txt
            ),
            title="goom",
        )
