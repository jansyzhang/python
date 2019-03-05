# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 15:49:49 2019

"""

#一个基于Socketerver的小型服务器
from socketserver import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler): # 创建一个请求处理类
    
    def handle(self):
        addr = self.request.getpeername()
        print('Got connetion from', addr)
        self.wfile.write('Thank you for connecting')
    
server = TCPServer(('', 1236), Handler) #实例化一个服务器类，传入服务器的地址和请求处理的程序类
server.serve_forever()

#使用了分叉技术的服务器
from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler

class Server(ForkingMixIn, TCPServer): pass

class Handler(StreamRequestHandler):
    
    def handle(self):
        addr = self.request.getpeername()
        print('Got connetion from', addr)
        self.wfile.write('Thank you for connecting')
        
server = Server(('', 1236), Handler) 
server.serve_forever()

#使用线程处理的服务器
from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler

class Server(ThreadingMixIn, TCPServer): pass

class Handler(StreamRequestHandler):
    
    def handle(self):
        addr = self.request.getpeername()
        print('Got connetion from', addr)
        self.wfile.write('Thank you for connecting')
        
server = Server(('', 1236), Handler) 
server.serve_forever()