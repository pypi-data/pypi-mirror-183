# Originally sourced from pySerial. https://github.com/pyserial/pyserial
# (C) 2011-2015 Chris Liechti <cliechti@gmx.net>
# SPDX-License-Identifier:    BSD-3-Clause
from __future__ import annotations

import sys

assert sys.platform == "win32", "This module is only for Windows."

import ctypes
import re
from collections.abc import Generator
from ctypes import GetLastError, WinError, byref, create_unicode_buffer, sizeof
from ctypes.wintypes import (
    BOOL,
    DWORD,
    HKEY,
    HWND,
    LONG,
    LPDWORD,
    PDWORD,
    PULONG,
    ULONG,
    WORD,
    WPARAM,
)
from winreg import KEY_READ, REG_DWORD

from lsports._common import PortInfo

HDEVINFO = ctypes.c_void_p
LPCTSTR = ctypes.c_wchar_p
PCTSTR = ctypes.c_wchar_p
PTSTR = ctypes.c_wchar_p
LPBYTE = PBYTE = ctypes.c_void_p
UBYTE = ctypes.c_ubyte
ULONG_PTR = WPARAM

ACCESS_MASK = DWORD
REGSAM = ACCESS_MASK

# fmt: off
DIGCF_DEFAULT               = 0x00000001
DIGCF_PRESENT               = 0x00000002
DIGCF_ALLCLASSES            = 0x00000004
DIGCF_PROFILE               = 0x00000008
DIGCF_DEVICEINTERFACE       = 0x00000010

ERROR_INVALID_DATA          = 0x0000000D
ERROR_INSUFFICIENT_BUFFER   = 0x0000007A
ERROR_NOT_FOUND             = 0x00000490

SPDRP_DEVICEDESC            = 0x00000000
SPDRP_HARDWAREID            = 0x00000001
SPDRP_CLASS                 = 0x00000007
SPDRP_MFG                   = 0x0000000B
SPDRP_FRIENDLYNAME          = 0x0000000C
SPDRP_CAPABILITIES          = 0x0000000F
SPDRP_BUSNUMBER             = 0x00000015
SPDRP_DEVTYPE               = 0x00000019
SPDRP_EXCLUSIVE             = 0x0000001A
SPDRP_CHARACTERISTICS       = 0x0000001B
SPDRP_ADDRESS               = 0x0000001C
SPDRP_UI_NUMBER_DESC_FORMAT = 0x0000001D
SPDRP_INSTALL_STATE         = 0x00000022
SPDRP_LOCATION_PATHS        = 0x00000023

INVALID_HANDLE_VALUE        = 0x00000000
DICS_FLAG_GLOBAL            = 0x00000001
DIREG_DEV                   = 0x00000001
# fmt: on

MAX_USB_DEVICE_TREE_TRAVERSAL_DEPTH = 5
USB_HW_ID_PAT = re.compile(r"VID_([0-9a-f]{4})(&PID_([0-9a-f]{4}))?(&MI_(\d{2}))?(\\(.*))?", re.I)


# https://learn.microsoft.com/en-us/windows/win32/api/guiddef/ns-guiddef-guid
class GUID(ctypes.Structure):
    _fields_ = [
        # Data1: Specifies the first 8 hexadecimal digits of the GUID.
        ("Data1", DWORD),
        # Data2: Specifies the first group of 4 hexadecimal digits.
        ("Data2", WORD),
        # Data3: Specifies the second group of 4 hexadecimal digits.
        ("Data3", WORD),
        # Data4: Array of 8 bytes. The first 2 bytes contain the third group of 4 hexadecimal
        # digits. The remaining 6 bytes contain the final 12 hexadecimal digits.
        ("Data4", UBYTE * 8),
    ]

    def __str__(self) -> str:
        return (
            f"{{{self.Data1:08x}-{self.Data2:04x}-{self.Data3:04x}-"
            f"{bytes(self.Data4[:2]).hex()}-{bytes(self.Data4[2:]).hex()}}}"
        )


PGUID = ctypes.POINTER(GUID)


# https://learn.microsoft.com/en-us/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data
class SP_DEVINFO_DATA(ctypes.Structure):
    _fields_ = [
        # cbSize: The size, in bytes, of the SP_DEVINFO_DATA structure.
        ("cbSize", DWORD),
        # ClassGuid: The GUID of the device's setup class.
        ("ClassGuid", GUID),
        # DevInst: An opaque handle to the device instance (also known as a handle to the devnode).
        # Some functions, such as SetupDiXxx functions, take the whole SP_DEVINFO_DATA structure as
        # input to identify a device in a device information set. Other functions, such as CM_Xxx
        # functions like CM_Get_DevNode_Status, take this DevInst handle as input.
        ("DevInst", DWORD),
        # Reserved: For internal use only.
        ("Reserved", ULONG_PTR),
    ]

    def __str__(self) -> str:
        return f"ClassGuid:{self.ClassGuid} DevInst:{self.DevInst}"


PSP_DEVINFO_DATA = ctypes.POINTER(SP_DEVINFO_DATA)


# https://learn.microsoft.com/en-us/windows-hardware/drivers/install/property-keys
class SP_DEVPROPKEY(ctypes.Structure):
    _fields_ = [
        # fmtid: A DEVPROPGUID-typed value that specifies a property category.
        ("fmtid", GUID),
        # pid: A DEVPROPID-typed value that uniquely identifies the property within the property
        # category. For internal system reasons, a property identifier must be greater than or
        # equal to two.
        ("pid", ULONG),
    ]

    def __str__(self) -> str:
        return f"fmtid:{self.fmtid} pid:{self.pid}"


# https://learn.microsoft.com/en-us/windows-hardware/drivers/install/devpkey-device-busreporteddevicedesc
DEVPKEY_Device_BusReportedDeviceDesc = SP_DEVPROPKEY(
    # https://learn.microsoft.com/en-us/windows/win32/properties/devices-bumper
    # https://www.magnumdb.com/search?q=DEVPKEY_Device_BusReportedDeviceDesc
    # Get the GUID with `SetupDiClassGuidsFromName("CDROM", ...)`
    GUID(
        0x540B947E,
        0x8B40,
        0x45BC,
        (0xA8, 0xA2, 0x6A, 0x0B, 0x89, 0x4C, 0xBD, 0xA2),
    ),
    REG_DWORD,
)

PSP_DEVPROPKEY = ctypes.POINTER(SP_DEVPROPKEY)

PSP_DEVICE_INTERFACE_DETAIL_DATA = ctypes.c_void_p

setupapi = ctypes.windll.LoadLibrary("setupapi")
SetupDiDestroyDeviceInfoList = setupapi.SetupDiDestroyDeviceInfoList
SetupDiDestroyDeviceInfoList.argtypes = (HDEVINFO,)
SetupDiDestroyDeviceInfoList.restype = BOOL

SetupDiClassGuidsFromName = setupapi.SetupDiClassGuidsFromNameW
SetupDiClassGuidsFromName.argtypes = (PCTSTR, PGUID, DWORD, PDWORD)
SetupDiClassGuidsFromName.restype = BOOL

SetupDiEnumDeviceInfo = setupapi.SetupDiEnumDeviceInfo
SetupDiEnumDeviceInfo.argtypes = (HDEVINFO, DWORD, PSP_DEVINFO_DATA)
SetupDiEnumDeviceInfo.restype = BOOL

SetupDiGetClassDevs = setupapi.SetupDiGetClassDevsW
SetupDiGetClassDevs.argtypes = (PGUID, PCTSTR, HWND, DWORD)
SetupDiGetClassDevs.restype = HDEVINFO

SetupDiGetDeviceRegistryProperty = setupapi.SetupDiGetDeviceRegistryPropertyW
SetupDiGetDeviceRegistryProperty.argtypes = (
    HDEVINFO,
    PSP_DEVINFO_DATA,
    DWORD,
    PDWORD,
    PBYTE,
    DWORD,
    PDWORD,
)
SetupDiGetDeviceRegistryProperty.restype = BOOL

# https://learn.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw
SetupDiGetDeviceProperty = setupapi.SetupDiGetDevicePropertyW
SetupDiGetDeviceProperty.argtypes = (
    HDEVINFO,
    PSP_DEVINFO_DATA,
    PSP_DEVPROPKEY,
    PULONG,
    PBYTE,
    DWORD,
    PDWORD,
    DWORD,
)
SetupDiGetDeviceProperty.restype = BOOL

SetupDiGetDeviceInstanceId = setupapi.SetupDiGetDeviceInstanceIdW
SetupDiGetDeviceInstanceId.argtypes = (HDEVINFO, PSP_DEVINFO_DATA, PTSTR, DWORD, PDWORD)
SetupDiGetDeviceInstanceId.restype = BOOL

SetupDiOpenDevRegKey = setupapi.SetupDiOpenDevRegKey
SetupDiOpenDevRegKey.argtypes = (HDEVINFO, PSP_DEVINFO_DATA, DWORD, DWORD, DWORD, REGSAM)
SetupDiOpenDevRegKey.restype = HKEY

advapi32 = ctypes.windll.LoadLibrary("Advapi32")
RegCloseKey = advapi32.RegCloseKey
RegCloseKey.argtypes = (HKEY,)
RegCloseKey.restype = LONG

RegQueryValueEx = advapi32.RegQueryValueExW
RegQueryValueEx.argtypes = (HKEY, LPCTSTR, LPDWORD, LPDWORD, LPBYTE, LPDWORD)
RegQueryValueEx.restype = LONG

cfgmgr32 = ctypes.windll.LoadLibrary("Cfgmgr32")
CM_Get_Parent = cfgmgr32.CM_Get_Parent
CM_Get_Parent.argtypes = (PDWORD, DWORD, ULONG)
CM_Get_Parent.restype = LONG

CM_Get_Device_IDW = cfgmgr32.CM_Get_Device_IDW
CM_Get_Device_IDW.argtypes = (DWORD, PTSTR, ULONG, ULONG)
CM_Get_Device_IDW.restype = LONG

CM_MapCrToWin32Err = cfgmgr32.CM_MapCrToWin32Err
CM_MapCrToWin32Err.argtypes = (DWORD, DWORD)
CM_MapCrToWin32Err.restype = DWORD


def get_parent_serial_number(
    child_devinst: ctypes._CData,
    child_vid: int | None,
    child_pid: int | None,
    depth: int = 0,
    last_serial_number: str | None = None,
) -> str:
    """Get the serial number of the parent of a device.

    Args:
        child_devinst:
            The device instance handle to get the parent serial number of.
        child_vid:
            The vendor ID of the child device.
        child_pid:
            The product ID of the child device.
        depth:
            The current iteration depth of the USB device tree.
    """
    # If the traversal depth is beyond the max, abandon attempting to find the serial number.
    if depth > MAX_USB_DEVICE_TREE_TRAVERSAL_DEPTH:
        return last_serial_number or ""

    # Get the parent device instance.
    devinst = DWORD()
    ret = CM_Get_Parent(byref(devinst), child_devinst, 0)

    if ret:
        win_error = CM_MapCrToWin32Err(DWORD(ret), DWORD(0))
        # If no parent available, the child was the root device. We cannot traverse further.
        if win_error == ERROR_NOT_FOUND:
            return last_serial_number or ""
        raise WinError(win_error)

    # Get the ID of the parent device and parse it for vendor ID, product ID, and serial number.
    parentHardwareID = create_unicode_buffer(250)
    ret = CM_Get_Device_IDW(devinst, parentHardwareID, sizeof(parentHardwareID) - 1, 0)
    if ret:
        raise WinError(CM_MapCrToWin32Err(DWORD(ret), DWORD(0)))
    parentHardwareID_str = parentHardwareID.value
    m = USB_HW_ID_PAT.search(parentHardwareID_str)
    # Return early if we have no matches (likely malformed serial, traversed too far)
    if not m:
        return last_serial_number or ""

    vid = None
    pid = None
    serial_number = None
    if m.group(1):
        vid = int(m.group(1), 16)
    if m.group(3):
        pid = int(m.group(3), 16)
    if m.group(7):
        serial_number = m.group(7)
    # Store what we found as a fallback for malformed serial values up the chain
    found_serial_number = serial_number

    # Check that the USB serial number only contains alphanumeric characters. It may be a windows
    # device ID (ephemeral ID).
    if serial_number and not re.match(r"^\w+$", serial_number):
        serial_number = None

    if not vid or not pid:
        # If PID and VID are not available at this device level, continue to the parent.
        return get_parent_serial_number(
            devinst, child_vid, child_pid, depth + 1, found_serial_number
        )

    if pid != child_pid or vid != child_vid:
        # If the VID or PID has changed, we are no longer looking at the same physical device. The
        # serial number is unknown.
        return last_serial_number or ""

    # In this case, the VID and PID of the parent device are identical to the child. However, if
    # there still isn't a serial number available, continue to the next parent.
    if not serial_number:
        return get_parent_serial_number(
            devinst, child_vid, child_pid, depth + 1, found_serial_number
        )

    # Finally, the VID and PID are identical to the child and a serial number is present, return it.
    return serial_number


def iterate_comports() -> Generator[PortInfo, None, None]:
    """A generator that yields descriptions for serial ports."""
    PortsGUIDs = (GUID * 8)()  # so far only seen one used, so hope 8 are enough...
    ports_guids_size = DWORD()
    if not SetupDiClassGuidsFromName(
        "Ports", PortsGUIDs, sizeof(PortsGUIDs), byref(ports_guids_size)
    ):
        raise WinError()

    ModemGUIDs = (GUID * 8)()  # so far only seen one used, so hope 8 are enough...
    modem_guids_size = DWORD()
    if not SetupDiClassGuidsFromName(
        "Modem", ModemGUIDs, sizeof(ModemGUIDs), byref(modem_guids_size)
    ):
        raise WinError()

    GUIDs = PortsGUIDs[: ports_guids_size.value] + ModemGUIDs[: modem_guids_size.value]

    # Repeat for all possible GUIDs
    for guid in GUIDs:
        bInterfaceNumber = None
        g_hdi = SetupDiGetClassDevs(byref(guid), None, None, DIGCF_PRESENT)
        if g_hdi == INVALID_HANDLE_VALUE:
            raise WinError()

        devinfo = SP_DEVINFO_DATA()
        devinfo.cbSize = sizeof(devinfo)
        index = 0
        while SetupDiEnumDeviceInfo(g_hdi, index, byref(devinfo)):
            index += 1

            # Get the real com port name
            hkey = SetupDiOpenDevRegKey(
                g_hdi,
                byref(devinfo),
                DICS_FLAG_GLOBAL,
                0,
                DIREG_DEV,  # DIREG_DRV for SW info
                KEY_READ,
            )
            port_name_buffer = create_unicode_buffer(250)
            port_name_length = ULONG(sizeof(port_name_buffer))
            RegQueryValueEx(
                hkey, "PortName", None, None, byref(port_name_buffer), byref(port_name_length)
            )
            RegCloseKey(hkey)
            port_name: str = port_name_buffer.value

            # Unfortunately this method also include parallel ports. We could check for names
            # starting with COM or just exclude LPT and hope that other "unknown" names are serial
            # ports...
            if port_name.startswith("LPT"):
                continue

            # Hardware ID
            szHardwareID = create_unicode_buffer(250)
            # Try to get ID that includes serial number
            if not SetupDiGetDeviceInstanceId(
                g_hdi, byref(devinfo), szHardwareID, sizeof(szHardwareID) - 1, None
            ):
                # Fall back to more generic hardware ID if that would fail
                if not SetupDiGetDeviceRegistryProperty(
                    g_hdi,
                    byref(devinfo),
                    SPDRP_HARDWAREID,
                    None,
                    byref(szHardwareID),
                    sizeof(szHardwareID) - 1,
                    None,
                ):
                    # Ignore ERROR_INSUFFICIENT_BUFFER
                    if GetLastError() != ERROR_INSUFFICIENT_BUFFER:
                        raise WinError()
            szHardwareID_str: str = szHardwareID.value

            info = PortInfo(port_name, skip_link_detection=True)

            # In case of USB, make a more readable string, similar to that on other platforms
            if szHardwareID_str.startswith("USB"):
                m = USB_HW_ID_PAT.search(szHardwareID_str)
                if m:
                    info.vid = int(m.group(1), 16)
                    if m.group(3):
                        info.pid = int(m.group(3), 16)
                    if m.group(5):
                        bInterfaceNumber = int(m.group(5))

                    ser_num = m.group(7)
                    # Check that the USB serial number only contains alphanumeric characters. It
                    # may be a windows device ID (ephemeral ID) for composite devices.
                    if not (ser_num and re.match(r"^\w+$", ser_num)):
                        ser_num = get_parent_serial_number(devinfo.DevInst, info.vid, info.pid)
                    info.serial_number = ser_num

                # Calculate a location string
                loc_path_str = create_unicode_buffer(500)
                if SetupDiGetDeviceRegistryProperty(
                    g_hdi,
                    byref(devinfo),
                    SPDRP_LOCATION_PATHS,
                    None,
                    byref(loc_path_str),
                    sizeof(loc_path_str) - 1,
                    None,
                ):
                    location = []
                    for g in re.finditer(r"USBROOT\((\w+)\)|#USB\((\w+)\)", loc_path_str.value):
                        if g.group(1):
                            location.append(f"{int(g.group(1)) + 1:d}")
                        else:
                            location.append("." if len(location) > 1 else "-")
                            location.append(g.group(2))
                    if bInterfaceNumber is not None:
                        # XXX how to determine correct bConfigurationValue?
                        location.append(f":{'x'}.{bInterfaceNumber}")
                    if location:
                        info.location = "".join(location)
                info.hwid = info.usb_info()
            elif szHardwareID_str.startswith("FTDIBUS"):
                m = re.search(
                    r"VID_([0-9a-f]{4})\+PID_([0-9a-f]{4})(\+(\w+))?", szHardwareID_str, re.I
                )
                if m:
                    info.vid = int(m.group(1), 16)
                    info.pid = int(m.group(2), 16)
                    if m.group(4):
                        info.serial_number = m.group(4)
                # USB location is hidden by FTDI driver :(
                info.hwid = info.usb_info()
            else:
                info.hwid = szHardwareID_str

            # Bus Reported Device Name
            szBusReportedDeviceDesc = create_unicode_buffer(250)
            devPropType = ULONG()
            if SetupDiGetDeviceProperty(
                g_hdi,
                byref(devinfo),
                byref(DEVPKEY_Device_BusReportedDeviceDesc),
                byref(devPropType),
                byref(szBusReportedDeviceDesc),
                sizeof(szBusReportedDeviceDesc) - 1,
                None,
                0,
            ):
                info.product = szBusReportedDeviceDesc.value

            # Friendly name
            szFriendlyName = create_unicode_buffer(250)
            if SetupDiGetDeviceRegistryProperty(
                g_hdi,
                byref(devinfo),
                SPDRP_FRIENDLYNAME,
                None,
                byref(szFriendlyName),
                sizeof(szFriendlyName) - 1,
                None,
            ):
                info.description = szFriendlyName.value

            # Manufacturer
            szManufacturer = create_unicode_buffer(250)
            if SetupDiGetDeviceRegistryProperty(
                g_hdi,
                byref(devinfo),
                SPDRP_MFG,
                None,
                byref(szManufacturer),
                sizeof(szManufacturer) - 1,
                None,
            ):
                info.manufacturer = szManufacturer.value
            yield info
        SetupDiDestroyDeviceInfoList(g_hdi)


def comports(include_links: bool = False) -> list[PortInfo]:
    return list(iterate_comports())
