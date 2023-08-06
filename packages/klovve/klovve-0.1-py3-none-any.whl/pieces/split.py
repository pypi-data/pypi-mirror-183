#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve


class Model(klovve.Model):

    item1 = klovve.Property(default=lambda: None)

    item2 = klovve.Property(default=lambda: None)


class View(klovve.BaseView):

    model: Model
