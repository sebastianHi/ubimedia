from libavg import AVGApp
from TextRectNode import *
from IPStorage import *
from MainMenue import MainMenue
from LobbyMenue import LobbyMenue
from GameMenue import  GameMenue
from twisted.internet import reactor
from twisted.python import log
from autobahn.websocket import WebSocketServerFactory,WebSocketServerProtocol, listenWS
import sys,thread 

class Gui(AVGApp):
    
    def __init__(self,ipStorage):
        #/////////////////////////////////////
        self.field1 = None
        self.field2 = None
        #/////////Eckpunkte///////////////////
        self.linksFeld1X    =0
        self.linksFeld2X    =0
        self.rechtsFeld1X   =0
        self.rechtsFeld2X   =0
        self.yOben          =0
        self.yUnten         =0
        #/////////////////////////////////////
        self.matrix = [[]]
        #/////////////////////////////////////
        self.leftFallingBlock = None
        self.rightFallingBlock = None
        self.blocksize = 0   
        self.ipStorage = ipStorage
    
        self.keepCountingToStart = True
        self.player=avg.Player.get()
        self.canvas=self.player.createMainCanvas(size=(1440,900))
        self.rootNode=self.canvas.getRootNode()
        
        
        self.mainMenu = MainMenue(self.rootNode)
 
        self.mainMenu.button1vs1.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.mainMenu.button1vs1, self.onClickMain1v1)
        self.mainMenu.button2vs2.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.mainMenu.button2vs2, self.onClickMain2v2)
        self.mainMenu.button1vs1vs1.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.mainMenu.button1vs1vs1, self.onClickMain1v1v1)
        self.mainMenu.button1vs1.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.mainMenu.button1vs1, self.onClickMain1v1)
        self.mainMenu.button2vs2.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.mainMenu.button2vs2, self.onClickMain2v2)
        self.mainMenu.button1vs1vs1.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.mainMenu.button1vs1vs1, self.onClickMain1v1v1)
        self.mainMenu.divNodeMainMenue.active = True 
        
        thread.start_new_thread(self.initializeWebSocket, ())##start the WebSocket in new Thread
                                
        
    def initLobby(self, modus):
        self.lobbyMenu = LobbyMenue(self.rootNode, modus) 
        self.lobbyMenu.backButton.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.lobbyMenu.backButton, self.backToMenue)
        self.lobbyMenu.firstPlayer.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.lobbyMenu.firstPlayer, self.test) 
        self.lobbyMenu.backButton.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.lobbyMenu.backButton, self.backToMenue)
        self.lobbyMenu.secondPlayer.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.lobbyMenu.secondPlayer, self.gameCounter)  
        
        self.mainMenu.divNodeMainMenue.active = False 
        self.lobbyMenu.divNodelobbyMenue.active = True 
        #ZumUebergangZumGame               
        
    def initGame(self):
        self.gameMenu = GameMenue(self.rootNode, self.player)
        
        self.lobbyMenu.divNodelobbyMenue.active = False 
        self.gameMenu.divNodeGameMenue.active = True 

   



#-----------------------------------------------Lobby Methoden----------------------------------------------------------------------------------------------------------------------------
    
    def gameCounter(self,event):
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

    def eventHandler(self):
        self.initGame()
        self.test   = avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (200, 200), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.blocksize ,self.blocksize)
                                  )
    
    
  
    
#-------------------------------------------------MenuesOffSwitches-----------------------------------------------------------------------------------------------------------------------

    
    def test(self, event):  ## <<-----------------loeschbar nur zum counter test
        self.initGame()
    
    
#----------------------------------------------------------EventHandler-----------------------------------------------------------------------------------------------------------------
    
    def onClickMain1v1(self, event):
        self.initLobby(2)
         
    def onClickMain1v1v1(self, event):
        self.initLobby(3)    
     
    def onClickMain2v2(self, event):
        self.initLobby(4)
        
    def backToMenue(self, event):
        self.lobbyMenu.divNodelobbyMenue.active = False
        self.mainMenu.divNodeMainMenue.active = True
        self.ipStorage.getAllCurrentConnections()
        for ip in self.ipStorage.getAllCurrentConnections():
            self.ipStorage.dropConnection(ip)
        
 
#-----------------------------------------------------------Eventuell unnuetz: Notfall fuer IP Mac Probleme-------------------------------------------------------------------------------   

    def initializeWebSocket(self):##Starts the WebSocket
        log.startLogging(sys.stdout)##Create a logfile (not necessary)
        self.factory = WebSocketServerFactory("ws://localhost:55555", debug = False)
        self.factory.protocol = EchoServerProtocol ##assign our Protocol to send/receive Messages
        listenWS(self.factory)
        reactor.run(installSignalHandlers=0)##"installSignalHandlers=0" Necessary for Multithreading @UndefinedVariable
        

#-----------------------------------------------------------Erinnerungen was noch zutun ist-----------------------------------------------------------------------------------------------
   
    def newGame(self):
        pass
    
    def getRdy (self):
        pass
    
    def movePlayer(self):
        pass
    
    def setRole(self):
        pass
    
    def startNewRound(self):
        pass
    
    def speedUp(self):
        pass
    
    def updateScore(self):
        pass
    
    def pause(self):
        pass
    
    def timer(self):
        pass

    def usedSkill(self):
        pass
    
    def usedSpecialSkill(self):
        pass
    
    def alertNotEnoughMoney(self):
        pass
     
    def updateClock(self):
        pass
    
    def updateCooldowns(self):
        pass
    
    def chanceLevel(self):
        pass

 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
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
        ipStorage.eventHandler(msg);

if __name__ == '__main__':
    ipStorage = IPStorage()
    gui = Gui(ipStorage)
    ipStorage.initGui(gui)
    gui.player.play()