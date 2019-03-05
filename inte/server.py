# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 15:09:14 2019

"""

from socket import socket
from time import ctime

Host = ""
BUFSIZ = 1024
Port = 20000
addr = (Host, Port)

ss = socket()
ss.bind(addr)
ss.listen()

while True:
    print('waiting for connection...')
    cl, Addr = ss.accept()
    print('connect from ', Addr)
    while True:
        data = cl.recv(BUFSIZ)
        if not data:
            break
        type(data)
        cl.send(bytes(('[%s] %s' % (ctime(), data)), 'utf-8'))
    cl.close()

