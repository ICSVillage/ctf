from pycomm3 import CIPDriver

address: str = '10.0.0.212,1,1'

classes = {
    '0x1': "Device",
    '0x2': "MessageRouter",
    '0x3': "Device Net",
    '0x4': "Assembly",
    '0x5': 'Connection',
    '0x6': "Connection Manager",
    '0x7': "Register",
    '0x8': "Digital Input",
    '0x9': "Digital output",
    '0xA': "Analog Input",
    '0xB': "Analog Output",
    '0xE': "Presence Sensing",
    '0xF': "Parameter",

    '0x10': "Parameter Group",
    '0x12': "Group",
    '0x1D': 'Digital Input Group',
    '0x1E': 'Digital Output Group',
    '0x1F': 'Digital Group',
    '0x20': 'Analog Input Group',
    '0x21': 'Analog Output Group',
    '0x22': 'Analog Group',
    '0x23': 'Position Sensor',
    '0x24': 'Position Controller Supervisor',
    '0x25': 'Position Controller',
    '0x26': 'Block Sequencer',
    '0x27': 'Command Block',
    '0x28': 'Motor Data',
    '0x29': 'Control Supervisor',
    '0x2A': 'AC/DC Drive',
    '0x2B': 'Acknowledge Handler',
    '0x2C': 'Overload',
    '0x2D': 'Softstart',
    '0x2E': 'Selection',
    '0x30': "Device Supervisor (Safety)",
    '0x31': "Analog Sensor (Safety)",
    '0x32': "Analog Actuator (Safety)",
    '0x33': "Single Stage Controller (Safety)",
    '0x34': "Gas Calibration (Safety)",
    '0x35': "Trip Point (Safety)",
    '0x37': "File Object (Safety)",
    '0x38': "Partial Pressure (Safety)",
    '0x39': "Supervisor (Safety)",
    '0x3A': "Validator (Safety)",
    '0x3B': "Digital Output Point (Safety)",
    '0x3C': "Digital Output Group (Safety)",
    '0x3D': "Digital Input Point (Safety)",
    '0x3E': "Digital Input Group (Safety)",
    '0x3F': "Dual Channel Output (Safety)",
    '0x40': "Sensor Calibration (Safety)",
    '0x41': 'Event Log',
    '0x42': 'Motion Axis',
    '0x43': "Time Synchronize",
    '0x44': 'Modbus',
    '0x46': 'Serial Link',
    '0x47': "Device Level Ring",
    '0x4E': "Base Energy Object",
    '0x4F': "Electrical Energy Object",
    '0x64': "ExtendedDevice",
    '0x66': "Integrated Control Platform",
    '0x67': "PCCC",
    '0x68': "Program",
    '0x69': "I/OMap",
    '0x6A': "DataTable",
    '0x6B': "Symbol",
    '0x6C': "UserTemplate",
    '0x6D': "Executable",
    '0x6E': "ERRD",
    '0x6F': "Serial Port",
    '0x70': "UserTask",
    '0x71': "Data Logging",
    '0x72': "UserMemory",
    '0x73': "FaultLog",
    '0x74': "Semaphore",
    '0x77': "Coordinated System Time",
    '0x7C': "1771 Discrete I/O Rack",
    '0x7E': "I/OConnection",
    '0x7F': "Built In Functions",
    '0x80': "Remote I/O Status",
    '0x85': "Production",
    '0x8B': "Wall Clock Time",
    '0x8C': "Label",
    '0x8D': "Message",
    '0x8E': "Controller",
    '0xA2': "DF1 Com Driver",
    '0xA3': "ASCII Com Driver",
    '0xA4': "Routing Table",
    '0xA5': "DH PLUS",
    '0xA6': "DH Plus Interface",
    '0xA7': "ICP Rack",
    '0xA8': "Remote I/O",
    '0xAA': "Ethernet TCP/IP",
    '0xAC': "Change Log",
    '0xB0': "Axis Group",
    '0xB1': "Axis",
    '0xB2': "Trending",
    '0xC0': "Redundancy",
    '0xF0': "Control Net",
    '0xF1': "Control Net Keeper",
    '0xF2': "Control Net Scheduling",
    '0xF3': "Control Net Configuration",
    '0xF4': "Port Object",
    '0xF5': "TCP/IP Interface",
    '0xF6': "Ethernet Link",
    '0xF7': "Component Link",
    '0xF8': "Component Repeater",
    '0xFF': "Test",
    '0x300': "Virtual Backplane",
    '0x304': "Port",
    '0x316': "Transition",
    '0x317': "Chart",
    '0x318': "Step",
    '0x319': "Action",
    '0x31A': "File Manager",
    '0x32B': "Coordinate System",
    '0x32D': "Equipment Phase",
    '0x331': "Digital Alarm",
    '0x332': "Analog Alarm",
    '0x334': "Safety Controller",
    '0x338': "UDI Definition",
    '0x33A': "Universal Serial Bus",
    '0x342': 'Socket',
    '0x348': "Metadata Definition",
    '0x36A': "Security Authority Binding",
    '0x36E': "HMI Button Control",
    '0x378': "Logix Repository",
    '0x37D': "Logix Library Object",
    '0x3A6': "Configured Alarm",
    '0x3A7': "Alarm Set",
    '0x3A8': "Alarm Condition Definition",
    '0x3B0': "Device Diagnostics Object",
    '0x3B1': "Device Diagnostic Profile",
    '0x3B2': "Diagnostics Message",
    '0x412': "Resilient Transport Object",
    '0x4FE': "Data Type Member",
}


def printBytes(value):
    count = len(value)
    print("Result: " + str(count) + " bytes")
    print("      0  1  2  3  4  5  6  7  8  9 ")
    print("    +-----------------------------+")
    for r in range(0, count, 10):
        packedByteString = ""
        maxRange = r + 10 if r + 10 < count else count
        for c in range(r, maxRange):
            packedByteString += "{:02x}".format(value[c])
            if c < maxRange - 1:
                packedByteString += ' '
        if maxRange - r < 10:
            for b in range(maxRange, r + 10):
                packedByteString += '   '

        print('{0:0{1}}'.format(r, 4) + "|" + packedByteString + "|")

    print("    +-----------------------------+")
    print("ASCII:")
    print(value)


# List supported CIP classes from the message router on the controller
def cipListClasses():
    with CIPDriver(address) as plc:
        result = plc.generic_message(service=0x01, class_code=0x02, instance=0x01, attribute=0x00, connected=False,
                                     unconnected_send=True, route_path=True)
        if result.error is not None:
            print(result.error)
            return

        printBytes(result.value)

        print('Num of Classes: ' + str(result.value[0] + result.value[1] * 0x10))
        for i in range(2, len(result.value), 2):
            classCode = result.value[i] + result.value[i + 1] * 0x10
            classHex = f"0x{classCode:X}"
            className = classes[str(classHex)] if str(classHex) in classes else 'Unknown'
            print('Class: ' + classHex + ': ' + className)


def cipService4CTest():
    with CIPDriver(address) as plc:
        result = plc.generic_message(service=0x4C, class_code=0x04, instance=130, attribute=0x00,
                                     request_data=b'\x01\x00\x03\x00',
                                     connected=False, unconnected_send=True, route_path=True)
        if result.error is not None:
            print(result.error)
            return

        printBytes(result.value)


def cipFindClassVersionsService3():
    with CIPDriver(address) as plc:
        for classId in range(1, 1000):
            result = plc.generic_message(service=0x03, class_code=classId, instance=0x00, attribute=0x00,
                                         request_data=b'\x01\x00\x01\x00',
                                         connected=False, unconnected_send=True, route_path=True)


            classHex = f"0x{classId:X}"
            className = classes[str(classHex)] if str(classHex) in classes else 'Unknown'

            version = 0
            if result.error is None and len(result.value) > 0:
                printBytes(result.value)
                version = result.value[2] + result.value[3] * 0x10 if len(result.value) > 2 else 0

            if result.error is None:
                print('Class: ' + classHex + ' v' + str(version) + ': ' + className)
            else:
                print('?Class: ' + classHex + ': ' + className + " = " + result.error)

    print('Done!')


def cipFindClassesService1():
    with CIPDriver(address) as plc:
        for classId in range(1, 0x100):
            result = plc.generic_message(service=0x01, class_code=classId, instance=0x01, attribute=0x00,
                                         request_data=b'',
                                         connected=False, unconnected_send=True, route_path=True)

            classHex = f"0x{classId:X}"
            className = classes[str(classHex)] if str(classHex) in classes else 'Unknown'

            if result.error is None:
                print('Class: ' + classHex + ': ' + className)
                printBytes(result.value)
            elif len(result.value) > 1 and result.value[0] != 0x00 and result.value[1] != 0x00:
                # pass
                print('?Class: ' + classHex + ': ' + className)
                printBytes(result.value)
            else:
                # pass
                print('XClass: ' + classHex + ': ' + className + ": " + result.error)

    print('Done!')


def cipFindAssemblyServices():
    with CIPDriver(address) as plc:
        for instanceId in range(1, 256):
            print('Instance: ' + str(instanceId))
            for serviceId in range(1, 0x100):
                try:
                    result = plc.generic_message(service=serviceId, class_code=0x04, instance=instanceId,
                                                 attribute=0x00,
                                                 request_data=b'',
                                                 connected=False, unconnected_send=True, route_path=True)

                    if result.error is None:
                        print('Service: ' + str(serviceId))
                        printBytes(result.value)
                    elif len(result.value) > 1 and result.value[0] != 0x00 and result.value[1] != 0x00:
                        # pass
                        print('?Service: ' + str(serviceId))
                        print(result.error)
                        printBytes(result.value)
                    else:
                        # pass
                        print('XService: ' + str(serviceId) + ": " + result.error)
                except:
                    pass

    print('Done!')


def cipFindService4B():
    with CIPDriver(address) as plc:
        for instanceId in range(0, 256):
            print('Instance: ' + str(instanceId))
            for classId in range(4, 256):
                try:
                    result = plc.generic_message(service=0x4b, class_code=classId, instance=instanceId,
                                                 attribute=0x00,
                                                 request_data=b'',
                                                 connected=False, unconnected_send=True, route_path=True)

                    if result.error is None:
                        print('Class: ' + str(classId))
                        printBytes(result.value)
                    elif len(result.value) > 1 and result.value[0] != 0x00 and result.value[1] != 0x00:
                        # pass
                        print('?Class: ' + str(classId))
                        print(result.error)
                        printBytes(result.value)
                    else:
                        pass
                        # print('XClass: ' + str(classId) + ": " + result.error)
                except:
                    pass

    print('Done!')


def cipFindService0E():
    with CIPDriver(address) as plc:
        for instanceId in range(0, 256):
            for attr in range(1, 256):
                try:
                    result = plc.generic_message(service=0x0E, class_code=0x04, instance=instanceId,
                                                 attribute=attr,
                                                 request_data=b'',
                                                 connected=False, unconnected_send=True, route_path=True)

                    if result.error is None:
                        print('Instance: ' + str(instanceId))
                        print('Attr: ' + str(attr))
                        printBytes(result.value)
                    elif len(result.value) > 1 and result.value[0] != 0x00 and result.value[1] != 0x00:
                        # pass
                        print('?Instance: ' + str(instanceId))
                        print('?Attr: ' + str(attr))
                        print(result.error)
                        printBytes(result.value)
                    else:
                        pass
                        # print('XAttr: ' + str(classId) + ": " + result.error)
                except:
                    pass

    print('Done!')


def cipFindIOInstance():
    with CIPDriver(address) as plc:
        for instanceId in range(0, 255):
            try:
                result = plc.generic_message(service=0x4B, class_code=0x04, instance=instanceId,
                                             attribute=0x00,
                                             request_data=b'',
                                             connected=False, unconnected_send=True, route_path=True)

                if result.error is None:
                    print('Instance: ' + str(instanceId))
                    print('Found')
                    printBytes(result.value)
                elif len(result.value) > 1 and result.value[0] != 0x00 and result.value[1] != 0x00:
                    # pass
                    print('Instance: ' + str(instanceId))
                    print('?Found')
                    print(result.error)
                    printBytes(result.value)
                else:
                    pass
                    print('Instance: ' + str(instanceId))
                    print('X:' + result.error)

            except:
                pass

    print('Done!')


def cipGetClassInstanceInfo():
    classCodeStr = input('Class Code: ')
    classCode = None
    if classCodeStr.startswith('0x'):
        classCode = int(classCodeStr, 16)
    else:
        classCode = int(classCodeStr)

    with CIPDriver(address) as plc:
        result = plc.generic_message(service=0x03, class_code=classCode, instance=0x00, attribute=0x00,
                                     request_data=b'\x02\x00\x02\x00\x03\x00',
                                     connected=False, unconnected_send=True, route_path=True)
        printBytes(result.value)


# Attempt to get supported services optional attribute from class
# Note: I have yet to actually run into a class in ControlLogix that supports this
def cipGetClassServices():
    classCodeStr = input('Class Code: ')
    classCode = None
    if classCodeStr.startswith('0x'):
        classCode = int(classCodeStr, 16)
    else:
        classCode = int(classCodeStr)

    with CIPDriver(address) as plc:
        result = plc.generic_message(service=0x0E, class_code=classCode, instance=0x00, attribute=0x05,
                                     connected=False, unconnected_send=True, route_path=True)
        printBytes(result.value)


def cipGetAllAttributes():
    classCodeStr = input('Class Code: ')
    classCode = None
    if classCodeStr.startswith('0x'):
        classCode = int(classCodeStr, 16)
    else:
        classCode = int(classCodeStr)

    instanctCodeStr = input('Instance Code: ')
    instanceCode = None
    if instanctCodeStr.startswith('0x'):
        instanceCode = int(instanctCodeStr, 16)
    else:
        instanceCode = int(instanctCodeStr)

    with CIPDriver(address) as plc:
        result = plc.generic_message(service=0x01, class_code=classCode, instance=instanceCode, attribute=0x00,
                                     connected=False, unconnected_send=True, route_path=True)
        printBytes(result.value)


# Get basic info from controller
def cipGetInfo():
    with CIPDriver(address) as plc:
        result = plc.generic_message(
            service=0x01,          # Get All Attributes
            class_code=0x01,       # Device Identity Class
            instance=0x01,         # Default Instance
            attribute=0x00,        # No Attribute
            connected=False,       # Use Unconnected Send instead of UCMM
            unconnected_send=True, # Use Unconnected Send instead of UCMM
            route_path=True        # Use Unconnected Send instead of UCMM
        )
        printBytes(result.value)

if __name__ == '__main__':
    # cipGetInfo()
    # cipListClasses()
    # cipService4CTest()
    cipFindClassVersionsService3()
    # cipFindClassesService1()
    # cipGetClassServices()
    # cipFindAssemblyServices()
    # cipGetAllAttributes()
    # cipGetClassInstanceInfo()
    # cipFindIOInstance()
    # cipFindService4B()
    # cipFindService0E()
