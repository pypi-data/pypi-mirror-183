# lsports

A simple Python 3.7+ module to list serial ports on Windows, Linux, and macOS.

This is a modified version of `serial.tools.list_ports` from
[pySerial](https://github.com/pyserial/pyserial) by Chris Liechti.

## Installation

```bash
pip install lsports
```

## Usage

The module provides a single function `comports` that returns a list of `PortInfo` objects.
Each `PortInfo` object contains information about a connected serial port.
```python
from lsports import comports

for port in comports():
    print(port.device, port.product, port.hwid)
```
For a full list of available attributes, see the `PortInfo` class. Only `comports` and `PortInfo`
are considered public API.
