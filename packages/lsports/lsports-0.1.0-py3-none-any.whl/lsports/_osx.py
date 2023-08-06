# Originally sourced from pySerial. https://github.com/pyserial/pyserial
# (C) 2011-2015 Chris Liechti <cliechti@gmx.net>
# SPDX-License-Identifier:    BSD-3-Clause
from __future__ import annotations

import ctypes
from ctypes import byref, create_string_buffer

from lsports._common import PortInfo

# List all of the callout devices in OS/X by querying IOKit.
# See the following for a reference of how to do this:
# http://developer.apple.com/library/mac/#documentation/DeviceDrivers/Conceptual/WorkingWSerial/WWSerial_SerialDevs/SerialDevices.html#//apple_ref/doc/uid/TP30000384-CIHGEAFD

# More help from darwin_hid.py
# Also see the 'IORegistryExplorer' for an idea of what we are actually searching

kCFStringEncodingMacRoman = 0
kCFStringEncodingUTF8 = 0x08000100

# defined in `IOKit/usb/USBSpec.h`
kUSBVendorString = b"USB Vendor Name"
kUSBSerialNumberString = b"USB Serial Number"

# `io_name_t` defined as `typedef char io_name_t[128];` in `device/device_types.h`
io_name_size = 128

# defined in `mach/kern_return.h`
KERN_SUCCESS = 0
# kern_return_t defined as `typedef int kern_return_t;` in `mach/i386/kern_return.h`
kern_return_t = ctypes.c_int

iokit = ctypes.cdll.LoadLibrary("/System/Library/Frameworks/IOKit.framework/IOKit")
cf = ctypes.cdll.LoadLibrary("/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation")

# kIOMasterPortDefault is no longer exported in BigSur but no biggie, using NULL works just the same
kIOMasterPortDefault = 0  # WAS: ctypes.c_void_p.in_dll(iokit, "kIOMasterPortDefault")
kCFAllocatorDefault = ctypes.c_void_p.in_dll(cf, "kCFAllocatorDefault")

iokit.IOServiceMatching.restype = ctypes.c_void_p

iokit.IOServiceGetMatchingServices.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
iokit.IOServiceGetMatchingServices.restype = kern_return_t

iokit.IORegistryEntryGetParentEntry.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
iokit.IOServiceGetMatchingServices.restype = kern_return_t

iokit.IORegistryEntryCreateCFProperty.argtypes = (
    ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32  # fmt: skip
)
iokit.IORegistryEntryCreateCFProperty.restype = ctypes.c_void_p

iokit.IORegistryEntryGetPath.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
iokit.IORegistryEntryGetPath.restype = kern_return_t

iokit.IORegistryEntryGetName.argtypes = (ctypes.c_void_p, ctypes.c_void_p)
iokit.IORegistryEntryGetName.restype = kern_return_t

iokit.IOObjectGetClass.argtypes = (ctypes.c_void_p, ctypes.c_void_p)
iokit.IOObjectGetClass.restype = kern_return_t

iokit.IOObjectRelease.argtypes = (ctypes.c_void_p,)


cf.CFStringCreateWithCString.argtypes = (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int32)
cf.CFStringCreateWithCString.restype = ctypes.c_void_p

cf.CFStringGetCStringPtr.argtypes = (ctypes.c_void_p, ctypes.c_uint32)
cf.CFStringGetCStringPtr.restype = ctypes.c_char_p

cf.CFStringGetCString.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_long, ctypes.c_uint32)
cf.CFStringGetCString.restype = ctypes.c_bool

cf.CFNumberGetValue.argtypes = (ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p)
cf.CFNumberGetValue.restype = ctypes.c_void_p

# void CFRelease ( CFTypeRef cf );
cf.CFRelease.argtypes = (ctypes.c_void_p,)
cf.CFRelease.restype = None

# CFNumber type defines
kCFNumberSInt8Type = 1
kCFNumberSInt16Type = 2
kCFNumberSInt32Type = 3
kCFNumberSInt64Type = 4


def get_string_property(device_type: ctypes._CData, property: bytes) -> str | None:
    """Search the given device for the specified string property.

    Args:
        device_type:
            Type of Device.

        property:
            Bytestring to search for.

    Returns:
        Python string containing the value, or None if not found.
    """
    key = cf.CFStringCreateWithCString(kCFAllocatorDefault, property, kCFStringEncodingUTF8)
    CFContainer = iokit.IORegistryEntryCreateCFProperty(device_type, key, kCFAllocatorDefault, 0)
    output = None
    if CFContainer:
        output = cf.CFStringGetCStringPtr(CFContainer, 0)
        if output is not None:
            output = output.decode("utf-8")
        else:
            buffer = create_string_buffer(io_name_size)
            success = cf.CFStringGetCString(
                CFContainer, byref(buffer), io_name_size, kCFStringEncodingUTF8
            )
            if success:
                output = buffer.value.decode("utf-8")
        cf.CFRelease(CFContainer)
    return output


def get_int_property(device_type: ctypes._CData, property: bytes, cf_type: int) -> int | None:
    """Search the given device for the specified string property.

    Args:
        device_type:
            Device to search.

        property:
            Bytestring to search for.

        cf_type:
            CFType number.

    Returns:
        Python int containing the value, or None if not found.
    """
    key = cf.CFStringCreateWithCString(kCFAllocatorDefault, property, kCFStringEncodingUTF8)
    CFContainer = iokit.IORegistryEntryCreateCFProperty(device_type, key, kCFAllocatorDefault, 0)
    if CFContainer:
        number: ctypes.c_uint32 | ctypes.c_uint16
        if cf_type == kCFNumberSInt32Type:
            number = ctypes.c_uint32()
        elif cf_type == kCFNumberSInt16Type:
            number = ctypes.c_uint16()
        else:
            raise NotImplementedError(f"CFType {cf_type} not implemented")
        cf.CFNumberGetValue(CFContainer, cf_type, byref(number))
        cf.CFRelease(CFContainer)
        return number.value
    return None


def IORegistryEntryGetName(device: ctypes._CData) -> str | None:
    devicename = create_string_buffer(io_name_size)
    res = iokit.IORegistryEntryGetName(device, byref(devicename))
    if res != KERN_SUCCESS:
        return None
    # I don't know if this encoding is guaranteed. It may be dependent on system locale.
    return devicename.value.decode("utf-8")


def IOObjectGetClass(device: ctypes._CData) -> bytes:
    classname = create_string_buffer(io_name_size)
    iokit.IOObjectGetClass(device, byref(classname))
    return classname.value


def GetParentDeviceByType(device: ctypes._CData, parent_type: bytes) -> ctypes._CData | None:
    """Find the first parent of a device that implements the ``parent_type``.

    Args:
        device:
            IOService Service to inspect.

        parent_type:
            Type of parent to find.

    Returns:
        Pointer to the parent type, or None if it was not found.
    """
    # First, try to walk up the IOService tree to find a parent of this device that is a IOUSBDevice.
    while IOObjectGetClass(device) != parent_type:
        parent = ctypes.c_void_p()
        response = iokit.IORegistryEntryGetParentEntry(device, b"IOService", byref(parent))
        # If we weren't able to find a parent for the device, we're done.
        if response != KERN_SUCCESS:
            return None
        device = parent
    return device


def GetIOServicesByType(service_type: bytes) -> list[ctypes._CData]:
    """List specified ``service_type``."""
    serial_port_iterator = ctypes.c_void_p()
    iokit.IOServiceGetMatchingServices(
        kIOMasterPortDefault, iokit.IOServiceMatching(service_type), byref(serial_port_iterator)
    )
    services = []
    while iokit.IOIteratorIsValid(serial_port_iterator):
        service = iokit.IOIteratorNext(serial_port_iterator)
        if not service:
            break
        services.append(service)
    iokit.IOObjectRelease(serial_port_iterator)
    return services


def location_to_string(locationID: int) -> str:
    """Helper to calculate port and bus number from locationID."""
    loc = [f"{locationID >> 24}-"]
    while locationID & 0xF00000:
        if len(loc) > 1:
            loc.append(".")
        loc.append(f"{(locationID >> 20) & 0xf}")
        locationID <<= 4
    return "".join(loc)


class SuitableSerialInterface:
    def __init__(self, id: int | None, name: str | None) -> None:
        self.id = id
        self.name = name


def scan_interfaces() -> list[SuitableSerialInterface]:
    """Helper function to scan USB interfaces.

    Returns:
        A list of SuitableSerialInterface objects with name and id attributes.
    """
    interfaces = []
    for service in GetIOServicesByType(b"IOSerialBSDClient"):
        device = get_string_property(service, b"IOCalloutDevice")
        if device:
            usb_device = GetParentDeviceByType(service, b"IOUSBInterface")
            if usb_device:
                name = get_string_property(usb_device, b"USB Interface Name") or None
                locationID = (
                    get_int_property(usb_device, b"locationID", kCFNumberSInt32Type) or None
                )
                interfaces.append(SuitableSerialInterface(locationID, name))
    return interfaces


def search_for_locationID_in_interfaces(
    serial_interfaces: list[SuitableSerialInterface], locationID: int
) -> str | None:
    for interface in serial_interfaces:
        if interface.id == locationID:
            return interface.name
    return None


def comports(include_links: bool = False) -> list[PortInfo]:
    # include_links is currently ignored. Are links in /dev even supported here?
    # Scan for all iokit serial ports
    services = GetIOServicesByType(b"IOSerialBSDClient")
    ports = []
    serial_interfaces = scan_interfaces()
    for service in services:
        # First, add the callout device file.
        device = get_string_property(service, b"IOCalloutDevice")
        if device:
            info = PortInfo(device)
            usb_device = GetParentDeviceByType(service, b"IOUSBHostDevice")
            if not usb_device:
                # If the serial port is implemented by IOUSBDevice (deprecated as of 10.11)
                usb_device = GetParentDeviceByType(service, b"IOUSBDevice")
            if usb_device:
                # Fetch some useful information from properties
                info.vid = get_int_property(usb_device, b"idVendor", kCFNumberSInt16Type)
                info.pid = get_int_property(usb_device, b"idProduct", kCFNumberSInt16Type)
                info.serial_number = get_string_property(usb_device, kUSBSerialNumberString)
                # We know this is a usb device, so the IORegistryEntryName should always be aliased
                # to the usb product name string descriptor.
                info.product = IORegistryEntryGetName(usb_device) or "n/a"
                info.manufacturer = get_string_property(usb_device, kUSBVendorString)
                locationID = get_int_property(usb_device, b"locationID", kCFNumberSInt32Type)
                assert locationID is not None
                info.location = location_to_string(locationID)
                info.interface = search_for_locationID_in_interfaces(serial_interfaces, locationID)
                info.apply_usb_info()
            ports.append(info)
    return ports
