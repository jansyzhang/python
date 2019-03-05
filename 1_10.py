# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:33:23 2019

"""

import socket
import select

s = socket.socket()

host = socket.gethostname()
port = 1234

s.bind((host, port))
s.listen(5)

inputs = [s]
while True:
    #select函数阻塞进程，直到inputs中的套接字被触发（在此例中，套接字接收到客户端发来的握手信号，
    #从而变得可读，满足select函数的“可读”条件），rs返回被触发的套接字（服务器套接字）；  
    #select再次阻塞进程，同时监听服务器套接字和获得的客户端套接字；  
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r is s: #如果是服务器套接字被触发（监听到有客户端连接服务器）  
            c, addr = s.accept()
            print('got connection from', addr)
            inputs.append(c) # inputs加入客户端套接字  
        else:
            # 当客户端发送数据时，客户端套接字被触发，rs返回客户端套接字，然后进行下一步处理。  
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True
            
            if disconnected:
                print(r.getpeername(), 'disconnected')
                inputs.remove(r)
            else:
                print(data)
