#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only

import json
import pathlib
import sys
import os
import tempfile
import uuid

# The following hack makes Kloove sample apps work even without proper package installation. Do not copy that line!
sys.path += (os.path.abspath(__file__ + up * "/..") for up in (2, 4))

import klovve


class Domain:
    """
    Just a foolish and simplified 'domain layer' of this sample app. You could have a completely different one.
    """

    class Thing:

        def __init__(self, name, *, comment=None, id=None):
            self.id = id or str(uuid.uuid4())
            self.name = name
            self.comment = comment

    def __init__(self, filepath):
        self.thing_added_handlers = []
        self.thing_modified_handlers = []
        self.thing_removed_handlers = []
        self.__things = {}
        self.__filepath = filepath
        self.__load()

    def get_thing_ids(self):
        return list(self.__things.keys())

    def get_thing_by_id(self, thing_id: str):
        return self.__things.get(thing_id)

    def add_thing(self, name):
        self.__ensure_name_not_already_in_use(name)
        new_thing = Domain.Thing(name)
        self.__things[new_thing.id] = new_thing
        self.__call_handlers(self.thing_added_handlers, new_thing.id)
        self.__store()

    def remove_thing(self, thing_id: str):
        self.__things.pop(thing_id)
        self.__call_handlers(self.thing_removed_handlers, thing_id)
        self.__store()

    def set_thing_name(self, thing_id: str, name: str):
        self.__ensure_name_not_already_in_use(name)
        thing = self.get_thing_by_id(thing_id)
        thing.name = name
        self.__call_handlers(self.thing_modified_handlers, thing_id)
        self.__store()

    def set_thing_comment(self, thing_id: str, comment: str):
        thing = self.get_thing_by_id(thing_id)
        thing.comment = comment
        self.__call_handlers(self.thing_modified_handlers, thing_id)
        self.__store()

    def __ensure_name_not_already_in_use(self, name: str):
        if any(map(lambda thing: thing.name == name, self.__things.values())):
            raise Exception(f"The name '{name}' is already in use.")

    def __load(self):
        if self.__filepath.exists():
            for thing in [Domain.Thing(**thing_data) for thing_data in json.loads(self.__filepath.read_text())]:
                self.__things[thing.id] = thing

    def __store(self):
        self.__filepath.write_text(json.dumps([thing.__dict__ for thing in self.__things.values()]))

    @staticmethod
    def __call_handlers(handlers, thing_id):
        for handler in handlers:
            handler(thing_id)


if __name__ == "__main__":
    import crud_app.pieces.app  # TODO
    domain = Domain(pathlib.Path(tempfile.gettempdir()) / "klovve_sample__crud_app__data")

    klovve.create_app(
        lambda view: view.crud_app.app(crud_app.pieces.app.Model(domain))
    ).run()
