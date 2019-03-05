# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:18:48 2019

"""

from twisted.internet import protocol, reactor
from time import ctime

Port = 20004

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('connect from', clnt)  
    
    def dataReceived(self, data):
        self.transport.write(('[%s] %s' % (ctime(), data)).encode())
        
factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connecton...')
reactor.listenTCP(Port, factory)
reactor.run()
                             