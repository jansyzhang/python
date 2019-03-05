# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 15:19:56 2019

"""

from socket import socket

Host = "localhost"
BUFSIZ = 1024
Port = 20000
addr = (Host, Port)

cl = socket()
cl.connect(addr)


while True:
    data = input('>')
    if not data:
        break
    cl.send(bytes(data,'utf-8'))
    #cl.send(data.encode())
    data = cl.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
cl.close()
