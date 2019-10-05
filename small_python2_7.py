from __future__ import print_function
from multiprocessing import Process
d = '/dev/ttyS0'
def r():
 f = open(d, 'rb')
 while True:
  o = f.read(1)
  if o != '':
   print(o, end='')
p = Process(target=r)
p.start()
f = open(d, 'w')
while True:
 f.write(raw_input('>')+"\r")
 f.flush()