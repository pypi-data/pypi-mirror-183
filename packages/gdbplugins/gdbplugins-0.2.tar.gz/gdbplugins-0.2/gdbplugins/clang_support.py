# -*- coding: utf-8 -*-
import gdb
from contextlib import contextmanager


class CFunc(object):
    def __init__(self):
        self.name = None
        self.func = None

    def __get__(self, instance, owner=None):
        if self.func is None:
            self.func = gdb.parse_and_eval(self.name)
        return self.func

    def __set_name__(self, owner, name):
        self.name = name


class CAPI(object):
    def __init__(self):
        for k in dir(self):
            # This will cause the CFunc result to get loded and cached.
            getattr(self, k)


class StdLib(CAPI):
    malloc = CFunc()
    free = CFunc()

    @classmethod
    @contextmanager
    def allocate_type(cls, the_type):
        ptr = cls.malloc(the_type.sizeof)
        yield ptr.cast(the_type.pointer())
        cls.free(ptr)
