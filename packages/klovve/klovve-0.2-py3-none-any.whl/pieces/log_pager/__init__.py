#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve


class Model(klovve.Model):

    entries = klovve.ListProperty()

    boff = klovve.Property() #TODO


class View(klovve.BaseView):

    model: Model
