# Originally sourced from pySerial. https://github.com/pyserial/pyserial
# (C) 2011-2015 Chris Liechti <cliechti@gmx.net>
# SPDX-License-Identifier:    BSD-3-Clause
from __future__ import annotations

import glob
import os
import re
from collections.abc import Container


def _numsplit(text: str) -> list[str | int]:
    """Convert string into a list of texts and numbers in order to support a natural sorting."""
    result = []
    for group in re.split(r"(\d+)", text):
        if group:
            try:
                group = int(group)
            except ValueError:
                pass
            result.append(group)
    return result


class PortInfo:
    """Serial port information.

    General attributes:
        - device (str): device name, e.g. /dev/ttyUSB0
        - name (str): device base name, e.g. ttyUSB0
        - description (str): human readable description of the device
        - hwid (str): hardware ID, e.g. VID:PID=0403:6001 SER=123456 LOCATION=1-1.2

    USB specific attributes:
        - vid (int or None): USB vendor ID
        - pid (int or None): USB product ID
        - serial_number (str or None): USB serial number
        - location (str or None): USB location
        - manufacturer (str or None): USB manufacturer
        - product (str or None): USB product name (Bus Reported Device Description on Windows)
        - interface (str or None): USB interface name

    Linux specific attributes (SysFS):
        - usb_device_path (str or None): USB device path
        - device_path (str or None): device path
        - subsystem (str or None): device subsystem
        - usb_interface_path (str or None): USB interface path
    """

    def __init__(self, device: str, skip_link_detection: bool = False) -> None:
        self.device = device
        self.name = os.path.basename(device)
        self.description = "n/a"
        self.hwid = "n/a"
        # USB specific data
        self.vid: int | None = None
        self.pid: int | None = None
        self.serial_number: str | None = None
        self.location: str | None = None
        self.manufacturer: str | None = None
        self.product: str | None = None
        self.interface: str | None = None
        # Linux specific data
        self.usb_device_path: str | None = None
        self.device_path: str | None = None
        self.subsystem: str | None = None
        self.usb_interface_path: str | None = None
        # Special handling for links
        if not skip_link_detection and device is not None and os.path.islink(device):
            self.hwid = f"LINK={os.path.realpath(device)}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.device!r})"

    def __str__(self) -> str:
        return f"{self.device} - {self.description}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PortInfo):
            return NotImplemented
        return self.device == other.device

    def __hash__(self) -> int:
        return hash(self.device)

    def __lt__(self, other: PortInfo) -> bool:
        if not isinstance(other, PortInfo):
            return NotImplemented
        return _numsplit(self.device) < _numsplit(other.device)

    def usb_description(self) -> str:
        """A short string to name the port based on USB info."""
        if self.interface is not None:
            return f"{self.product} - {self.interface}"
        elif self.product is not None:
            return self.product
        else:
            return self.name

    def usb_info(self) -> str:
        """A string with USB related information about device."""
        vid = self.vid or 0
        pid = self.pid or 0
        ser = f" SER={self.serial_number}" if self.serial_number else ""
        loc = f" LOCATION={self.location}" if self.location else ""
        return f"USB VID:PID={vid:04X}:{pid:04X}{ser}{loc}"

    def apply_usb_info(self) -> None:
        """Update description and hwid from USB data."""
        self.description = self.usb_description()
        self.hwid = self.usb_info()


def list_links(devices: Container[str]) -> list[str]:
    """Search all /dev devices and look for symlinks to known ports already listed in devices."""
    links: list[str] = []
    for device in glob.glob("/dev/*"):
        if os.path.islink(device) and os.path.realpath(device) in devices:
            links.append(device)
    return links
