import Gui, IPStorage, StoneGenerator
from twisted.internet import reactor
from twisted.python import log
from autobahn.websocket import WebSocketServerFactory,WebSocketServerProtocol, listenWS
import sys,thread

###WEBSOCKETPROTOCOL USED FOR COMMUNICATION####
class EchoServerProtocol(WebSocketServerProtocol):
    
    def onClose(self,wasClean,code,reason):
        print "Client left"
        ipStorage.dropConnection(self.peer.host) ##Drop Connection out of IPStorage when Client disconnects
        ipStorage.updateAll("Client with IP "+self.peer.host+" has disconnected")#Update all
        
    def onOpen(self):
        ipStorage.addNewClient(self.peer.host, self) ##adds current Connection and Client IP to the Storage
        ipStorage.updateAll("New Client with IP "+self.peer.host+" has joined")
              
    def onMessage(self, msg, binary):
        print "sending echo:", msg ##print incoming message
        self.sendMessage("Received: "+msg, binary)##send back message to initiating client
        


class main():
    
    def __init__(self):
        stone = StoneGenerator()
        gui = Gui(stone, ipStorage)
        thread.start_new_thread(self.initializeWebSocket, ()) ##start the WebSocket in new Thread

        
    def initializeWebSocket(self):##Starts the WebSocket
        log.startLogging(sys.stdout)##Create a logfile (not necessary)
        self.factory = WebSocketServerFactory("ws://localhost:9000", debug = False)
        self.factory.protocol = EchoServerProtocol ##assign our Protocol to send/receive Messages
        listenWS(self.factory)
        reactor.run(installSignalHandlers=0)##"installSignalHandlers=0" Necessary for Multithreading @UndefinedVariable<-------------------------------------War davor ein Fehler!!!

if __name__ == '__main__':
    ipStorage = IPStorage
    main()
    
