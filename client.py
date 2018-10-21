#!/usr/bin/python3

import sys
import socket

s=socket.socket()
ip=sys.argv[1]
port=int(sys.argv[2])
cmd=sys.argv[3]

cmd = str.encode(cmd)
s.connect((ip,port))
s.send(cmd)

output=s.recv(1024)
print(output.decode())
s.close()
