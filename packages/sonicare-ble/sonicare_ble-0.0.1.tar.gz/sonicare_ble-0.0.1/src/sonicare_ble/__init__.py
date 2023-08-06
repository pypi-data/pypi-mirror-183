"""Parser for Sonicare BLE advertisements.

This file is shamelessly copied and adapted from the following repository:
https://github.com/Bluetooth-Devices/oralb-ble/blob/main/src/oralb_ble/__init__.py

which was also copied from

https://github.com/Ernst79/bleparser/blob/c42ae922e1abed2720c7fac993777e1bd59c0c93/package/bleparser/oral_b.py


MIT License applies.
"""
from __future__ import annotations

from sensor_state_data import (
    BinarySensorDeviceClass,
    BinarySensorValue,
    DeviceKey,
    SensorDescription,
    SensorDeviceClass,
    SensorDeviceInfo,
    SensorUpdate,
    SensorValue,
    Units,
)

from .parser import SonicareBinarySensor, SonicareBluetoothDeviceData, SonicareSensor

__version__ = "0.0.1"

__all__ = [
    "SonicareSensor",
    "SonicareBinarySensor",
    "sonicareBluetoothDeviceData",
    "BinarySensorDeviceClass",
    "BinarySensorValue",
    "SensorDescription",
    "SensorDeviceInfo",
    "DeviceKey",
    "SensorUpdate",
    "SensorDeviceClass",
    "SensorDeviceInfo",
    "SensorValue",
    "Units",
]
