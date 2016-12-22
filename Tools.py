import os
import time


def usagePrint():
    print 'Welcome to use this tool!'
    print '**************************************'
    print '1\tshutdown process X after Y minutes'
    print '2\texit'
    print '**************************************'
    print 'input your command(1 or 2)'


def shutdown():
    process = raw_input('process name\tX=')
    t = raw_input('wait how long to close\tY=')
    if '.exe' not in process:
        process = process + '.exe'
    print process
    count = float(t) * 60
    while count > 0:
        count -= 1
        time.sleep(1)
        os.system('cls')
        print 'countdown %d seconds' % count
    os.system('taskkill -f -im %s' % process)
    os.system('cls')


if __name__ == '__main__':
    usagePrint()
    command = raw_input()
    while True:
        if command == '1':
            shutdown()
            usagePrint()
            command = raw_input()
        elif command == '2':
            exit()
        else:
            os.system('cls')
            print 'wrong command!'
            usagePrint()
            command = raw_input()
