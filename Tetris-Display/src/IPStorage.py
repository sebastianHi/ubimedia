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
                print "Nachricht An Kevin: "+ key+"###"+msg
                self._ipList[key].sendMessage(key+"###"+msg)
    
    #sendet nachricht an nur eine ip    
    def sendMessageToOneIP(self,ip,msg):
        if (self._ipList[ip] != None):
            print "Nachricht An Kevin: "+ ip+"###"+msg
            self._ipList[ip].sendMessage(ip+"###"+msg)
     
    #sendet ip an sich selbst        
    def sendIp(self,ip):
        if (self._ipList[ip] != None):
            self._ipList[ip].sendMessage(ip)