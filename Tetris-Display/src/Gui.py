from libavg import AVGApp
from TextRectNode import *
import socket


class Gui(AVGApp):
    
    def __init__(self, ipStorage):
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
        self.blocksize = 0   
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
        
                                
                            
        
#-----------------------------------------------Main Menu-------------------------------------------------------------------------------------------------------------------------------      
    
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
        self.button1vs1.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.button1vs1, self.onClickMain1v1)
        self.button2vs2.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.button2vs2, self.onClickMain2v2)
        self.button1vs1vs1.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.button1vs1vs1, self.onClickMain1v1v1)
        
        
    
#-----------------------------------------------Lobby Menue--------------------------------------------------------------------------------------------------------------------------        


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
            
        self.divNodelobbyMenue = avg.DivNode(parent = self.rootNode, size  = self.rootNode.size, active = False)
        self.background = avg.RectNode(parent = self.divNodelobbyMenue, pos = (0,0), fillcolor = "0040FF", fillopacity = 1, color = "0040FF", size = self.divNodelobbyMenue.size )  
        
        self.gameName = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,0),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2.4,self.divNodelobbyMenue.size[1]*0.07))
        self.gameName.addTextForLobbyLine("IP:",socket.gethostbyname(socket.gethostname()))
        
        self.port = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,self.divNodelobbyMenue.size[1]*0.07),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2.4,self.divNodelobbyMenue.size[1]*0.07))
        self.port.addTextForLobbyLine("Port:" , "55555")
        
        self.playStyle = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0] - self.divNodelobbyMenue.size[0]/2.4 ,0),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2.4,self.divNodelobbyMenue.size[1]*0.07))
        self.playStyle.addTextForLobbyLine("Playstyle:" , self.playstyleModus)
        
        self.numberPlayers = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0] - self.divNodelobbyMenue.size[0]/2.4,self.divNodelobbyMenue.size[1]*0.07),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2.4,self.divNodelobbyMenue.size[1]*0.07))
        
        self.numberPlayers.addTextForLobbyLine("Players connected:", str(self.connectedPlayers)+"/"+ str(self.modus))
        
        self.backButton =  TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2.4,0),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(2*(self.divNodelobbyMenue.size[0]/2- self.divNodelobbyMenue.size[0]/2.4), self.divNodelobbyMenue.size[1]*0.14))
        self.backButton.addTextForBackButton("Back")
        
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
        
        if(self.modus == 4):
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
        
        elif(self.modus == 2):
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
            
        
#--------------------------------------test- kann geloescht werden----------------------------------------------------------------------------------------------------------------------------
        self.firstPlayer.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.firstPlayer, self.test)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.backButton.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.backButton, self.backToMenue)
        self.endMainMenue()
        self.divNodelobbyMenue.active = True
        
        
#-----------------------------------------------Lobby Methoden----------------------------------------------------------------------------------------------------------------------------
    
    def gameCounter(self):
        self.count = 9
        if(self.modus == 2):
            self.firstPlayer.setInactiv()
            self.secondPlayer.setInactiv()
        elif(self.modus == 3):
            self.firstPlayer.setInactiv()
            self.secondPlayer.setInactiv()
            self.thirdPlayer.setInactiv()
        elif(self.modus == 4):
            self.firstPlayer.setInactiv()
            self.secondPlayer.setInactiv()
            self.thirdPlayer.setInactiv()
            self.forthPlayer.setInactiv()
        else:
            raise SyntaxError("Wrong Modus gameCounter")
         
        self.countNode = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/4,self.divNodelobbyMenue.size[1]*0.45),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
        self.countNode.addText("Gamestart: "+ str(self.count), "000000")  
        self.countNode.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.countNode, self.interruptCount)
        self.timer = self.player.setInterval(1000, self.countCount)
        self.gameStartTimer = self.player.setInterval(10000, self.maybeStart)
        
        
    def maybeStart(self):
        self.player.clearInterval(self.gameStartTimer)
        self.player.clearInterval(self.timer)
        self.countNode.setInactiv()
        if(self.keepCountingToStart):
            self.initGame()
             
        elif(self.modus == 2):
            self.divNodelobbyMenue.active = True
            self.firstPlayer.setActiv()
            self.secondPlayer.setActiv()
        elif(self.modus == 3):
            self.divNodelobbyMenue.active = True
            self.firstPlayer.setActiv()
            self.secondPlayer.setActiv()
            self.thirdPlayer.setActiv()
        elif(self.modus == 4):
            self.divNodelobbyMenue.active = True
            self.firstPlayer.setActiv()
            self.secondPlayer.setActiv()
            self.thirdPlayer.setActiv()
            self.forthPlayer.setActiv()
        else:
            raise SyntaxError("Wrong Modus gameCounter")
        
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
    
    def countCount(self):
        self.count -=1
        self.countNode.updateTextNode("Gamestart: "+ str(self.count))
        
    def updateJoinedPlayerNumber(self):
        self.connectedPlayers+=1
        if(self.connectedPlayers>self.modus):
            self.connectedPlayers-=1
            raise SyntaxError("Mehr Spieler als erlaubt; updateJoinedPlayerNumber")
        
        self.numberPlayers.updateTextNode("Players connected:   " + str(self.connectedPlayers)+"/"+ str(self.modus))
        
      
#-----------------------------------------------Tetris Feld -----------------------------------------------------------------------------------------------------------------------------     
    
    def initGame(self):
        self.divNodeGameMenue= avg.DivNode(parent = self.rootNode, size  = self.rootNode.size, active = False)
        self.background = avg.RectNode(parent = self.divNodeGameMenue, pos = (0,0), fillcolor = "0040FF", fillopacity = 1, color = "0040FF", size = self.divNodeGameMenue.size )
        xstartFeld1 = self.divNodeGameMenue.size[0] * 0.02
        xendFeld1   = self.divNodeGameMenue.size[0] * 0.45
        xstartFeld2 = self.divNodeGameMenue.size[0]/2 + self.divNodeGameMenue.size[0] *0.05
        xendFeld2   = self.divNodeGameMenue.size[0] - self.divNodeGameMenue.size[0] * 0.02
        self.blocksize = ((xendFeld1 - self.divNodeGameMenue.size[0]*0.025) - (xstartFeld1 + self.divNodeGameMenue.size[0]*0.025))/14
        self.tetrishoehe = self.blocksize * 20
        self.initFeld(xstartFeld1, xendFeld1)
        self.initFeld(xstartFeld2, xendFeld2)
        
        self.timelimit =  avg.WordsNode(pos = (xendFeld1 + (xstartFeld2 - xendFeld1)/2 , self.divNodeGameMenue.size[1] * 0.20),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="TimeLimit", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        self.timerLimit = avg.WordsNode(pos = (xendFeld1 + (xstartFeld2 - xendFeld1)/2 , self.divNodeGameMenue.size[1] * 0.23),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="500", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
        self.timeLimitCounter = self.player.setInterval(1000, self.timerLCountDown)
        
        self.roundText = avg.WordsNode(pos = (xendFeld1 + (xstartFeld2 - xendFeld1)/2 , self.divNodeGameMenue.size[1] * 0.33),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="Round", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
        self.roundNumber = avg.WordsNode(pos = (xendFeld1 + (xstartFeld2 - xendFeld1)/2 , self.divNodeGameMenue.size[1] * 0.36),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="1", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
        self.speedText = avg.WordsNode(pos = (xendFeld1 + (xstartFeld2 - xendFeld1)/2 , self.divNodeGameMenue.size[1] * 0.46),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="Speed", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
        self.speedNumber = avg.WordsNode(pos = (xendFeld1 + (xstartFeld2 - xendFeld1)/2 , self.divNodeGameMenue.size[1] * 0.49),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="1", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
        self.scoreTeam1 = avg.WordsNode(pos = ((xstartFeld1 + xendFeld1)/2 , self.divNodeGameMenue.size[1] * 0.96),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="Score:  000000", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
        self.scoreTeam2 = avg.WordsNode(pos = ((xstartFeld2 + xendFeld2)/2 , self.divNodeGameMenue.size[1] * 0.96),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="Score:  000000",  
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
       
        self.linksFeld1X   = xstartFeld1 + self.divNodeGameMenue.size[0]*0.025
        self.rechtsFeld1X  = xendFeld1 -self.divNodeGameMenue.size[0]*0.025
        
        self.linksFeld2X   = xstartFeld2 + self.divNodeGameMenue.size[0]*0.025
        self.rechtsFeld2X  = xendFeld2 -self.divNodeGameMenue.size[0]*0.025
 
        self.yOben = self.divNodeGameMenue.size[1] * 0.03
        self.yUnten =  self.yOben + self.tetrishoehe
        
        print "Blocksize: ", self.blocksize
        print "Tetrisfeldbegrenzungen:   lX1:",self.linksFeld1X,"  rF1: ",self.rechtsFeld1X,"   lF2: ",self.linksFeld2X,"  rF2:  ",self.rechtsFeld2X,"  yO: ", self.yOben," yU: ", self.yUnten
        
        
        self.test = avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (self.linksFeld1X, self.yOben), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.blocksize ,self.blocksize)
                                  )
       
        self.endLobby()
        self.divNodeGameMenue.active = True
        
        
    def initFeld (self, startX, endX):
#linker Rahmen
        avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (startX , self.divNodeGameMenue.size[1] * 0.03), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.divNodeGameMenue.size[0]*0.025 ,self.tetrishoehe) #self.divNodeGameMenue.size[1]* 0.87
                                  )
#rechter Rahmen
        avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (endX - self.divNodeGameMenue.size[0]*0.025 , self.divNodeGameMenue.size[1] * 0.03), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.divNodeGameMenue.size[0]*0.025, self.tetrishoehe)
                                  )
#Boden
        avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (startX, self.tetrishoehe+self.divNodeGameMenue.size[1] * 0.03), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(endX - startX ,self.divNodeGameMenue.size[1]*0.04)
                                  )
    
    
    
    
    
#-----------------------------------------------Interaction with App/socket--------------------------------------------------------------------------------------------------------------

    
    
    def eventHandler(self):
        self.initGame()
        self.test   = avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (200, 200), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.blocksize ,self.blocksize)
                                  )
    
    
    
    
    
#---------------------------------------------------Tetris Spiel Berechnungen-------------------------------------------------------------------------------------------------------------  

    
    
#-------------------------------------------------MenuesOffSwitches-----------------------------------------------------------------------------------------------------------------------
        
    def endMainMenue(self):
        self.divNodeMainMenue.active = False
    
    def endLobby(self):
        self.divNodelobbyMenue.active = False
    
    def endGame(self):
        self.divNodeGameMenue = False
    
    
    def test(self, event):  ## <<-----------------loeschbar nur zum counter test
        self.initGame()
    
    
#----------------------------------------------------------EventHandler-----------------------------------------------------------------------------------------------------------------
    
    def onClickMain1v1(self, event):
        self.startLobby(2)
        
    def onClickMain1v1v1(self, event):
        self.startLobby(3)    
    
    def onClickMain2v2(self, event):
        self.startLobby(4)
        
    def backToMenue(self, event):
        self.endLobby()
        self.divNodeMainMenue.active = True
        self.ipStorage.getAllCurrentConnections()
        for ip in self.ipStorage.getAllCurrentConnections():
            self.ipStorage.dropConnection(ip)
        
    def interruptCount(self, event):
        self.keepCountingToStart = False
        self.maybeStart()
        
    def timerLCountDown (self):
        count = int (self.timerLimit.text)
        count -= 1
        self.timerLimit.text = str(count)
#-----------------------------------------------------------Eventuell unnuetz: Notfall fuer IP Mac Probleme-------------------------------------------------------------------------------   

# import os
# 
# import socket
# 
# if os.name != "nt":
# 
#     import fcntl
# 
#     import struct
# 
#     def get_interface_ip(ifname):
# 
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 
#         return socket.inet_ntoa(fcntl.ioctl(
# 
#                 s.fileno(),
# 
#                 0x8915,  # SIOCGIFADDR
# 
#                 struct.pack('256s', ifname[:15])
# 
#             )[20:24])
# 
# 
# 
# def get_lan_ip():
# 
#     ip = socket.gethostbyname(socket.gethostname())
# 
#     if ip.startswith("127.") and os.name != "nt":
# 
#         interfaces = ["eth0","eth1","eth2","wlan0","wlan1","wifi0","ath0","ath1","ppp0"]
# 
#         for ifname in interfaces:
# 
#             try:
# 
#                 ip = get_interface_ip(ifname)
# 
#                 break;
# 
#             except IOError:
# 
#                 pass
# 
#     return ip
#-----------------------------------------------------------Erinnerungen was noch zutun ist-----------------------------------------------------------------------------------------------
   
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
    