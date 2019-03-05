# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:20:04 2019

"""
from twisted.internet import protocol, reactor

Host = 'localhost'
Port = 20004

class TSClntProtocl(protocol.Protocol):
    def sendData(self):
        data = input('>')
        if data:
            print('...sending %s...' % data)
            self.transport.write(data.encode())
        else:
            self.transport.loseConnection()
    
    def connectionMade(self):
        self.sendData()
    
    def dataReceived(self, data):
        print(data)
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocl
    clientConnectionLost = clientConnectionFailed = \
    lambda self, connector, reason: reactor.stop()

reactor.connectTCP(Host, Port, TSClntFactory())
reactor.run()
