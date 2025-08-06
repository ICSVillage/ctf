import data


def printBytes(value):
    count = len(value)
    print("Result: " + str(count) + " bytes")
    print("      0  1  2  3  4  5  6  7  8  9 ")
    print("     +----------------------------+")
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

    print("     +----------------------------+")
    print("ASCII:")
    print(value)


def printResult(result, struct=None):
    if result.error is None:
        if struct == None:
            printBytes(result.value)
        else:
            print(struct.decode(result.value))
    else:
        print(result.error)


def sendRequest(serviceId, classId, instanceId, attributeId=0x00, sourceBuffer=b''):
    with data.driver as plc:
        if ',' in data.cipPath or '/' in data.cipPath:
            return plc.generic_message(service=serviceId, class_code=classId, instance=instanceId,
                                       attribute=attributeId,
                                       request_data=sourceBuffer,
                                       connected=False, unconnected_send=True, route_path=True
                                       )
        else:
            return plc.generic_message(service=serviceId, class_code=classId, instance=instanceId,
                                       attribute=attributeId,
                                       request_data=sourceBuffer
                                       )
