#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

if sys.version_info < (3, 10):
    from importlib_metadata import entry_points
else:
    from importlib.metadata import entry_points


def load_plugins():
    print("Loading gdb python plugins")

    discovered_plugins = entry_points(group="gdbplugins.plugins")

    for name, _ in discovered_plugins:
        plugin_entry_point = discovered_plugins[name].load()
        plugin_entry_point()
        print("plugin {} loaded".format(name))


def main():
    load_plugins()


if __name__ == "__main__":
    main()
