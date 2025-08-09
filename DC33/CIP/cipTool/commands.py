from pycomm3.packets import ListIdentityRequestPacket

import data
import util
import structs
from pycomm3 import CIPDriver, CommError, Struct, DINT, UINT, Revision, n_bytes, UDINT, SHORT_STRING, STRING, INT, \
    LogixDriver


def cmdConnect():
    if data.driver is not None:
        data.driver.close()
        print("Disconnected from " + data.cipPath)
    data.cipPath = input("Enter PLC CIP Path: ")
    data.driver = CIPDriver(data.cipPath)
    try:
        data.driver.open()
    except CommError as e:
        print('Failed to connect to device')


def cmdReconnect():
    if data.driver is None or not data.driver.connected:
        print("Not connected to device")
        return
    data.driver = CIPDriver(data.cipPath)
    data.driver.open()


def cmdDisconnect():
    if data.driver is not None:
        data.driver.close()
        print('Disconnected')
    else:
        print('Not connected to device')


def cmdPrintCipPath():
    if data.cipPath is not None:
        print('CIP Path: ' + data.cipPath)
    else:
        print('No CIP Path')


def cmdConnectionStatus():
    if data.driver is None:
        print("No connection")
    else:
        print("Connected")


def cmdCustomMsg():
    if data.driver is None:
        print("Please connect to a device")
        return
    print('Enter Custom CIP Command Info')
    msgService = int(input('Service: '), 0)
    msgClass = int(input('Class: '), 0)
    msgInstance = int(input('Instance: '), 0)
    msgAttribute = int(input('Attribute: '), 0)
    msgSrcBuffer = bytes(input('Src Buffer: '), 'utf-8')

    result = util.sendRequest(msgService, msgClass, msgInstance, msgAttribute, msgSrcBuffer)
    util.printResult(result)


def cmdWhoMsg():
    if data.driver is None:
        print("Please connect to a device")
        return
    result = util.sendRequest(0x01, 0x01, 0x01)
    util.printResult(result, structs.whoStruct)


def cmdListTags():
    if data.driver is None:
        print("Please connect to a device")
        return

    with LogixDriver(data.cipPath) as plc:
        tagList = plc.get_tag_list()
        for tag in tagList:
            print(tag)


def cmdTagRead():
    if data.driver is None:
        print("Please connect to a device")
        return

    with LogixDriver(data.cipPath) as plc:
        tagName = input('Tag Name: ')
        value = plc.read(tagName)
        print(value)


def cmdTagWrite():
    if data.driver is None:
        print("Please connect to a device")
        return

    with LogixDriver(data.cipPath) as plc:

        tagName = input('Tag Name: ')
        tagValue = input('Tag Value: ')
        tag = plc.read(tagName)
        if tag.type == 'DINT':
            value = plc.write((tagName, int(tagValue)))
        elif tag.type == 'REAL':
            value = plc.write((tagName, float(tagValue)))
        elif tag.type == 'BOOL':
            value = plc.write((tagName, (tagValue == '1' or tagValue == 'true' or tagValue == 'True')))
        print(value)


def cmdKeyPosMsg():
    if data.driver is None:
        print("Please connect to a device")
        return
    result = util.sendRequest(0x0E, 0x01, 0x01, 0x05)
    print("Mode: " + format(result.value[0], 'b'))
    print("Key: " + format(result.value[1], 'b'))
    if result.error is None:
        if result.value[0] & 0b01110000 == 0b01110000:
            print("Mode: Program")
        elif result.value[0] & 0b01100000 == 0b01100000:
            print("Mode: Run")
        else:
            print("Mode: Unknown")

        if result.value[1] & 0b00110000 == 0b00110000:
            print("Key Position: Remote")
        elif result.value[1] & 0b00100000 == 0b00100000:
            print("Key Position: Program")
        elif result.value[1] & 0b00010000 == 0b00010000:
            print("Key Position: Run")
        else:
            print("Key Position: Unknown")
    else:
        print(result.error)


def cmdProgNameMsg():
    if data.driver is None:
        print("Please connect to a device")
        return
    result = util.sendRequest(0x03, 0x64, 0x01, 0x00, b'\x01\x00\x01\x00')
    msgStruct = Struct(
        INT, DINT, STRING('name')
    )
    util.printResult(result, msgStruct)


def cmdDiscover():
    print('Discovering PLCs')
    print(CIPDriver.discover())

