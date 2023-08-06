#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve


class Model(klovve.Model):

    entries = klovve.ListProperty()

    message = klovve.Property(default=lambda: "")

    began_at = klovve.Property()

    ended_at = klovve.Property()

    only_single_time = klovve.Property(default=lambda: False)

    only_verbose = klovve.Property(default=lambda: False)


class View(klovve.BaseView):

    model: Model
