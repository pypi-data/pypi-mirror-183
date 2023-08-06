#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import abc
import asyncio
import functools
import inspect
import threading
import time
import traceback
import typing as t

import klovve.type_loader
import klovve.view

if t.TYPE_CHECKING:
    import klovve.drivers


def create_app(view_spec: "klovve.view._TViewSpec", *,
               type_loader: t.Optional["klovve.type_loader.TypeLoader"] = None) -> "Application":
    type_loader = type_loader or klovve.type_loader.DefaultTypeLoader(())
    driver = type_loader.driver_type()()
    return ApplicationInternal(driver=driver, view_spec=view_spec, type_loader=type_loader)


class Application(abc.ABC):

    @abc.abstractmethod
    def start(self) -> None:
        pass

    @abc.abstractmethod
    async def sleep_until_stopped(self) -> None:
        pass


class ApplicationInternal(Application):

    running_apps = []

    __running_apps_changed_event = None

    @staticmethod
    def _running_apps_changed_event():
        if not ApplicationInternal.__running_apps_changed_event:
            ApplicationInternal.__running_apps_changed_event = asyncio.Event()
        return ApplicationInternal.__running_apps_changed_event

    def __init__(self, *, driver: "klovve.drivers.Driver", view_spec: "klovve.view._TViewSpec",
                 type_loader: "klovve.type_loader.TypeLoader"):
        self.__driver = driver
        self.__view_spec = view_spec
        self.__type_loader = type_loader

    async def sleep_until_stopped(self):
        while self in ApplicationInternal.running_apps:
            await ApplicationInternal._running_apps_changed_event().wait()
            ApplicationInternal._running_apps_changed_event().clear()

    async def start(self):
        ApplicationInternal.running_apps.append(self)
        view_factory = klovve.view.ViewFactory(self.__type_loader, self.__driver, TODO=self)
        window = self.__view_spec(view_factory).view()
        self._view = window  # TODO
        window.get_native_stuff()
        ww = window._ComposedView__result._model.item.view()
        self.__driver.show_window(ww)
        foo = True

        @klovve.reaction(owner=self)
        def _():
            nonlocal foo, ww
            if ww._model.is_closed and foo:
                foo = False
                ApplicationInternal.running_apps.remove(self)
                ApplicationInternal._running_apps_changed_event().set()
                ww = None  # TODO mem

    def run(self):
        mainloop = self.__driver.mainloop
        if mainloop is self.__running_loop():

            async def do():
                await self.start()
                await self.sleep_until_stopped()

            mainloop.create_task(do())
        else:

            async def do():
                await self.start()
                while len(ApplicationInternal.running_apps) > 0:
                    await ApplicationInternal._running_apps_changed_event().wait()
                    ApplicationInternal._running_apps_changed_event().clear()

            try:#TODO try/except weg
             mainloop.run_until_complete(do())
            except:
                traceback.print_exc()

    def __running_loop(self):
        try:
            return asyncio.get_running_loop()
        except RuntimeError:
            return None


def call_with_kwargs(func, **kwargs):  # TODO move and rename
    akwargs = {}
    tsig = inspect.signature(func)
    for pparam in tsig.parameters.values():
        if pparam.kind == inspect.Parameter.VAR_KEYWORD:
            akwargs = kwargs
            break
        elif pparam.kind in [inspect.Parameter.KEYWORD_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD]:
            akwargs[pparam.name] = kwargs[pparam.name]
    return func(**akwargs)


def call_with_kwargs_maybe_async(func, mainloop, **kwargs):
    result = call_with_kwargs(func, **kwargs)
    if inspect.isawaitable(result):
        return mainloop.create_task( result  )
    else:
        # TODO return a finished Future or alike
        return result


def in_mainloop(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        reslt = None

        def fuunc():
            nonlocal reslt
            reslt = [func(*args, **kwargs)]

        mainloop = klovve.drivers.Driver._mainloop  # TODO
        mainloop.call_soon_threadsafe(fuunc)

    return wrapper


def in_mainloop2(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        reslt = None

        def fuunc():
            nonlocal reslt
            reslt = [func(*args, **kwargs)]
        mainloop = klovve.drivers.Driver._mainloop  # TODO
        mainloop.call_soon_threadsafe(fuunc)

        while reslt is None:
            time.sleep(0.05) # TODO
        return reslt[0]

    return wrapper


class MainloopObjectProxy:

    def __init__(self, obj):
        self.__obj = obj

    def __getattr__(self, item):

        if threading.current_thread() == threading.main_thread():
            return getattr(self.__obj, item)

        def getter():
            re = getattr(self.__obj, item)

            if callable(re):
                def fdf(*args, **kwargs):
                    return in_mainloop2(lambda: re(*args, **kwargs))()
                return fdf

            return re
        return in_mainloop2(getter)()

    def __setattr__(self, key, value):
        if key == "_MainloopObjectProxy__obj":
            super().__setattr__(key, value)
        else:
            if threading.current_thread() == threading.main_thread():
                setattr(self.__obj, key, value)
            def goo():
                setattr(self.__obj, key, value)
            in_mainloop2(goo)()
