#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import asyncio
import klovve.drivers


class Driver(klovve.drivers.Driver):

    @staticmethod
    def rank():
        return 100_000

    @staticmethod
    def name():
        return "bare_terminal"

    def _create_mainloop(self):
        return asyncio.SelectorEventLoop()

    def show_window(self, window):
        self.__griche = window.get_native_stuff()
