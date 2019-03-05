# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:46:08 2019

"""
#一个小型的服务器

import socket

s = socket.socket() #创建服务器套接字

host = socket.gethostname()
port = 1234

s.bind((host, port)) #套接字与地址绑定
s.listen(5) #监听连接，传入与连接请求最大数

while True:
    c, addr = s.accept()
    print('got connection from', addr)
    c.send(('thank you for connecting').encode())
    c.close()