# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 15:27:06 2019

"""
#一个小型的客户机
import socket

s = socket.socket()
host = socket.gethostname()
port = 1234

s.connect((host, port))
print(s.recv(1024).decode())