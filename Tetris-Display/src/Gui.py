from libavg import AVGApp
from TextRectNode import *
from IPStorage import *
from MainMenue import MainMenue
from LobbyMenue import LobbyMenue
from GameMenue import  GameMenue
from twisted.internet import reactor
from GameTypeMenue import GameTypeMenue
from twisted.python import log
from autobahn.websocket import WebSocketServerFactory,WebSocketServerProtocol, listenWS
import sys,thread 

class Gui(AVGApp):
    
    def init(self):

############################################################
#        zustand = 0    :    Gui ist im MainMenu
#        zustand = 1    :    Gui ist im LobbyMenu
#        zustand = 2    :    Gui ist im Gamemenu
############################################################

        self.zustand = 0
        self.gtype = 0  # 0 = classic    1 = equal
        self.ipStorage = ipStorage
        self.alreadyServerRunning = False
    
        self.keepCountingToStart = True
        self.player= avg.Player.get()
        self.rootNode= self._parentNode
        
        
        self.mainMenu = MainMenue(self.rootNode)
        self.mainMenu.button1vs1.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.mainMenu.button1vs1, self.onClickMain1v1)
        self.mainMenu.button2vs2.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.mainMenu.button2vs2, self.onClickMain2v2)
        self.mainMenu.button1vs1vs1.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.mainMenu.button1vs1vs1, self.onClickMain1v1v1)
        self.mainMenu.divNodeMainMenue.active = True 
        
        
    def initWhatGame(self):
        self.typeMenu = GameTypeMenue(self.rootNode)
        self.typeMenu.buttonEqualMode.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.typeMenu.buttonEqualMode, self.onClickEqual)
        self.typeMenu.buttonNormalMode.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.typeMenu.buttonNormalMode, self.onClickNormal)
        self.typeMenu.backButton.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.typeMenu.buttonNormalMode, self.backToMenue) 
        self.mainMenu.divNodeMainMenue.active = False 
        self.typeMenu.divNodeTypeMenue.active = True                           
        
    def initLobby(self):
        self.lobbyMenu = LobbyMenue(self.rootNode, self.modus,self,self.gtype) 
        self.lobbyMenu.backButton.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.lobbyMenu.backButton, self.backToType)
        
#-------------------------------ZUM TESTEN ------------------------------------------------------------------------------------------------------------------------------
        self.lobbyMenu.firstPlayer.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.lobbyMenu.firstPlayer, self.test)   
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        self.mainMenu.divNodeMainMenue.active = False 
        self.lobbyMenu.divNodelobbyMenue.active = True 
        self.zustand = 1
        #ZumUebergangZumGame
        if(not(self.alreadyServerRunning)) : 
            self.alreadyServerRunning = True
            thread.start_new_thread(self.initializeWebSocket, ())##start the WebSocket in new Thread         
        
    def initGame(self):
        self.gameMenu = GameMenue(self.rootNode, self.player)
        
        self.lobbyMenu.divNodelobbyMenue.active = False 
        self.gameMenu.divNodeGameMenue.active = True
        self.zustand = 2
        #TODO:  + rollenzuweisung
        #self.ipStorage.updateAll("gamestarts")



#-----------------------------------------------Lobby Methoden----------------------------------------------------------------------------------------------------------------------------
    
    def gameCounter(self):
        self.count = 9
        if(self.lobbyMenu.modus == 2):
            self.lobbyMenu.firstPlayer.setInactiv()
            self.lobbyMenu.secondPlayer.setInactiv()
        elif(self.lobbyMenu.modus == 3):
            self.lobbyMenu.firstPlayer.setInactiv()
            self.lobbyMenu.secondPlayer.setInactiv()
            self.lobbyMenu.thirdPlayer.setInactiv()
        elif(self.lobbyMenu.modus == 4):
            self.lobbyMenu.firstPlayer.setInactiv()
            self.lobbyMenu.secondPlayer.setInactiv()
            self.lobbyMenu.thirdPlayer.setInactiv()
            self.lobbyMenu.forthPlayer.setInactiv()
        else:
            raise SyntaxError("Wrong Modus gameCounter")
         
        self.countNode = TextRectNode(parent = self.lobbyMenu.divNodelobbyMenue, 
                                   pos = (self.lobbyMenu.divNodelobbyMenue.size[0]/4,self.lobbyMenu.divNodelobbyMenue.size[1]*0.45),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.lobbyMenu.divNodelobbyMenue.size[0]/2,self.lobbyMenu.divNodelobbyMenue.size[1]*0.35))
        
        self.countNode.addText("Gamestart: "+ str(self.count), "000000")  
        self.countNode.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.countNode, self.interruptCount)
        #TODO: touch
        self.timer = self.player.setInterval(1000, self.countCount)
        self.gameStartTimer = self.player.setInterval(10000, self.maybeStart)
        
    def interruptCount(self, event):
        self.keepCountingToStart = False
        self.maybeStart()
        
        
    def maybeStart(self):
        self.player.clearInterval(self.gameStartTimer)
        self.player.clearInterval(self.timer)
        self.countNode.setInactiv()
        if(self.keepCountingToStart):
            self.initGame()
             
        elif(self.lobbyMenu.modus == 2):
            self.lobbyMenu.divNodelobbyMenue.active = True
            self.lobbyMenu.firstPlayer.setActiv()
            self.lobbyMenu.secondPlayer.setActiv()
        elif(self.lobbyMenu.modus == 3):
            self.lobbyMenu.divNodelobbyMenue.active = True
            self.lobbyMenu.firstPlayer.setActiv()
            self.lobbyMenu.secondPlayer.setActiv()
            self.lobbyMenu.thirdPlayer.setActiv()
        elif(self.lobbyMenu.modus == 4):
            self.lobbyMenu.divNodelobbyMenue.active = True
            self.lobbyMenu.firstPlayer.setActiv()
            self.lobbyMenu.secondPlayer.setActiv()
            self.lobbyMenu.thirdPlayer.setActiv()
            self.lobbyMenu.forthPlayer.setActiv()
        else:
            raise SyntaxError("Wrong Modus gameCounter")
        
   
   
    def countCount(self):
        self.count -=1
        self.countNode.updateTextNode("Gamestart: "+ str(self.count))
      
       
    
#-----------------------------------------------Interaction with App/socket--------------------------------------------------------------------------------------------------------------

    def eventHandler(self,msg):
##parser
        print msg
        ip = ""
        l = []
        count = 0
        for c in msg:
            if(c == '#'):
                if(count ==0):
                    ip = ''.join(l)
                    l = []
                count+=1
                
            else:
                l.append(c)
          
        
        befehl = ''.join(l)
        
        print "befehl: ",befehl,"ip: ",ip   
##eigentlicher eventhander mit befehl:
#----------------------Anmeldung Des Clients-------------------------------
        if((befehl[0:9]== 'nickname:' )& (self.zustand == 1)):
            print "GotNickForIP : ",ip," Nick: ", befehl[9:befehl.__len__()]
            self.lobbyMenu.updateJoinedPlayerNumber(ip, befehl[9:befehl.__len__()])
#----------------------Bewegungen Des Blocks-------------------------------!!!!!!<--- brauche den aktuell fallenden Block bzw links oder rechts
        elif(  (befehl == "moveLeft" )   & (self.zustand == 2)):
            print "GotMoveLeft"
            if(ip == self.lobbyMenu.playerIP[0]):
                self.gameMenu.field1.moveLeft()
            elif(ip == self.lobbyMenu.player[2]):
                self.gameMenu.field2.moveLeft()
            else:
                raise SyntaxError("Falscher Spieler wollte bewegung machen; Gui") 
            
        elif((befehl == "moveRight")   & (self.zustand == 2)):
            print "GotMoveRight"
            if(ip == self.lobbyMenu.playerIP[0]):
                self.gameMenu.field1.moveRight()
            elif(ip == self.lobbyMenu.player[2]):
                self.gameMenu.field2.moveRight()
            else:
                raise SyntaxError("Falscher Spieler wollte bewegung machen; Gui") 
            
        elif((befehl == "moveRotateR" )& (self.zustand == 2)):
            print "GotMoveRotateR"
            if(ip == self.lobbyMenu.playerIP[0]):
                self.gameMenu.field1.rotateRight()
            elif(ip == self.lobbyMenu.player[2]):
                self.gameMenu.field2.rotateRight()
            else:
                raise SyntaxError("Falscher Spieler wollte bewegung machen; Gui") 
            
        elif((befehl == "moveRotateL" )& (self.zustand == 2)):
            print "GotRotateL"
            if(ip == self.lobbyMenu.playerIP[0]):
                self.gameMenu.field1.rotateLeft()
            elif(ip == self.lobbyMenu.player[2]):
                self.gameMenu.field2.rotateLeft()
            else:
                raise SyntaxError("Falscher Spieler wollte bewegung machen; Gui") 
            
#-----------------------Rdy Signal fuer Lobby------------------------------
        elif((befehl == "rdy")):
            self.lobbyMenu.playerGotRdy(ip)

           
    
#-------------------------------------------------MenuesOffSwitches-----------------------------------------------------------------------------------------------------------------------

    
    def test(self, event):  ## <<-----------------loeschbar nur zum gamestart mit mausklick
        self.initGame()
    
    
#----------------------------------------------------------EventHandlerButtoms----------------------------------------------------------------------------------------------------------
    
    def onClickMain1v1(self, event):
        self.modus = 2
        self.initWhatGame()
         
    def onClickMain1v1v1(self, event):
        self.modus = 3   
        self.initWhatGame()
        
    def onClickMain2v2(self, event):
        self.modus = 4
        self.initWhatGame()
        
    def onClickEqual(self,event):
        self.gtype = 1
        self.initLobby()

    def onClickNormal(self, event):
        self.gtype = 0
        self.initLobby()
        
    def backToType(self, event):
        self.lobbyMenu.divNodelobbyMenue.active = False
        self.typeMenu.divNodeTypeMenue.active = True
        for ip in self.ipStorage.getAllCurrentConnections():
            self.ipStorage.dropConnection(ip)
        
    def backToMenue(self, event):
        self.typeMenu.divNodeTypeMenue.active = False
        self.mainMenu.divNodeMainMenue.active = True
        
        
 
#-----------------------------------------------------------Eventuell unnuetz: Notfall fuer IP Mac Probleme-------------------------------------------------------------------------------   

    def initializeWebSocket(self):##Starts the WebSocket
        log.startLogging(sys.stdout)##Create a logfile (not necessary)
        self.factory = WebSocketServerFactory("ws://localhost:55555", debug = False)
        self.factory.protocol = EchoServerProtocol ##assign our Protocol to send/receive Messages
        listenWS(self.factory)
        reactor.run(installSignalHandlers=0)##"installSignalHandlers=0" Necessary for Multithreading @UndefinedVariable
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
###WEBSOCKETPROTOCOL USED FOR COMMUNICATION####
class EchoServerProtocol(WebSocketServerProtocol):
     
    def onClose(self,wasClean,code,reason):
        print "Client left"
        ipStorage.dropConnection(self.peer.host) ##Drop Connection out of IPStorage when Client disconnects
        ipStorage.updateAll("Client with IP "+self.peer.host+" has disconnected")#Update all
         
    def onOpen(self):
        ipStorage.addNewClient(self.peer.host, self) ##adds current Connection and Client IP to the Storage
        self.sendMessage(self.peer.host) #Sends IP-Adress to Target
        ipStorage.updateAll("New Client with IP "+self.peer.host+" has joined")
        self.sendMessage(self.peer.host+"###"+"Test") ##See if Parser Works.
               
    def onMessage(self, msg, binary):
        print "sending echo:", msg ##print incoming message
        #self.sendMessage("Received: "+msg, binary)##send back message to initiating client
        Gui.eventHandler(msg)

if __name__ == '__main__':
    ipStorage = IPStorage()
    Gui.start(resolution = (900,600))