#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import asyncio

import klovve


class Model(klovve.Model):

    counter = klovve.Property(default=lambda: 0)

    @klovve.ComputedProperty
    def a(self):
        return self.counter * self.__factor

    @klovve.ComputedProperty
    def b(self):
        return self.counter * self.__factor

    @klovve.ComputedProperty
    def c(self):
        return self.a * self.__factor

    @klovve.ComputedProperty
    def d(self):
        return self.b * self.__factor

    @klovve.ComputedProperty
    def e(self):
        return self.c + self.d

    @klovve.ComputedProperty
    def txt(self):
        return str(self.e)

    def __init__(self):
        super().__init__()
        import klovve.drivers.gtk as fritz
        self.__factor = 2

        def uuf():
            self.counter += 1
            asyncio.get_running_loop().call_later(4, uuf)
        uuf()


class View(klovve.ComposedView):

    def get_composition(self, model, model_bind, pieces):
        return pieces.window(
            body=pieces.label(
                text=model_bind.txt
            ),
            title="boom",
        )
