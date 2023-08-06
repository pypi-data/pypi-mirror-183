#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import asyncio
import weakref

import klovve


class Model(klovve.Model):

    counter = klovve.Property(default=lambda: 0)

    @klovve.ComputedProperty  # TODO klovve.List())
    def bam(self):
        return [chr(0x1F311 + int(digit)) for digit in oct(self.counter)[2:]]

    @klovve.ComputedProperty
    def counter_k(self):
        return int(self.counter / 1000)

    def __init__(self):
        super().__init__()

        wself = weakref.ref(self)
        def uuf():
            self = wself()
            if self:
                self.counter += 1
                asyncio.get_running_loop().call_later(0.01 * 100, uuf)


                if self.counter % 30 == -30:
                    import guppy,code
                    hp = guppy.hpy()
                    code.interact(local=locals())

        uuf()


class View(klovve.ComposedView):

    def get_composition(self, model, model_bind, pieces):
        return pieces.window(
            body=pieces.vertical_box(
                items=[
                    pieces.button(
                        text="open new window",
                        action=lambda context: klovve.create_app(lambda view: view.multi_app.app()).run(),
                    ),
                    pieces.horizontal_box(
                        items=self.computed(lambda: [pieces.label(text=digit) for digit in self.model.bam])
                    )
                ]
            ),
            title=self.computed(lambda: f"Counter: ~{self.model.counter_k}k"),
        )
