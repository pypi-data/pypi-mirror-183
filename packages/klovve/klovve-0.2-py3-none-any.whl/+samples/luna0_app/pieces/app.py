#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
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
        import klovve.drivers.gtk as fritz

        def uuf():
            self.counter += 1
            return True
        fritz.TODO.enqueue_asap(uuf)


class View(klovve.ComposedView):

    def get_composition(self, view):
        
        return pieces.window(
            body=pieces.horizontal_box(
                items=[pieces.label(text=digit) for digit in self.model.bam]
            ),
            title=self.computed(lambda: f"Counter: ~{self.model.counter_k}k"),
        )
