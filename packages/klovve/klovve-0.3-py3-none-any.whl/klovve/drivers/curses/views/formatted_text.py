#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.curses
import klovve.pieces.formatted_text
import xml.etree.ElementTree

import viwid.widgets.label


class View(klovve.pieces.formatted_text.View, klovve.drivers.curses.View):

    def get_native(self, model, model_bind):  # TODO scrolling?!
        label = viwid.widgets.label.Label()

        @klovve.reaction(owner=label)
        def tx():
            if model.text:
                x = xml.etree.ElementTree.fromstring(f"<x>{model.text}</x>")
                text = ""
                ul = 0
                def ca(ele):
                    nonlocal text, ul
                    if ele.tag == "br":
                        text += "\n"
                    if ele.tag == "h1":
                        text += "\n"
                    if ele.tag == "ul":
                        ul += 1
                        text += "\n\n"
                    if ele.tag == "li":
                        text += "- "
                    text += ele.text or ""
                    for child in ele:
                        ca(child)
                    if ele.tag == "ul":
                        ul -= 1
                        text += "\n"
                    if ele.tag == "h1":
                        text += "\n\n"
                    if ele.tag == "li":
                        text += "\n"
                    text += ele.tail or ""
                ca(x)
                label.text = text
            else:
                label.text = ""

        return label
