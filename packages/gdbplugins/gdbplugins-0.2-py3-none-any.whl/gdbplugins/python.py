# -*- coding: utf-8 -*-
import ast
import gdb
import subprocess
from contextlib import contextmanager
import argparse
from textwrap import dedent
from gdbplugins.clang_support import CAPI, CFunc


class Python(CAPI):
    PyGILState_Ensure = CFunc()
    PyGILState_Release = CFunc()
    PyObject_GetAttrString = CFunc()
    PyUnicode_FromString = CFunc()
    PyObject_CallFunctionObjArgs = CFunc()
    PyObject_CallFunction = CFunc()
    PyObject_CallMethod = CFunc()
    PyObject_CallMethodObjArgs = CFunc()
    PyImport_ImportModule = CFunc()
    PyRun_SimpleString = CFunc()
    Py_DecRef = CFunc()

    @classmethod
    @contextmanager
    def GIL(cls):
        gstate = cls.PyGILState_Ensure()
        yield
        cls.PyGILState_Release(gstate)


class StartDebugger(gdb.Command):
    def __init__(self, modname, command=None):
        self.modname = modname
        command = modname if not command else command
        super().__init__(command, gdb.COMMAND_NONE)

    def invoke(self, argument, from_tty):
        with Python.GIL():
            Python.PyRun_SimpleString(
                dedent(
                    f"""\
import {self.modname}
import sys
{self.modname}.set_trace(sys._getframe().f_back,
                         header="{self.modname} injected and tracing.")
"""
                )
            )


class StartPdb(gdb.Command):
    def __init__(self, modname, command=None):
        self.modname = modname
        command = modname if not command else command
        super().__init__(command, gdb.COMMAND_NONE)

    def invoke(self, argument, from_tty):
        parser = argparse.ArgumentParser(description=f"Spawn {self.modname}")
        parser.add_argument("--tty")
        parser.add_argument("--fback")
        args = parser.parse_args(gdb.string_to_argv(argument))

        tty = ""
        if args.tty == "reuse":
            tty = subprocess.check_output("tty").decode("utf8").strip()
            print(f"tty: {tty}")

        code = dedent(
            f"""\
            import {self.modname}
            import sys
            import os
            import traceback

            stdin = stdout = None
            if "{tty}":
                stdout = open("{tty}", 'w')
                stdin = open("{tty}", 'r')
            thepdb = {self.modname}.Pdb(stdin=stdin, stdout=stdout)

            if {args.fback}:
                frame = sys._getframe()
                traceback.print_stack(frame)
                thepdb.set_trace(frame.f_back)
            else:
                thepdb.set_trace()
            (lambda: None)()
        """
        )
        ast.parse(code)  # Check for code validity

        with Python.GIL():
            Python.PyRun_SimpleString(code)
        gdb.execute("c")


class PythonEval(gdb.Command):
    def __init__(self):
        super().__init__("python_eval", gdb.COMMAND_NONE)

    def invoke(self, argument, from_tty):
        with Python.GIL():
            Python.PyRun_SimpleString(argument)


def main():
    PythonEval()

    StartDebugger("pdb", "justpdb")
    StartDebugger("ipdb", "justipdb")
    StartPdb("pdb", "pdb")
