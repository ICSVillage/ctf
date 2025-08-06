import traceback

import data
import commands


def cmdHelp():
    print('Help')
    for (k, v) in commands.items():
        print(k + (" [" + str.join(', ', v['alias']) + "]: " if len(v['alias']) > 0 else ": ") + v['desc'])


commands = {
    'help': {
        'alias': ['h'],
        'desc': 'Display Help',
        'func': cmdHelp
    },
    'exit': {
        'alias': ['quit', 'q'],
        'desc': 'Exit Program',
        'func': quit
    },
    'msg': {
        'alias': [],
        'desc': 'Custom CIP Message',
        'func': commands.cmdCustomMsg
    },
    'msg-who': {
        'alias': ['who'],
        'desc': 'CIP Who Message',
        'func': commands.cmdWhoMsg
    },
    'msg-tag-list': {
        'alias': ['tag-list'],
        'desc': 'List Program Tags',
        'func': commands.cmdListTags
    },
    'msg-tag-read': {
        'alias': ['read'],
        'desc': 'Read Tag',
        'func': commands.cmdTagRead
    },
    'msg-tag-write': {
        'alias': ['write'],
        'desc': 'Write Tag',
        'func': commands.cmdTagWrite
    },
    'msg-prog-name': {
        'alias': ['prog-name'],
        'desc': 'CIP Get Program Name Message',
        'func': commands.cmdProgNameMsg
    },
    'msg-key-position': {
        'alias': ['key-pos'],
        'desc': 'CIP Key Position Message',
        'func': commands.cmdKeyPosMsg
    },
    'discover': {
        'alias': ['scan'],
        'desc': 'Scan for PLCs',
        'func': commands.cmdDiscover
    },
    'connect': {
        'alias': ['c'],
        'desc': 'Connect to a device',
        'func': commands.cmdConnect
    },
    'disconnect': {
        'alias': ['d'],
        'desc': 'Disconnect from the connected device',
        'func': commands.cmdDisconnect
    },
    'reconnect': {
        'alias': ['r'],
        'desc': 'Reconnect to the device',
        'func': commands.cmdReconnect
    },
    'status': {
        'alias': ['s'],
        'desc': 'Connection status to the device',
        'func': commands.cmdConnectionStatus
    },
    'path': {
        'alias': [],
        'desc': 'Print the current CIP path to the device',
        'func': commands.cmdPrintCipPath
    }
}


def cli():
    print(data.versionName + ' ' + data.versionString + ':' + str(data.versionId))
    while True:
        rawInput = input('> ')
        found = False
        for k in commands:
            c = commands[k]
            if rawInput == k or rawInput in c['alias']:
                if k == 'exit':
                    c['func']()
                else:
                    try:
                        c['func']()
                    except:
                        print("An error occurred running the command")
                        # printing stack trace
                        traceback.print_exc()

                found = True
                break
        if not found:
            print("Unknown Command")


if __name__ == '__main__':
    cli()
