#!/bin/python
# -*- coding: utf-8 -*-

import os
import pathlib
import subprocess
from enum import Enum, auto


this_module_path = os.path.dirname(__file__)
gdbinit_path = os.path.join(this_module_path, "gdbinit")
plugins_loader_path = os.path.join(this_module_path, "gdbplugins_loader.py")

dnf_gdbplugins_loader_dst = pathlib.Path("/etc/gdbinit.d/gdbplugins_loader.py")
dnf_gdbinit_dest = pathlib.Path("/etc/gdbinit")

apt_gdbplugins_loader_dst = pathlib.Path("/etc/gdb/gdbinit.d/gdbplugins_loader.py")
apt_gdbinit_dest = pathlib.Path("/etc/gdb/gdbinit")


class PackageManager(Enum):
    UNKNOWN = auto()
    APT = auto()
    DNF = auto()


pkg_mgr_cmdlines = {
    PackageManager.APT: ("apt-get", "install", "-y", "gdb"),
    PackageManager.DNF: ("dnf", "install", "-y", "gdb"),
}


def detect_package_manager_by_installing_gdb():
    for pm, cmdline in pkg_mgr_cmdlines.items():
        try:
            completed_process = subprocess.run(cmdline, check=False)
        except FileNotFoundError:
            # We don't have this package manager present in the system.
            pass
        else:
            if completed_process.returncode != 0:
                print("Couldn't install gdb. Trying another package manager.")
                continue
            else:
                return pm
    else:
        return PackageManager.UNKNOWN


def ynchoice(propmt: str):
    while True:
        answ = input(propmt).strip().lower()
        if answ.startswith("y"):
            return True
        elif answ.startswith("n"):
            return False


def replace(original: pathlib.Path, target: pathlib.Path):
    if ynchoice(f"Replace the {original} with the {target}? y/n: "):
        backuppath = pathlib.Path(f"{original}.backup")
        if backuppath.exists():
            print(
                "Cannot make a backup as there already "
                f"is a backup file {backuppath}. Skipping."
            )
            return
        if original.exists():
            original.rename(backuppath)
        pathlib.Path(original).symlink_to(target)


def dnf_distro_replaces():
    replace(dnf_gdbinit_dest, gdbinit_path)
    replace(dnf_gdbplugins_loader_dst, plugins_loader_path)


def apt_distro_replaces():
    replace(apt_gdbinit_dest, gdbinit_path)
    replace(apt_gdbplugins_loader_dst, plugins_loader_path)


def main():
    pkg_mgr = detect_package_manager_by_installing_gdb()
    print(pkg_mgr)
    CHOICES = {pkg_mgr.DNF: dnf_distro_replaces, pkg_mgr.APT: apt_distro_replaces}
    work = CHOICES.get(pkg_mgr, None)
    if not work:
        raise Exception("Couldn't detect package manager on this system.")
    work()

    print("Done.")
