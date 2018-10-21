#!/usr/bin/python3
import sys
import subprocess
import socket

s=socket.socket()
ip='127.0.0.1'
port=12345
s.bind((ip,port))
s.listen(5)
c,addr=s.accept()

cmd = c.recv(1024)

cmd = cmd.decode()
cmdMain = cmd.split("'")
cmd = cmdMain[0]

output = subprocess.check_output(cmd,shell=True)
c.send(output)

c.close()
