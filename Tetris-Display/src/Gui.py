from StoneGenerator import *
from libavg import AVGApp, avg
from TextRectNode import *
import time

class Gui(AVGApp):
    
    def __init__(self, ipStorage):
        self.keepCountingToStart = True
        self.modus = 0
        self.playerAmountRdy = 0
        self.player1 = ""
        self.player2 = ""
        self.player3 = ""
        self.player4 = ""
        self.connectedPlayers = 0
        self.playstyleModus = ""
        self.ipStorage = ipStorage
        self.divNodeMainMenue = None
        self.divNodelobbyMenue = None
        self.divNodeGameMenue = None
        
        self.player=avg.Player.get()
        self.canvas=self.player.createMainCanvas(size=(1440,900))
        self.rootNode=self.canvas.getRootNode()
    
        self.startMainMenue()
        
        
    def startMainMenue(self):
        self.divNodeMainMenue = avg.DivNode(parent = self.rootNode, size  = self.rootNode.size)
        self.background = avg.RectNode(parent = self.divNodeMainMenue, pos = (0,0), fillcolor = "0040FF", fillopacity = 1, color = "0040FF", size = self.divNodeMainMenue.size )  
        self.header = TextRectNode(parent = self.divNodeMainMenue, 
                                   pos = (0,0),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodeMainMenue.size[0],self.divNodeMainMenue.size[1]*0.25))
        self.header.addText("MultiTetris")
        
        self.buttonCreateGame = TextRectNode(parent = self.divNodeMainMenue, 
                                   pos = (self.divNodeMainMenue.size[0]*0.3,self.divNodeMainMenue.size[1]*0.25),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodeMainMenue.size[0]*0.25,self.divNodeMainMenue.size[1]*0.15))
        self.buttonCreateGame.addText("Create Game:")
        
        self.button1vs1 = TextRectNode(parent = self.divNodeMainMenue, 
                                   pos = (self.divNodeMainMenue.size[0]*0.40,self.divNodeMainMenue.size[1]*0.40),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeMainMenue.size[0]*0.15,self.divNodeMainMenue.size[1]*0.10))
        self.button1vs1.addText("1vs1")
         
        self.button2vs2 = TextRectNode(parent = self.divNodeMainMenue, 
                                   pos = (self.divNodeMainMenue.size[0]*0.40,self.divNodeMainMenue.size[1]*0.70),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeMainMenue.size[0]*0.15,self.divNodeMainMenue.size[1]*0.10))
        self.button2vs2.addText("2vs2")
        
        self.button1vs1vs1 = TextRectNode(parent = self.divNodeMainMenue, 
                                   pos = (self.divNodeMainMenue.size[0]*0.40,self.divNodeMainMenue.size[1]*0.55),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeMainMenue.size[0]*0.15,self.divNodeMainMenue.size[1]*0.10))
        self.button1vs1vs1.addText("1vs1vs1")
        
        self.button1vs1.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.button1vs1, self.onClickMain1v1)
        self.button2vs2.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.button2vs2, self.onClickMain2v2)
        self.button1vs1vs1.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.button1vs1vs1, self.onClickMain1v1v1)
    
        
    def startLobby(self, modus):
        self.modus = modus
        if(self.modus==2):
            self.playstyleModus = "1vs1"
            self.player1 = "Player 1"
            self.player2 = "Player 2"
        elif(self.modus == 3):
            self.playstyleModus = "1vs1vs1"
            self.player1 = "Defender"
            self.player2 = "Defender"
            self.player3 = "Attacker"
        elif(self.modus == 4):
            self.playstyleModus = "2vs2"
            self.player1 = "Defender"
            self.player2 = "Defender"
            self.player3 = "Attacker"
            self.player4 = "Attacker"
        else:
            raise SyntaxError("Falscher Modus in startlobby")
            
        self.divNodelobbyMenue = avg.DivNode(parent = self.rootNode, size  = self.rootNode.size)
        self.background = avg.RectNode(parent = self.divNodelobbyMenue, pos = (0,0), fillcolor = "0040FF", fillopacity = 1, color = "0040FF", size = self.divNodelobbyMenue.size )  
        self.gameName = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,0),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.07))
        self.gameName.addText("IP:   " + "TODO")
        
        self.playStyle = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2,0),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.07))
        self.playStyle.addText("Playstyle:   " + self.playstyleModus)
        
        self.port = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,self.divNodelobbyMenue.size[1]*0.07),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.07))
        self.port.addText("Port:   " + "TODO")
        
        self.numberPlayers = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.07),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.07))
        
        self.numberPlayers.addText("Players connected:   " + str(self.connectedPlayers)+"/"+ str(self.modus))
        
        self.teamOne = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,self.divNodelobbyMenue.size[1]*0.07+self.divNodelobbyMenue.size[1]*0.07),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.15))
        self.teamOne.addText("Team 1")
        
        self.teamTwo = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.07+self.divNodelobbyMenue.size[1]*0.07),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.15))
        self.teamTwo.addText("Team 2")
        
        aktuelleHoehe = self.divNodelobbyMenue.size[1]*0.07+self.divNodelobbyMenue.size[1]*0.07 + self.divNodelobbyMenue.size[1]*0.15
        
        if(self.modus != 3):
            self.firstPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.firstPlayer.addText(self.player1)
            
            self.secondPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.secondPlayer.addText(self.player2)
            
            aktuelleHoehe += self.divNodelobbyMenue.size[1]*0.35    
            
            self.thirdPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.thirdPlayer.addText(self.player3)
            
            self.forthPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.forthPlayer.addText(self.player4)
            
        else:
            self.firstPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.firstPlayer.addText(self.player1)
            
            self.secondPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.secondPlayer.addText(self.player2)
            
            aktuelleHoehe += self.divNodelobbyMenue.size[1]*0.35
            
            self.thirdPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/4,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.thirdPlayer.addText(self.player3)
            
        
#--------------------------------------test- kann geloescht werden--------------------------------------------------------------------------------------------------------------------------------
        self.firstPlayer.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.firstPlayer, self.test)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.endMainMenue()
        self.divNodelobbyMenue.active = True

    def gameCounter(self):
        count = 10
        print self.modus
        if(self.modus == 2):
            self.firstPlayer.active = False
            self.secondPlayer.active = False
        elif(self.modus == 3):
            print self.firstPlayer.active
            self.firstPlayer.active = False
            print self.firstPlayer.active
            self.secondPlayer.active = False
            self.thirdPlayer.active = False
        elif(self.modus == 4):
            self.firstPlayer.active = False
            self.secondPlayer.active = False
            self.thirdPlayer.active = False
            self.forthPlayer.active = False
        else:
            raise SyntaxError("Wrong Modus gameCounter")
            
        self.countNode = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/4,self.divNodelobbyMenue.size[1]*0.35   +  self.divNodelobbyMenue.size[1]*0.07+self.divNodelobbyMenue.size[1]*0.07 + self.divNodelobbyMenue.size[1]*0.15),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
        self.countNode.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.countNode, self.interruptCount)
        while(count>=0 & self.keepCountingToStart ):
            print count
            self.gameName.addText("Gamestart: "+ str(count))
            count-=1
            time.sleep(1)
        if(self.keepCountingToStart):
            self.initGame()   
    
    def initGame(self):
        print "Game Can Start now"
        self.endLobby()
    
    def updatePlayerName(self):
        #self.player1-4 om startlobby text updaten der rectnodes
        pass
    
    
    def playerGotRdy(self):
        self.playerAmountRdy+=1
        if(self.playerAmountRdy == self.modus):
            self.gameCounter()
        
    def updatePlayerLeft(self):
        self.connectedPlayers-=1
        self.numberPlayers.updateTextNode("Players connected:   " + str(self.connectedPlayers)+"/"+ str(self.modus))
    
    
    def updateJoinedPlayerNumber(self):
        self.connectedPlayers+=1
        if(self.connectedPlayers>self.modus):
            self.connectedPlayers-=1
            raise SyntaxError("Mehr Spieler als erlaubt; updateJoinedPlayerNumber")
        
        self.numberPlayers.updateTextNode("Players connected:   " + str(self.connectedPlayers)+"/"+ str(self.modus))
    
    
#-----------------------------------------------Interaction with App/socket------------------------------------------------------------------------------------------------------------------
    
    
    
    def eventHandler(self):
        pass
    
    
    
    
    
    
    
#-------------------------------------------------MenuesOffSwitches--------------------------------------------------------------------------------------------------------------------------
        
    def endMainMenue(self):
        self.divNodeMainMenue.active = False
    
    def endLobby(self):
        self.divNodelobbyMenue.active = False
    
    def endGame(self):
        self.divNodeGameMenue = False
    
    
    def test(self, event):  ## <<-----------------loeschbar nur zum counter test
        self.gameCounter()
    
#----------------------------------------------------------EventHandler-----------------------------------------------------------------------------------------------------------------------
    
    def onClickMain1v1(self, event):
        self.startLobby(2)
        
    def onClickMain1v1v1(self, event):
        self.startLobby(3)    
    
    def onClickMain2v2(self, event):
        self.startLobby(4)
        
    def interruptCount(self, event):
        self.keepCountingToStart = False
        
#-----------------------------------------------------------Erinnerungen was noch zutun ist---------------------------------------------------------------------------------------------------   

    def newGame(self):
        pass
    
    def getRdy (self):
        pass
    
    def movePlayer(self):
        pass
    
    def setRole(self):
        pass
    
    def showFields(self):
        pass
    
    def startNewRound(self):
        pass
    
    def speedUp(self):
        pass
    
    def updateScore(self):
        pass
    
    def pause(self):
        pass
    
    def initMainMenu(self):
        pass
    
    def initLobbyConcept(self):
        pass
    
    def initFields(self):
        pass
    
    def gravity (self, value):
        pass
    
    def newFallingStone(self):
        pass
    
    def timer(self):
        pass
    
    def stoneGenerator(self):
        pass
    
    def rotateLeft(self):
        pass
    
    def rotateRight(self):
        pass
    
    def dropDownFast(self):
        pass
    
    def hitGround(self):
        pass
    
    def usedSkill(self):
        pass
    
    def usedSpecialSkill(self):
        pass
    
    def moveBlockLeft(self):
        pass
    
    def moveBlockRight(self):
        pass
    
    def alertNotEnoughMoney(self):
        pass
    
    def hitSide(self):
        pass
    
    def updateClock(self):
        pass
    
    def updateCds(self):
        pass
    
    def chanceLevel(self):
        pass
    