'''
Created on 15.06.2013

@author: sebastian
'''
###THIS CLASS SIMPLY HOLDS THE CONNECTED CLIENT IPS####
class IPStorage():
    def __init__(self):
        self._ipList=dict({})
        
    def addNewClient(self,ip,connection): ##adds a new Client to the Dictionary
        self._ipList[ip]=connection 
    
    def dropConnection(self,ip):##removes Connection out of Dict
        self._ipList[ip] = None
        
    def getAllCurrentConnections(self):#returns all currently active Connections
        return self._ipList
    
    def getConnectionForIp(self,ip):##returns a Connection to a Client with a certain IP
        return self._ipList[ip]
    
    def updateAll(self,msg): #sends Message to all connected Clients
        for key in self._ipList:
            if (self._ipList[key] != None):
                self._ipList[key].sendMessage(key+"###"+msg)
        
    def sendMessageToOneIP(self,ip,msg):
        self._ipList[ip].sendMessage(msg)