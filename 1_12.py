# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:17:23 2019

"""
#使用twisted的简单服务器

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

class SimpleLogger(Protocol):
    
    def connectionMade(self):
        print('got connection from', self.transport.client)
        
    def connectionLost(self, reason):
        print(self.transport.client, 'disconnected')
        
    def dataReceived(self, data):
        print(data)
    
factory = Factory()
factory.protocol = SimpleLogger
reactor.listenTCP(1234, factory)
reactor.run()

#使用LineReceived协议改进记录服务器
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver

class SimpleLogger(LineReceiver):
    
    def connectionMade(self):
        print('got connection from', self.transport.client)
        
    def connectionLost(self, reason):
        print(self.transport.client, 'disconnected')
        
    def LineReceived(self, line):
        print(line)
    
factory = Factory()
factory.protocol = SimpleLogger
reactor.listenTCP(1234, factory)
reactor.run()

