# Originally sourced from pySerial. https://github.com/pyserial/pyserial
# (C) 2011-2015 Chris Liechti <cliechti@gmx.net>
# SPDX-License-Identifier:    BSD-3-Clause
from __future__ import annotations

import glob
import os

from lsports._common import PortInfo, list_links


def _readline(*args: str) -> str:
    with open(os.path.join(*args)) as f:
        return f.readline().strip()


def _readline_optional(*args: str) -> str | None:
    try:
        return _readline(*args)
    except OSError:
        return None


def sysfs_wrapper(device: str) -> PortInfo:
    """Wrapper for easy sysfs access and device info."""
    info = PortInfo(device)
    # Special handling for links
    if device is not None and os.path.islink(device):
        device = os.path.realpath(device)
        is_link = True
    else:
        is_link = False
    info.usb_device_path = None
    if os.path.exists(f"/sys/class/tty/{info.name}/device"):
        info.device_path = os.path.realpath(f"/sys/class/tty/{info.name}/device")
        info.subsystem = os.path.basename(
            os.path.realpath(os.path.join(info.device_path, "subsystem"))
        )
    else:
        info.device_path = None
        info.subsystem = None
    # Check device type
    if info.subsystem == "usb-serial":
        assert info.device_path is not None
        info.usb_interface_path = os.path.dirname(info.device_path)
    elif info.subsystem == "usb":
        info.usb_interface_path = info.device_path
    else:
        info.usb_interface_path = None
    # Fill-in info for USB devices
    if info.usb_interface_path is not None:
        info.usb_device_path = os.path.dirname(info.usb_interface_path)
        num_if = int(_readline_optional(info.usb_device_path, "bNumInterfaces") or "1")
        info.vid = int(_readline(info.usb_device_path, "idVendor"), 16)
        info.pid = int(_readline(info.usb_device_path, "idProduct"), 16)
        info.serial_number = _readline_optional(info.usb_device_path, "serial")
        info.location = os.path.basename(  # num_if > 1 for multi interface devices like FT4232
            info.usb_interface_path if num_if > 1 else info.usb_device_path
        )
        info.manufacturer = _readline_optional(info.usb_device_path, "manufacturer")
        info.product = _readline_optional(info.usb_device_path, "product")
        info.interface = _readline_optional(info.usb_interface_path, "interface")

    if info.subsystem in ("usb", "usb-serial"):
        info.apply_usb_info()
    elif info.subsystem == "pnp":  # PCI based devices
        info.description = info.name
        assert info.device_path is not None
        info.hwid = _readline(info.device_path, "id")
    elif info.subsystem == "amba":  # raspi
        info.description = info.name
        assert info.device_path is not None
        info.hwid = os.path.basename(info.device_path)

    if is_link:
        info.hwid += f" LINK={device}"
    return info


def comports(include_links: bool = False) -> list[PortInfo]:
    devices = set()
    # built-in serial ports
    devices.update(glob.glob("/dev/ttyS*"))
    # usb-serial with own driver
    devices.update(glob.glob("/dev/ttyUSB*"))
    # xr-usb-serial port exar (DELL Edge 3001)
    devices.update(glob.glob("/dev/ttyXRUSB*"))
    # usb-serial with CDC-ACM profile
    devices.update(glob.glob("/dev/ttyACM*"))
    # ARM internal port (raspi)
    devices.update(glob.glob("/dev/ttyAMA*"))
    # BT serial devices
    devices.update(glob.glob("/dev/rfcomm*"))
    # Advantech multi-port serial controllers
    devices.update(glob.glob("/dev/ttyAP*"))
    # https://www.kernel.org/doc/Documentation/usb/gadget_serial.txt
    devices.update(glob.glob("/dev/ttyGS*"))

    if include_links:
        devices.update(list_links(devices))
    # hide non-present internal serial ports
    return [info for info in (sysfs_wrapper(d) for d in devices) if info.subsystem != "platform"]
