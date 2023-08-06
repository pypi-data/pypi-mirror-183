#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only

import os
import sys

# The following hack makes Kloove tests work even without proper package installation. Do not copy that line!
import typing as t

import klovve.pieces.text
import klovve.pieces.placeholder
import klovve.pieces.horizontal_box

sys.path += (os.path.abspath(__file__ + up * "/..") for up in (1, 3))

import klovve.piece_loader


def test_simple_view():

    class Pieces:

        class MyPiece:  # production code would not implement pieces this 'embedded' way, but in separate files!

            class Model(klovve.Model):

                foo = klovve.ListProperty()

            class View(klovve.ComposedView):

                def get_composition(self, model, model_bind, pieces):
                    return pieces.horizontal_box(
                        items=[pieces.label(text=t) for t in self.model.foo]
                    )

    view = _get_view(Pieces, lambda view: view.MyPiece())
    foo = view.get_native_stuff()
    print(foo)
    print(view)


def _get_view(pieces, view_spec):
    """
    Internally used by the test only. You would not do that in production code.
    """

    class TestPieceLoader(klovve.piece_loader.DefaultPieceLoader):

        def __init__(self, driver, embedded_pieces):
            super().__init__(driver, ())
            self.__embedded_pieces = embedded_pieces

        def __embedded_piece(self, name_tuple, kind):
            return getattr(self.__embedded_pieces[tuple(name_tuple)[0]], kind)

        def view_base_type(self, name_tuple):
            return super().view_base_type(name_tuple) or self.__embedded_piece(name_tuple, "View")

        def view_type(self, name_tuple):
            return self.__embedded_piece(name_tuple, "View") or super().view_type(name_tuple)

        def model_type(self, name_tuple):
            return super().model_type(name_tuple) or self.__embedded_piece(name_tuple, "Model")

    class Pieces:

        class text:

            class View(klovve.pieces.label.View, klovve.BaseView):
                pass

        class placeholder:

            class View(klovve.pieces.placeholder.View, klovve.BaseView):
                pass

        class horizontal_box:

            class View(klovve.pieces.horizontal_box.View, klovve.BaseView):
                pass

    all_pieces = {**pieces.__dict__, **Pieces.__dict__}

    all_pieces2 = {}
    def opi(fff):
        raw_view_type, model_type = getattr(fff, "View", None), getattr(fff, "Model", None)
        if not raw_view_type:
            return fff
        class gro:

            class View(raw_view_type):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.actions = []

                def get_native_stuff(self):
                    return self.actions
        if model_type:
            gro.Model = model_type
        return gro
    for k, v in all_pieces.items():
        all_pieces2[k] = opi(v)

    class TestMainLoop(klovve.application.MainLoop):

        def run(self, view):
            pass

        def _invoke(self, func):
            pass

    class TestDriver(klovve.drivers.Driver):

        def view_type(self, name_tuple, additional_packages):
            return all_pieces2[tuple(name_tuple)[0]].View

        @staticmethod
        def name():
            return "test"

        def _create_mainloop(self):
            return TestMainLoop()

        @staticmethod
        def rank():
            return 1000000  # TODO

    driver = TestDriver()
    piece_loader = TestPieceLoader(driver, all_pieces2)
    app = klovve.create_app(view_spec, driver=driver, piece_loader=piece_loader)
    return app._view
