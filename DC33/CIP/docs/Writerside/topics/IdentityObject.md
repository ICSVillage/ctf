# Identity Object (0x01)
The CIP Device Identity Object

## Overview
- **Class Code**: `0x01`
- **Purpose**: Provides device identification and general status information.
- **Instances**: Typically, a device has one instance (Instance 1) of the Identity Object.
- **Access**: Attributes are generally read-only, except for specific services like Reset.

## Attributes
The Identity Object includes several attributes that describe the device's identity and status. The following are the common attributes defined in the CIP specification:

| Attribute ID | Name                     | Data Type       | Description                                                                 | Access  |
|--------------|--------------------------|-----------------|-----------------------------------------------------------------------------|---------|
| 1            | Vendor ID                | UINT            | Unique identifier of the device vendor (assigned by ODVA).                   | Read    |
| 2            | Device Type              | UINT            | Indicates the general type of device (e.g., PLC, sensor, drive).             | Read    |
| 3            | Product Code             | UINT            | Vendor-specific code identifying the product.                                | Read    |
| 4            | Revision                 | STRUCT of USINT | Major and minor firmware/hardware revision (e.g., Major.Minor).              | Read    |
| 5            | Status                   | WORD            | Current status of the device (e.g., owned, configured, faulted).             | Read    |
| 6            | Serial Number            | UDINT           | Unique serial number for the device.                                        | Read    |
| 7            | Product Name             | SHORT_STRING    | Human-readable name or description of the device.                           | Read    |

### Notes on Attributes
- **Vendor ID**: Assigned by ODVA (Open DeviceNet Vendor Association) to uniquely identify the manufacturer.
- **Device Type**: Maps to a predefined list of device profiles (e.g., 0x02 for AC drives, 0x0C for communications adapter).
- **Revision**: Split into Major and Minor fields to indicate significant or minor changes in firmware/hardware.
- **Status**: A bit field indicating various states (e.g., bit 0: Owned, bit 4-7: Device state like running or faulted).
- **Serial Number**: Must be unique for each device within a vendor’s product line.
- **Product Name**: A string limited to 32 characters in most implementations.

## Services
The Identity Object supports several services to interact with its attributes or control the device. Common services include:

| Service Code | Name                   | Description                                                                 |
|--------------|------------------------|-----------------------------------------------------------------------------|
| 0x01         | Get_Attributes_All     | Retrieves all attributes of the Identity Object in a single response.        |
| 0x05         | Reset                  | Initiates a device reset (e.g., power cycle, factory reset).                 |
| 0x0E         | Get_Attribute_Single   | Retrieves the value of a single specified attribute.                         |
| 0x10         | Set_Attribute_Single   | Sets the value of a single specified attribute (if writable).                |

### Reset Service Types
The Reset service (0x05) supports different reset types, typically specified in the service data:
- **Type 0**: Power cycle (simulates power off/on).
- **Type 1**: Factory reset (returns to out-of-box settings).
- **Additional types**: May be vendor-specific (e.g., reboot to bootloader).

## Instance and Class Details
- **Class Attributes**: Typically include revision and instance count information.
- **Instance Attributes**: Instance 1 contains the device-specific identity data (as listed above).
- **Mandatory Attributes**: Attributes 1–7 are required for compliance with CIP standards.
- **Optional Attributes**: Vendors may add custom attributes (e.g., Attribute 8 and above) for additional device-specific information.

## Usage
- The Identity Object is used during device discovery and configuration in CIP networks.
- It allows network tools or controllers to identify devices, check their status, and perform basic operations like resets.
- Commonly accessed during network commissioning or diagnostics.