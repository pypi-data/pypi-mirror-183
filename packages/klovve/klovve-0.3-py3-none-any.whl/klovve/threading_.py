#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import threading


def verify_correct_thread():
    if threading.current_thread() != threading.main_thread():
        raise ThreadingError("Access to klovve models is not allowed from this thread.")


class ThreadingError(Exception):
    pass
