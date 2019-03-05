# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 09:23:32 2019

"""

from socket import *

Host = 'localhost'
Port = 20003
Bufsiz = 1024
Addr = (Host, Port)

while True:
    tcpcl = socket()
    tcpcl.connect(Addr)
    data = input('>' )
    if not data:
        break
    tcpcl.send(('%s\r\n' % data).encode())
    data = tcpcl.recv(Bufsiz)
    if not data:
        break
    print(data.decode().strip())
    tcpcl.close()