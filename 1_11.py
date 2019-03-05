# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:01:00 2019

"""
import socket, select

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))
#建立通过fileno查找IO对象的字典
fdmap = {s.fileno(): s}


s.listen(5)
p = select.poll()
#注册关注IO事件,p.register(s,POLLIN | POLLERR)
p.register(s)
while True:
    #监控关注的IO
    events = p.poll()
    for fd, event in events:
        if fd in fdmap:
            c, addr = s.accept()
            print ('Got connection from', addr)
            #客户端退出,取消关注,维护字典
            p.register(c)
            #客户端退出,取消关注,维护字典
            fdmap[c.fileno()] = c
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024)
            if not data: # No data -- connection closed
                #客户端退出,取消关注,维护字典
                print (fdmap[fd].getpeername(), 'disconnected')
                p.unregister(fd)
                del fdmap[fd]
            else:
                print (data)
