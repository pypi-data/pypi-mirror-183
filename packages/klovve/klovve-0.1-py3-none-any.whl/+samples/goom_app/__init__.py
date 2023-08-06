#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only

import sys
import os

# The following hack makes Kloove sample apps work even without proper package installation. Do not copy that line!
sys.path += (os.path.abspath(__file__ + up * "/..") for up in (2, 4))

import klovve


if __name__ == "__main__":
    klovve.create_app(
        lambda view: view.goom_app.app()   # TODO window here or window in the .app ?! -> streamline
    ).run()
