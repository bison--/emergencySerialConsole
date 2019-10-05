from __future__ import print_function
from multiprocessing import Process
device = '/dev/ttyS0' #1 set device
def read():
    print('READING')
    f = open(device, 'rb')
    while True:
        out = f.read(1)
        if out != '':
            print(out, end='')

p = Process(target=read)
p.start()

f = open(device, 'w')
while True:
    inp = raw_input('>')
    f.write(inp + "\r") #2 return char
    f.flush()