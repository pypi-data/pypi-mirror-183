# Originally sourced from pySerial. https://github.com/pyserial/pyserial
# (C) 2011-2015 Chris Liechti <cliechti@gmx.net>
# SPDX-License-Identifier:    BSD-3-Clause
from __future__ import annotations

import glob
import sys

from lsports._common import PortInfo, list_links

if sys.platform == "linux":  # Linux
    from lsports._linux import comports as comports

elif sys.platform == "darwin":  # OS X
    from lsports._osx import comports as comports

elif sys.platform == "cygwin":  # Cygwin/win32
    # cygwin accepts /dev/com* in many contexts
    # (such as 'open' call, explicit 'ls'), but 'glob.glob'
    # and bare 'ls' do not; so use /dev/ttyS* instead
    def comports(include_links: bool = False) -> list[PortInfo]:
        devices = set(glob.glob("/dev/ttyS*"))
        if include_links:
            devices.update(list_links(devices))
        return [PortInfo(d) for d in devices]

elif sys.platform.startswith("openbsd"):  # OpenBSD

    def comports(include_links: bool = False) -> list[PortInfo]:
        devices = set(glob.glob("/dev/cua*"))
        if include_links:
            devices.update(list_links(devices))
        return [PortInfo(d) for d in devices]

elif sys.platform.startswith(("bsd", "freebsd")):

    def comports(include_links: bool = False) -> list[PortInfo]:
        devices = set(glob.glob("/dev/cua*[!.init][!.lock]"))
        if include_links:
            devices.update(list_links(devices))
        return [PortInfo(d) for d in devices]

elif sys.platform.startswith("netbsd"):  # NetBSD

    def comports(include_links: bool = False) -> list[PortInfo]:
        devices = set(glob.glob("/dev/dty*"))
        if include_links:
            devices.update(list_links(devices))
        return [PortInfo(d) for d in devices]

elif sys.platform.startswith("irix"):  # IRIX

    def comports(include_links: bool = False) -> list[PortInfo]:
        devices = set(glob.glob("/dev/ttyf*"))
        if include_links:
            devices.update(list_links(devices))
        return [PortInfo(d) for d in devices]

elif sys.platform.startswith("hp"):  # HP-UX (not tested)

    def comports(include_links: bool = False) -> list[PortInfo]:
        devices = set(glob.glob("/dev/tty*p0"))
        if include_links:
            devices.update(list_links(devices))
        return [PortInfo(d) for d in devices]

elif sys.platform.startswith("sunos"):  # Solaris/SunOS

    def comports(include_links: bool = False) -> list[PortInfo]:
        devices = set(glob.glob("/dev/tty*c"))
        if include_links:
            devices.update(list_links(devices))
        return [PortInfo(d) for d in devices]

elif sys.platform.startswith("aix"):  # AIX

    def comports(include_links: bool = False) -> list[PortInfo]:
        devices = set(glob.glob("/dev/tty*"))
        if include_links:
            devices.update(list_links(devices))
        return [PortInfo(d) for d in devices]

else:
    raise ImportError(f"No implementation available for '{sys.platform}' platforms.")

comports.__doc__ = "Scan for available ports."
