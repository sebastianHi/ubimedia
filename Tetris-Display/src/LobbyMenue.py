from libavg import avg
from TextRectNode import TextRectNode
import socket

class LobbyMenue(object):
    
    def __init__(self, parent, modus,gui,kind):
        
#####################################################################################
#        player[0] ist immer Defender Feld 1
#        player[1] ist immer Defender Feld 2
#        player[2] ist immer Attacker fuer Team Feld1
#        player[3] ist immer Attacker fuer Team Feld2
#####################################################################################
       
        self.gui = gui
        self.typ = 0
        if(kind == 1):
            self.typ = 1
            
        self.rootNode = parent
        self.player = ["","","",""]
        self.playerIP = ["","","",""]
        self.rdyPlayer = [False,False,False,False]
        self.rectNodPlayerArr = [None,None,None,None]
        self.connectedPlayers = 0
        self.oldPos = None
        self.playstyleModus = ""
        self.modus = modus
        if(self.modus==2):
            self.playstyleModus = "1vs1"
            self.player[0] = "Defender"
            self.player[1] = "Defender"
        elif(self.modus == 3):
            self.playstyleModus = "1vs1vs1"
            self.player[0] = "Defender"
            self.player[1] = "Defender"
            self.player[2] = "Attacker"
        elif(self.modus == 4):
            self.playstyleModus = "2vs2"
            self.player[0] = "Defender"
            self.player[1] = "Defender"
            self.player[2] = "Attacker"
            self.player[3] = "Attacker"
        else:
            raise SyntaxError("Falscher Modus in startlobby")
            
        
        self.divNodelobbyMenue = avg.DivNode(parent = self.rootNode, size  = self.rootNode.size, active = False)
        self.background = avg.RectNode(parent = self.divNodelobbyMenue, pos = (0,0), fillcolor = "0040FF", fillopacity = 1, color = "0040FF", size = self.divNodelobbyMenue.size )  
        
        self.gameName = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,self.divNodelobbyMenue.size[1]*0.07),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2.4,self.divNodelobbyMenue.size[1]*0.07))
        self.gameName.addTextForLobbyLine("IP:",socket.gethostbyname(socket.gethostname()))
        
        self.type = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,0),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2.4,self.divNodelobbyMenue.size[1]*0.07))
        if(self.typ == 0):
            self.type.addTextForLobbyLine("Type:" , "Classic")
        else:
            self.type.addTextForLobbyLine("Type:" , "EqualMode")
        
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
        
#----------------------------------------------Player Felder------------------------------------------------------------------------------------------------------------------------- 
        if(self.modus == 4):
            self.firstPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.firstPlayer.addText(self.player[0])
            
            self.secondPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.secondPlayer.addText(self.player[1])
            
            aktuelleHoehe += self.divNodelobbyMenue.size[1]*0.35    
            
            self.thirdPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.thirdPlayer.addText(self.player[2])
            
            self.forthPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.forthPlayer.addText(self.player[3])
            
            self.rectNodPlayerArr = [self.firstPlayer,self.secondPlayer,self.thirdPlayer,self.forthPlayer]
#----Eventhandler fuer player swap ------------------------------------------------------------------------------------------------------------------------------------------------------
            self.firstPlayer.connectEventHandler(avg.CURSORDOWN,avg.TOUCH, self.firstPlayer, self.onMouseDown)
            self.firstPlayer.connectEventHandler(avg.CURSORMOTION,avg.TOUCH, self.firstPlayer, self.onMouseMove)
            self.firstPlayer.connectEventHandler(avg.CURSORUP,avg.TOUCH, self.firstPlayer, self.onMouseUp)
            self.secondPlayer.connectEventHandler(avg.CURSORDOWN,avg.TOUCH, self.secondPlayer, self.onMouseDown)
            self.secondPlayer.connectEventHandler(avg.CURSORMOTION,avg.TOUCH, self.secondPlayer, self.onMouseMove)
            self.secondPlayer.connectEventHandler(avg.CURSORUP,avg.TOUCH, self.secondPlayer, self.onMouseUp)
            self.thirdPlayer.connectEventHandler(avg.CURSORDOWN,avg.TOUCH, self.thirdPlayer, self.onMouseDown)
            self.thirdPlayer.connectEventHandler(avg.CURSORMOTION,avg.TOUCH, self.thirdPlayer, self.onMouseMove)
            self.thirdPlayer.connectEventHandler(avg.CURSORUP,avg.TOUCH, self.thirdPlayer, self.onMouseUp)
            self.forthPlayer.connectEventHandler(avg.CURSORDOWN,avg.TOUCH, self.forthPlayer, self.onMouseDown)
            self.forthPlayer.connectEventHandler(avg.CURSORMOTION,avg.TOUCH, self.forthPlayer, self.onMouseMove)
            self.forthPlayer.connectEventHandler(avg.CURSORUP,avg.TOUCH, self.forthPlayer, self.onMouseUp)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        elif(self.modus == 2):
            self.firstPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.firstPlayer.addText(self.player[0])
            
            self.secondPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.secondPlayer.addText(self.player[1])
            
            self.rectNodPlayerArr = [self.firstPlayer,self.secondPlayer]
#----Eventhandler fuer player swap ------------------------------------------------------------------------------------------------------------------------------------------------------
            self.firstPlayer.connectEventHandler(avg.CURSORDOWN,avg.MOUSE, self.firstPlayer, self.onMouseDown)
            self.firstPlayer.connectEventHandler(avg.CURSORMOTION,avg.MOUSE, self.firstPlayer, self.onMouseMove)
            self.firstPlayer.connectEventHandler(avg.CURSORUP,avg.MOUSE, self.firstPlayer, self.onMouseUp)
            self.secondPlayer.connectEventHandler(avg.CURSORDOWN,avg.MOUSE, self.secondPlayer, self.onMouseDown)
            self.secondPlayer.connectEventHandler(avg.CURSORMOTION,avg.MOUSE, self.secondPlayer, self.onMouseMove)
            self.secondPlayer.connectEventHandler(avg.CURSORUP,avg.MOUSE, self.secondPlayer, self.onMouseUp)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
            
        else:
            self.firstPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.firstPlayer.addText(self.player[0])
            
            self.secondPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.secondPlayer.addText(self.player[1])
            
            aktuelleHoehe += self.divNodelobbyMenue.size[1]*0.35
            
            self.thirdPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/4,aktuelleHoehe),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.thirdPlayer.addText(self.player[2])
            
            self.rectNodPlayerArr = [self.firstPlayer,self.secondPlayer,self.thirdPlayer]
            
#----Eventhandler fuer player swap ------------------------------------------------------------------------------------------------------------------------------------------------------
            self.firstPlayer.connectEventHandler(avg.CURSORDOWN,avg.TOUCH, self.firstPlayer, self.onMouseDown)
            self.firstPlayer.connectEventHandler(avg.CURSORMOTION,avg.TOUCH, self.firstPlayer, self.onMouseMove)
            self.firstPlayer.connectEventHandler(avg.CURSORUP,avg.TOUCH, self.firstPlayer, self.onMouseUp)
            self.secondPlayer.connectEventHandler(avg.CURSORDOWN,avg.TOUCH, self.secondPlayer, self.onMouseDown)
            self.secondPlayer.connectEventHandler(avg.CURSORMOTION,avg.TOUCH, self.secondPlayer, self.onMouseMove)
            self.secondPlayer.connectEventHandler(avg.CURSORUP,avg.TOUCH, self.secondPlayer, self.onMouseUp)
            self.thirdPlayer.connectEventHandler(avg.CURSORDOWN,avg.TOUCH, self.thirdPlayer, self.onMouseDown)
            self.thirdPlayer.connectEventHandler(avg.CURSORMOTION,avg.TOUCH, self.thirdPlayer, self.onMouseMove)
            self.thirdPlayer.connectEventHandler(avg.CURSORUP,avg.TOUCH, self.thirdPlayer, self.onMouseUp)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
     
            
    def onMouseDown(self, event):
        node = event.node
        if(self.modus == 4):
            if(node != self.firstPlayer):
                self.firstPlayer.sensitive = False
            if(node != self.secondPlayer):
                self.secondPlayer.sensitive = False
            if(node != self.thirdPlayer):
                self.thirdPlayer.sensitive = False
            if(node != self.forthPlayer):
                self.forthPlayer.sensitive = False
        elif(self.modus == 3):
            if(node != self.firstPlayer):
                self.firstPlayer.sensitive = False
            if(node != self.secondPlayer):
                self.secondPlayer.sensitive = False
            if(node != self.thirdPlayer):
                self.thirdPlayer.sensitive = False
        elif(self.modus == 2):
            if(node != self.firstPlayer):
                self.firstPlayer.sensitive = False
            if(node != self.secondPlayer):
                self.secondPlayer.sensitive = False
            
        self.oldPos = node.pos
        node.setEventCapture()

    def onMouseMove(self, event):
        node = event.node
        if self.oldPos != None:
            node.pos = event.pos

    def onMouseUp(self, event):
        node = event.node
        if(self.modus == 4):
            if(node != self.firstPlayer):
                self.firstPlayer.sensitive = True
            if(node != self.secondPlayer):
                self.secondPlayer.sensitive = True
            if(node != self.thirdPlayer):
                self.thirdPlayer.sensitive = True
            if(node != self.forthPlayer):
                self.forthPlayer.sensitive = True
        elif(self.modus == 3):
            if(node != self.firstPlayer):
                self.firstPlayer.sensitive = True
            if(node != self.secondPlayer):
                self.secondPlayer.sensitive = True
            if(node != self.thirdPlayer):
                self.thirdPlayer.sensitive = True
        elif(self.modus == 2):
            if(node != self.firstPlayer):
                self.firstPlayer.sensitive = True
            if(node != self.secondPlayer):
                self.secondPlayer.sensitive = True
                
        if self.oldPos != None:
            node.releaseEventCapture()
            self.swapPlayer(node.pos)
            node.pos = self.oldPos
            print self.oldPos
            self.oldPos = None

       
    def swapPlayer(self,offset):
        pass#TODO:
#         if(self.modus == 4):
#             if((self.firstPlayer.pos[0]+self.firstPlayer.size[0]))
    
    def playerNotRdyAnylonge(self,ip):
        i = 0
        for i in range(self.modus):
            if(ip == self.playerIP[i]):
                self.rdyPlayer[i] = False
                break
 
    def playerGotRdy(self,ip):
        i = -1
        for k in self.playerIP:
            i+=1
            if(k == ip):
                self.rdyPlayer[i] = True
                break
        p = True
        for b in range(0,self.modus):
            p = (p) and (self.rdyPlayer[b])
        if p:
            self.gui.gameCounter()
            
            
    def playerStopBeingRdy(self,ip):
        i = 0
        for k in self.playerIP:
            if(k == ip):
                break
            i+=1
        self.rdyPlayer[i] = False
        
         
    def updatePlayerLeft(self, ip):#TODO:
        self.connectedPlayers-=1
        self.numberPlayers.updateTextForLobbyLine( "Players connected:", str(self.connectedPlayers)+"/"+ str(self.modus))
        i = 0
        b = False
        for i in range(self.modus):
            if(self.playerIP[i] == ip):
                if(i+1 < self.modus):
                    if((self.player[i+1] != "Attacker") | (self.player[i+1] != "Defender") ):
                        self.player[i] = self.player[i+1]
                        self.playerIP[i] = self.playerIP[i+1]
                        self.rdyPlayer[i] = False 
                        (self.rectNodPlayerArr[i]).updateTextNode(self.player[i]) 
                    else:
                        if((i == 0) | (i == 1)):
                            self.player[i] = "Defender"
                            self.playerIP[i] = ""
                            self.rdyPlayer[i] = False 
                            (self.rectNodPlayerArr[i]).updateTextNode("Defender") 
                        else:
                            self.player[i] = "Attacker"
                            self.playerIP[i] = ""
                            self.rdyPlayer[i] = False 
                            (self.rectNodPlayerArr[i]).updateTextNode("Attacker")
                else:
                    if((i == 0) | (i == 1)):
                        self.player[i] = "Defender"
                        self.playerIP[i] = ""
                        self.rdyPlayer[i] = False 
                        (self.rectNodPlayerArr[i]).updateTextNode("Defender") 
                    else:
                        self.player[i] = "Attacker"
                        self.playerIP[i] = ""
                        self.rdyPlayer[i] = False 
                        (self.rectNodPlayerArr[i]).updateTextNode("Attacker")
                b = True
            else:
                if(b):
                    if(i+1 < self.modus):
                        if((self.player[i+1] != "Attacker") | (self.player[i+1] != "Defender") ):
                            self.player[i] = self.player[i+1]
                            self.playerIP[i] = self.playerIP[i+1]
                            self.rdyPlayer[i] = False 
                            (self.rectNodPlayerArr[i]).updateTextNode(self.player[i]) 
                        else:
                            if((i == 0) | (i == 1)):
                                self.player[i] = "Defender"
                                self.playerIP[i] = ""
                                self.rdyPlayer[i] = False 
                                (self.rectNodPlayerArr[i]).updateTextNode("Defender") 
                            else:
                                self.player[i] = "Attacker"
                                self.playerIP[i] = ""
                                self.rdyPlayer[i] = False 
                                (self.rectNodPlayerArr[i]).updateTextNode("Attacker")
           
        self.gui.sendMsgToAll("notRdy")
        
        
    def updateJoinedPlayerNumber(self, ip, name):
        if(self.connectedPlayers+1>self.modus):
            raise SyntaxError("Mehr Spieler als erlaubt; updateJoinedPlayerNumber")
        else:
            self.numberPlayers.updateTextForLobbyLine( "Players connected:", str(self.connectedPlayers+1)+"/"+ str(self.modus))
            self.player[self.connectedPlayers] = name
            (self.rectNodPlayerArr[self.connectedPlayers]).updateTextNode(name)
            self.playerIP[self.connectedPlayers] = ip
            self.connectedPlayers+=1
            print self.playerIP[0],self.playerIP[1],self.playerIP[2],self.playerIP[3]
            