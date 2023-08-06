# -*- coding: utf-8 -*-
import gdb
from gdbplugins.clang_support import CAPI, CFunc, StdLib


class Ruby(CAPI):
    rb_eval_string = CFunc()
    rb_eval_string_protect = CFunc()


class RubyEval(gdb.Command):
    def __init__(self):
        super().__init__("ruby_eval", gdb.COMMAND_NONE)

    def invoke(self, argument, from_tty):
        Ruby.rb_eval_string(argument)


def run_ruby_string_protect(ruby):
    int_t = gdb.lookup_type("int")
    with StdLib.allocate_type(int_t) as state_p:
        r = Ruby.rb_eval_string_protect(ruby, state_p)
        state = state_p.referenced_value()
    return r, state


class RubyEvalProtect(gdb.Command):
    def __init__(self):
        super().__init__("ruby_eval_protect", gdb.COMMAND_NONE)

    def invoke(self, argument, from_tty):
        r, state = run_ruby_string_protect(argument)
        print(f"Result: {r}, state {state}")


class Pry(gdb.Command):
    def __init__(self):
        super().__init__("pry", gdb.COMMAND_NONE)

    def invoke(self, argument, from_tty):
        print("Executing pry in the inferior")
        r, state = run_ruby_string_protect("""require 'pry'; pry""")
        print(f"Result: {r}, state {state}")


def main():
    RubyEval()
    RubyEvalProtect()
    Pry()
