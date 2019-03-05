# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 09:14:57 2019

"""

from socketserver import TCPServer as TCP
from socketserver import StreamRequestHandler as SRH
from time import ctime 

Host = ''
Port = 20003
Addr = (Host, Port)

class MyRequestHandle(SRH):
    def handle(self):
        print('...connect from:', self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(), self.rfile.readline())).encode())
        
tcpServ = TCP(Addr, MyRequestHandle)
print('waiting for connection...')
tcpServ.serve_forever()