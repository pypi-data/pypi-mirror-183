#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve


class Model(klovve.Model):

    answer = klovve.Property()

    is_answered = klovve.Property()

    def set_answer(self, answer):
        self.answer = answer
        self.is_answered = True
        # TODO
        #       klovve.data.update_simultaneously((self.answer, answer),
        #                                        (self.is_answered, True))
