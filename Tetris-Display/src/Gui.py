from libavg import AVGApp
from TextRectNode import *
from collections import deque
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
    
        self.zumtestenaberloeschbar = True #HierLoeschbar
        self.zustand = 0
        self.gtype = 0  # 0 = classic    1 = equal
        self.ipStorage = ipStorage
        self.alreadyServerRunning = False
        self.dreiSpielerSkillSwitch = False
    
        self.keepCountingToStart = True
        self.player= avg.Player.get()
        self.rootNode= self._parentNode
        self.switchAttacker = True
        self.checkMsgTimer = self.player.setInterval(10, self.checkMsg)
        
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
        
#-------------------------------ZUM TESTEN ------------------------------------------------------------------------------------------------------------------------------------
        #TODO: Zum Testen self.lobbyMenu.firstPlayer.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.lobbyMenu.firstPlayer, self.test)   
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        self.mainMenu.divNodeMainMenue.active = False 
        self.lobbyMenu.divNodelobbyMenue.active = True 
        self.zustand = 1
        #ZumUebergangZumGame
        if(not(self.alreadyServerRunning)) : 
            self.alreadyServerRunning = True
            thread.start_new_thread(self.initializeWebSocket, ())##start the WebSocket in new Thread         
        
    def initGame(self):
        self.gameMenu = GameMenue(self.rootNode, self.player, self.gtype, self)
        self.lobbyMenu.divNodelobbyMenue.active = False 
        self.gameMenu.divNodeGameMenue.active = True
        self.zustand = 2
        self.gameMenu.winLooseMenu.buttonNextGame.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.gameMenu.winLooseMenu.buttonNextGame, self.backToMainAfterGameFinished)
        #rollenzuweisung
        if(self.zumtestenaberloeschbar):
            if(self.lobbyMenu.modus == 4 ):
                ipStorage.sendMessageToOneIP(self.lobbyMenu.playerIP[0], self.lobbyMenu.playerIP[0]+"###"+"defender")
                ipStorage.sendMessageToOneIP(self.lobbyMenu.playerIP[1], self.lobbyMenu.playerIP[1]+"###"+"defender")
                ipStorage.sendMessageToOneIP(self.lobbyMenu.playerIP[2], self.lobbyMenu.playerIP[2]+"###"+"attacker")
                ipStorage.sendMessageToOneIP(self.lobbyMenu.playerIP[3], self.lobbyMenu.playerIP[3]+"###"+"attacker")
            if(self.lobbyMenu.modus == 3 ):
                ipStorage.sendMessageToOneIP(self.lobbyMenu.playerIP[0], self.lobbyMenu.playerIP[0]+"###"+"defender")
                ipStorage.sendMessageToOneIP(self.lobbyMenu.playerIP[1], self.lobbyMenu.playerIP[1]+"###"+"defender")
                ipStorage.sendMessageToOneIP(self.lobbyMenu.playerIP[2], self.lobbyMenu.playerIP[2]+"###"+"attacker")
            if(self.lobbyMenu.modus == 2 ):
                ipStorage.sendMessageToOneIP(self.lobbyMenu.playerIP[0], self.lobbyMenu.playerIP[0]+"###"+"defender")
                ipStorage.sendMessageToOneIP(self.lobbyMenu.playerIP[1], self.lobbyMenu.playerIP[1]+"###"+"defender")

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
        self.lobbyMenu.backButton.setInactiv()
        self.countNode.addText("Gamestart: "+ str(self.count), "000000")  
        self.countNode.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.countNode, self.interruptCount)
        self.timer = self.player.setInterval(1000, self.countCount)
        self.gameStartTimer = self.player.setInterval(10000, self.maybeStart)
        
    def interruptCount(self, event):
        self.keepCountingToStart = False
        self.lobbyMenu.rdyPlayer =  [False,False,False,False]
        ipStorage.updateAll("notRdy")
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
        self.lobbyMenu.backButton.setActiv()
        self.keepCountingToStart = True
        
   
   
    def countCount(self):
        self.count -=1
        self.countNode.updateTextNode("Gamestart: "+ str(self.count))
      
       
    
#-----------------------------------------------Interaction with App/socket--------------------------------------------------------------------------------------------------------------

    def eventHandler(self,msg):
##parser

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
           
            self.lobbyMenu.updateJoinedPlayerNumber(ip, befehl[9:befehl.__len__()])
            
        elif((befehl == "disconnect") & (self.zustand ==1)):
            ipStorage.dropConnection(ip)
            self.lobbyMenu.updatePlayerLeft(ip)
#----------------------Bewegungen Des Blocks-------------------------------!!!!!!<--- brauche den aktuell fallenden Block bzw links oder rechts
        elif(  (befehl == "moveLeft" )   & (self.zustand == 2)):
            if(ip == self.lobbyMenu.playerIP[0]):
                self.gameMenu.field1.moveLeft()
            elif(ip == self.lobbyMenu.playerIP[1]):
                self.gameMenu.field2.moveLeft()
            else:
                raise SyntaxError("Falscher Spieler wollte bewegung machen; Gui") 
            
        elif((befehl == "moveRight")   & (self.zustand == 2)):
            if(ip == self.lobbyMenu.playerIP[0]):
                self.gameMenu.field1.moveRight()
            elif(ip == self.lobbyMenu.playerIP[1]):
                self.gameMenu.field2.moveRight()
            else:
                raise SyntaxError("Falscher Spieler wollte bewegung machen; Gui") 
            
        elif((befehl == "RotateR" )& (self.zustand == 2)):
            if(ip == self.lobbyMenu.playerIP[0]):
                self.gameMenu.field1.rotateRight()
            elif(ip == self.lobbyMenu.playerIP[1]):
                self.gameMenu.field2.rotateRight()
            else:
                raise SyntaxError("Falscher Spieler wollte bewegung machen; Gui") 
            
        elif((befehl == "RotateL" )& (self.zustand == 2)):
            if(ip == self.lobbyMenu.playerIP[0]):
                self.gameMenu.field1.rotateLeft()
            elif(ip == self.lobbyMenu.playerIP[1]):
                self.gameMenu.field2.rotateLeft()
            else:
                raise SyntaxError("Falscher Spieler wollte bewegung machen; Gui") 
        
        elif((befehl == "speedDown") & (self.zustand == 2)):
            if(ip == self.lobbyMenu.playerIP[0]):
                self.gameMenu.field1.speedDown()
            elif(ip == self.lobbyMenu.playerIP[1]):
                self.gameMenu.field2.speedDown()
            else:
                raise SyntaxError("Falscher Spieler wollte bewegung machen; Gui") 
            
#-----------------------Rdy Signal fuer Lobby------------------------------
        elif((befehl == "rdy") & (self.zustand == 1)):
            self.lobbyMenu.playerGotRdy(ip)
            
        elif((befehl == "notRdy") & (self.zustand == 1)):
            self.lobbyMenu.playerNotRdyAnylonge(ip)
#----------------------------------------------------Block erzeugen----------------------------------------------------------------------           
        elif(((befehl == "L")|
              (befehl == "cube") |
              (befehl == "I")|
              (befehl == "Z")|
              (befehl == "reverseL")|
              (befehl == "reverseZ")|
              (befehl == "cross") )& (self.zustand == 2)):
            if(self.lobbyMenu.modus == 3 ):
                # fuege block in beide Queues ein
                self.gameMenu.field1.Queue.append(befehl)
                self.gameMenu.field2.Queue.append(befehl)
            else:
                if(ip == self.lobbyMenu.playerIP[2]):
                    # fuege block in feld 2 queue hinzu
                    self.gameMenu.field2.Queue.append(befehl)
                elif(ip == self.lobbyMenu.playerIP[3]):
                    # fuege block in feld1 queue hinzu
                    self.gameMenu.field1.Queue.append(befehl)
                else:
                    raise SyntaxError("Falscher spieler wollte ",befehl," block hinzufuegen")
                
#-----------------------------------------------------Skills aktivieren-------------------------------------------------------------------
    #attacker normal
        elif((befehl == "inverseControl") & (self.zustand == 2)):
            if(self.modus == 4):
                if(ip == self.lobbyMenu.playerIP[2]):
                    self.gameMenu.attackerNormalField2.inverseControl()
                elif(ip == self.lobbyMenu.playerIP[3]):
                    self.gameMenu.attackerNormalField1.inverseControl()
            elif(self.modus == 3):
                if(self.switchAttacker):
                    self.gameMenu.attackerNormalField2.inverseControl()
                    self.switchAttacker = False
                else:
                    self.gameMenu.attackerNormalField1.inverseControl()
                    self.switchAttacker = True          
            else:
                raise SyntaxError(" Falscher spieler wollte normal attacker skill ausfuehren")
                    
        elif((befehl == "leftFreeze") & (self.zustand == 2)):
            if(self.modus == 4):
                if(ip == self.lobbyMenu.playerIP[2]):
                    self.gameMenu.attackerNormalField2.leftFreeze()
                elif(ip == self.lobbyMenu.playerIP[3]):
                    self.gameMenu.attackerNormalField1.leftFreeze()
            elif(self.modus == 3):
                if(self.switchAttacker):
                    self.gameMenu.attackerNormalField2.leftFreeze()
                    self.switchAttacker = False
                else:
                    self.gameMenu.attackerNormalField1.leftFreeze()
                    self.switchAttacker = True          
            else:
                raise SyntaxError(" Falscher spieler wollte normal attacker skill ausfuehren")
            
        elif((befehl == "rightFreeze") & (self.zustand == 2)):
            if(self.modus == 4):
                if(ip == self.lobbyMenu.playerIP[2]):
                    self.gameMenu.attackerNormalField2.rightFreeze()
                elif(ip == self.lobbyMenu.playerIP[3]):
                    self.gameMenu.attackerNormalField1.rightFreeze()
            elif(self.modus == 3):
                if(self.switchAttacker):
                    self.gameMenu.attackerNormalField2.rightFreeze()
                    self.switchAttacker = False
                else:
                    self.gameMenu.attackerNormalField1.rightFreeze()
                    self.switchAttacker = True          
            else:
                raise SyntaxError(" Falscher spieler wollte normal attacker skill ausfuehren")
            
        elif((befehl == "rotateFreeze") & (self.zustand == 2)):
            if(self.modus == 4):
                if(ip == self.lobbyMenu.playerIP[2]):
                    self.gameMenu.attackerNormalField2.rotateFreeze()
                elif(ip == self.lobbyMenu.playerIP[3]):
                    self.gameMenu.attackerNormalField1.rotateFreeze()
            elif(self.modus == 3):
                if(self.switchAttacker):
                    self.gameMenu.attackerNormalField2.rotateFreeze()
                    self.switchAttacker = False
                else:
                    self.gameMenu.attackerNormalField1.rotateFreeze()
                    self.switchAttacker = True          
            else:
                raise SyntaxError(" Falscher spieler wollte normal attacker skill ausfuehren")
            
        elif((befehl == "speedUp") & (self.zustand == 2)):
            if(self.modus == 4):
                if(ip == self.lobbyMenu.playerIP[2]):
                    self.gameMenu.attackerNormalField2.speedUp()
                elif(ip == self.lobbyMenu.playerIP[3]):
                    self.gameMenu.attackerNormalField1.speedUp()
            elif(self.modus == 3):
                if(self.switchAttacker):
                    self.gameMenu.attackerNormalField2.speedUp()
                    self.switchAttacker = False
                else:
                    self.gameMenu.attackerNormalField1.speedUp()
                    self.switchAttacker = True          
            else:
                raise SyntaxError(" Falscher spieler wollte normal attacker skill ausfuehren")
            
        elif((befehl == "makeBlockInvisible") & (self.zustand == 2)):
            if(self.modus == 4):
                if(ip == self.lobbyMenu.playerIP[2]):
                    self.gameMenu.attackerNormalField2.makeBlockInvisible()
                elif(ip == self.lobbyMenu.playerIP[3]):
                    self.gameMenu.attackerNormalField1.makeBlockInvisible()
            elif(self.modus == 3):
                if(self.switchAttacker):
                    self.gameMenu.attackerNormalField2.makeBlockInvisible()
                    self.switchAttacker = False
                else:
                    self.gameMenu.attackerNormalField1.makeBlockInvisible()
                    self.switchAttacker = True          
            else:
                raise SyntaxError(" Falscher spieler wollte normal attacker skill ausfuehren")
            
        elif((befehl == "noPoints") & (self.zustand == 2)):
            if(self.modus == 4):
                if(ip == self.lobbyMenu.playerIP[2]):
                    self.gameMenu.attackerNormalField2.noPoints()
                elif(ip == self.lobbyMenu.playerIP[3]):
                    self.gameMenu.attackerNormalField1.noPoints()
            elif(self.modus == 3):
                if(self.switchAttacker):
                    self.gameMenu.attackerNormalField2.noPoints()
                    self.switchAttacker = False
                else:
                    self.gameMenu.attackerNormalField1.noPoints()
                    self.switchAttacker = True          
            else:
                raise SyntaxError(" Falscher spieler wollte normal attacker skill ausfuehren")
            
    #attacker spezial
        elif((befehl == "orderSuperBlock") & (self.zustand == 2)):
            if(self.modus == 4):
                if(ip == self.lobbyMenu.playerIP[2]):
                    self.gameMenu.attackerSpezialonField2.orderSuperBlock()
                elif(ip == self.lobbyMenu.playerIP[3]):
                    self.gameMenu.attackerSpezialonField1.orderSuperBlock()
            elif(self.modus == 3):
                self.gameMenu.attackerSpezialonField1.orderSuperBlock()
                self.gameMenu.attackerSpezialonField2.orderSuperBlock()
            else:
                raise SyntaxError(" Falscher spieler wollte spezial attacker skill ausfuehren")
            
        elif((befehl == "orderRainOfBlocks") & (self.zustand == 2)):
            if(self.modus == 4):
                if(ip == self.lobbyMenu.playerIP[2]):
                    self.gameMenu.attackerSpezialonField2.orderRainOfBlocks()
                elif(ip == self.lobbyMenu.playerIP[3]):
                    self.gameMenu.attackerSpezialonField1.orderRainOfBlocks()
            elif(self.modus == 3):
                self.gameMenu.attackerSpezialonField1.orderRainOfBlocks()
                self.gameMenu.attackerSpezialonField2.orderRainOfBlocks()
            else:
                raise SyntaxError(" Falscher spieler wollte spezial attacker skill ausfuehren")
            
        elif((befehl == "orderThunder") & (self.zustand == 2)):
            if(self.modus == 4):
                if(ip == self.lobbyMenu.playerIP[2]):
                    self.gameMenu.attackerSpezialonField2.orderThunder()
                elif(ip == self.lobbyMenu.playerIP[3]):
                    self.gameMenu.attackerSpezialonField1.orderThunder()
            elif(self.modus == 3):
                self.gameMenu.attackerSpezialonField1.orderThunder()
                self.gameMenu.attackerSpezialonField2.orderThunder()
            else:
                raise SyntaxError(" Falscher spieler wollte spezial attacker skill ausfuehren")
    #defender
        elif((befehl == "skipBlock") & (self.zustand == 2)):
            if(ip == self.lobbyMenu.playerIP[0]):
                self.gameMenu.defenderSkillsField1.skipBlock()
            elif(ip == self.lobbyMenu.playerIP[1]):
                self.gameMenu.defenderSkillsField2.skipBlock()
            else:
                raise SyntaxError(" Falscher spieler wollte defender skill ausfuehren")
        elif((befehl == "slowPace") & (self.zustand == 2)):
            if(ip == self.lobbyMenu.playerIP[0]):
                self.gameMenu.defenderSkillsField1.slowPace()
            elif(ip == self.lobbyMenu.playerIP[1]):
                self.gameMenu.defenderSkillsField2.slowPace()
            else:
                raise SyntaxError(" Falscher spieler wollte defender skill ausfuehren")
        elif((befehl == "orderBomb") & (self.zustand == 2)):
            if(ip == self.lobbyMenu.playerIP[0]):
                self.gameMenu.defenderSkillsField1.orderBomb()
            elif(ip == self.lobbyMenu.playerIP[1]):
                self.gameMenu.defenderSkillsField2.orderBomb()
            else:
                raise SyntaxError(" Falscher spieler wollte defender skill ausfuehren")
        elif((befehl == "reduceTime") & (self.zustand == 2)):
            if(ip == self.lobbyMenu.playerIP[0]):
                self.gameMenu.defenderSkillsField1.reduceTime()
            elif(ip == self.lobbyMenu.playerIP[1]):
                self.gameMenu.defenderSkillsField2.reduceTime()
            else:
                raise SyntaxError(" Falscher spieler wollte defender skill ausfuehren")     
            
#-------------------------------------------------MenuesOffSwitches-----------------------------------------------------------------------------------------------------------------------

    
    def test(self, event):  ## <<-----------------loeschbar nur zum gamestart mit mausklick
        self.initGame()
        self.zumtestenaberloeschbar = False
    
    
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
        
             
    def backToMainAfterGameFinished(self, event):
        self.gameMenu.winLooseMenu.divNodeWinLooseMenue.active = False
        self.gameMenu.winLooseMenu.buttonNextGame.sensitive = False
        self.mainMenu.divNodeMainMenue.active = True 
        self.gameMenu.speed =1 
        self.gameMenu.round =1   
 
#-----------------------------------------------------------Eventuell unnuetz: Notfall fuer IP Mac Probleme-------------------------------------------------------------------------------   

    def initializeWebSocket(self):##Starts the WebSocket
        log.startLogging(sys.stdout)##Create a logfile (not necessary)
        self.factory = WebSocketServerFactory("ws://localhost:55555", debug = False)
        self.factory.protocol = EchoServerProtocol ##assign our Protocol to send/receive Messages
        listenWS(self.factory)
        reactor.run(installSignalHandlers=0)##"installSignalHandlers=0" Necessary for Multithreading @UndefinedVariable
        
    def checkMsg(self):
        if(len(msgList) > 0):
            msg = msgList.popleft()
            self.eventHandler(msg)
            
    def sendMsgToAll(self, msg):
        ipStorage.updateAll(msg)
        
    def sendMsgToOne(self,ip, msg):
        ipStorage.sendMessageToOneIP(ip, msg)
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
###WEBSOCKETPROTOCOL USED FOR COMMUNICATION####
class EchoServerProtocol(WebSocketServerProtocol):
     
    def onClose(self,wasClean,code,reason):
        print "Client left"
        ipStorage.dropConnection(self.peer.host) ##Drop Connection out of IPStorage when Client disconnects
        ipStorage.updateAll("Client with IP "+self.peer.host+" has disconnected")#Update all
         
    def onOpen(self):
        ipStorage.addNewClient(self.peer.host, self) ##adds current Connection and Client IP to the Storage
        ipStorage.sendMessageToOneIP(self.peer.host, str(self.peer.host))
        print "Client joined"
          
    def onMessage(self, msg, binary):
        self.sendMessage("Received: "+msg, binary)##send back message to initiating client
        msgList.append(msg)


if __name__ == '__main__':
    msgList = deque()
    ipStorage = IPStorage()
    resolution = avg.Player.get().getScreenResolution()
#     avg.Player.get().setWindowPos(0,0)
#     avg.Player.get().setWindowFrame(False)
#     Gui.start(resolution = resolution)
    Gui.start(resolution = (1400,800))