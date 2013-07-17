from libavg import avg,ui
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
        self.whoToSwap = -1
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
        self.background = avg.ImageNode(parent = self.divNodelobbyMenue, href = "DatBG.png", size = self.divNodelobbyMenue.size)
            
        self.gameName = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,self.divNodelobbyMenue.size[1]*0.07),
                                   href = "DatBG.png",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2.4,self.divNodelobbyMenue.size[1]*0.07))
        self.gameName.addTextForLobbyLine("IP:",socket.gethostbyname(socket.gethostname()))
        
        self.type = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,0),
                                   href = "DatBG.png",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2.4,self.divNodelobbyMenue.size[1]*0.07))
        if(self.typ == 0):
            self.type.addTextForLobbyLine("Type:" , "Classic")
        else:
            self.type.addTextForLobbyLine("Type:" , "EqualMode")
        
        self.playStyle = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0] - self.divNodelobbyMenue.size[0]/2.4 ,0),
                                   href = "DatBG.png",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2.4,self.divNodelobbyMenue.size[1]*0.07))
        self.playStyle.addTextForLobbyLine("Playstyle:" , self.playstyleModus)
        
        self.numberPlayers = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0] - self.divNodelobbyMenue.size[0]/2.4,self.divNodelobbyMenue.size[1]*0.07),
                                   href = "DatBG.png",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2.4,self.divNodelobbyMenue.size[1]*0.07))
        
        self.numberPlayers.addTextForLobbyLine("Players connected:", str(self.connectedPlayers)+"/"+ str(self.modus))
        
        self.backButton =  TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2.4,0),
                                   href = "DatBG.png",
                                   size = avg.Point2D(2*(self.divNodelobbyMenue.size[0]/2- self.divNodelobbyMenue.size[0]/2.4), self.divNodelobbyMenue.size[1]*0.14))
        self.backButton.addTextForBackButton("Back")
        
        self.teamOne = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,self.divNodelobbyMenue.size[1]*0.07+self.divNodelobbyMenue.size[1]*0.07),
                                   href = "DatBG.png",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.15))
        self.teamOne.addText("Team 1")
        
        self.teamTwo = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.07+self.divNodelobbyMenue.size[1]*0.07),
                                   href = "DatBG.png",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.15))
        self.teamTwo.addText("Team 2")
        
        aktuelleHoehe = self.divNodelobbyMenue.size[1]*0.07+self.divNodelobbyMenue.size[1]*0.07 + self.divNodelobbyMenue.size[1]*0.15
        
#----------------------------------------------Player Felder------------------------------------------------------------------------------------------------------------------------- 
        if(self.modus == 4):
            self.firstPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,aktuelleHoehe),
                                   href = "DatBG.png",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.firstPlayer.addText(self.player[0])
            
            self.secondPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2,aktuelleHoehe),
                                   href = "DatBG.png",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.secondPlayer.addText(self.player[1])
            
            aktuelleHoehe += self.divNodelobbyMenue.size[1]*0.35    
            
            self.thirdPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,aktuelleHoehe),
                                   href = "DatBG.png",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.thirdPlayer.addText(self.player[2])
            
            self.forthPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2,aktuelleHoehe),
                                   href = "DatBG.png",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.forthPlayer.addText(self.player[3])
            
            self.rectNodPlayerArr = [self.firstPlayer,self.secondPlayer,self.thirdPlayer,self.forthPlayer]
            
            self.firstPlayer.connectEventHandler(avg.CURSORDOWN, avg.TOUCH,self.firstPlayer,  self.onClick )
            self.secondPlayer.connectEventHandler(avg.CURSORDOWN, avg.TOUCH,self.secondPlayer,  self.onClick )
            self.thirdPlayer.connectEventHandler(avg.CURSORDOWN, avg.TOUCH,self.thirdPlayer,  self.onClick )


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        elif(self.modus == 2):
            self.firstPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,aktuelleHoehe),
                                   href = "DatBG.png",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.firstPlayer.addText(self.player[0])
            
            self.secondPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2,aktuelleHoehe),
                                   href = "DatBG.png",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.secondPlayer.addText(self.player[1])
            
            self.rectNodPlayerArr = [self.firstPlayer,self.secondPlayer]
            
            self.firstPlayer.connectEventHandler(avg.CURSORDOWN, avg.TOUCH,self.firstPlayer,  self.onClick )
            self.secondPlayer.connectEventHandler(avg.CURSORDOWN, avg.TOUCH,self.secondPlayer,  self.onClick )

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
            
        else:
            self.firstPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (0,aktuelleHoehe),
                                   href = "DatBG.png",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.firstPlayer.addText(self.player[0])
            
            self.secondPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/2,aktuelleHoehe),
                                   href = "DatBG.png",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.secondPlayer.addText(self.player[1])
            
            aktuelleHoehe += self.divNodelobbyMenue.size[1]*0.35
            
            self.thirdPlayer = TextRectNode(parent = self.divNodelobbyMenue, 
                                   pos = (self.divNodelobbyMenue.size[0]/4,aktuelleHoehe),
                                   href = "DatBG.png",
                                   size = avg.Point2D(self.divNodelobbyMenue.size[0]/2,self.divNodelobbyMenue.size[1]*0.35))
            self.thirdPlayer.addText(self.player[2])
            
            self.rectNodPlayerArr = [self.firstPlayer,self.secondPlayer,self.thirdPlayer]
            
            self.firstPlayer.connectEventHandler(avg.CURSORDOWN, avg.TOUCH,self.firstPlayer,  self.onClick )
            self.secondPlayer.connectEventHandler(avg.CURSORDOWN, avg.TOUCH,self.secondPlayer,  self.onClick )
            self.thirdPlayer.connectEventHandler(avg.CURSORDOWN, avg.TOUCH,self.thirdPlayer,  self.onClick )
            self.forthPlayer.connectEventHandler(avg.CURSORDOWN, avg.TOUCH,self.forthPlayer,  self.onClick )

 
    def onClick(self,event):
        if(self.whoToSwap == -1):
            if(self.modus == 2):
                if(event.node == self.firstPlayer):
                    self.whoToSwap = 0
                elif(event.node == self.secondPlayer):
                    self.whoToSwap = 1
                else:
                    raise SyntaxError ("Wtf")
                
            elif(self.modus == 3):
                if(event.node == self.firstPlayer):
                    self.whoToSwap = 0
                elif(event.node == self.secondPlayer):
                    self.whoToSwap = 1
                elif(event.node == self.thirdPlayer):
                    self.whoToSwap = 2
                else:
                    raise SyntaxError ("Wtf")
                
            elif(self.modus == 4):
                if(event.node == self.firstPlayer):
                    self.whoToSwap = 0
                elif(event.node == self.secondPlayer):
                    self.whoToSwap = 1
                elif(event.node == self.thirdPlayer):
                    self.whoToSwap = 2
                elif(event.node == self.forthPlayer):
                    self.whoToSwap = 3
                else:
                    raise SyntaxError ("Wtf")
            else:
                raise SyntaxError ("Wtf")
        else:
            if(self.modus == 2):
                if(event.node == self.firstPlayer):
                    self.swapPlayer(self.whoToSwap, 0)
                    self.whoToSwap = -1
                elif(event.node == self.secondPlayer):
                    self.swapPlayer(self.whoToSwap, 1)
                    self.whoToSwap = -1
                else:
                    raise SyntaxError ("Wtf")
                
            elif(self.modus == 3):
                if(event.node == self.firstPlayer):
                    self.swapPlayer(self.whoToSwap, 0)
                    self.whoToSwap = -1
                elif(event.node == self.secondPlayer):
                    self.swapPlayer(self.whoToSwap, 1)
                    self.whoToSwap = -1
                elif(event.node == self.thirdPlayer):
                    self.swapPlayer(self.whoToSwap, 2)
                    self.whoToSwap = -1
                else:
                    raise SyntaxError ("Wtf")
                
            elif(self.modus == 4):
                if(event.node == self.firstPlayer):
                    self.swapPlayer(self.whoToSwap, 0)
                    self.whoToSwap = -1
                elif(event.node == self.secondPlayer):
                    self.swapPlayer(self.whoToSwap, 1)
                    self.whoToSwap = -1
                elif(event.node == self.thirdPlayer):
                    self.swapPlayer(self.whoToSwap, 2)
                    self.whoToSwap =-1
                elif(event.node == self.forthPlayer):
                    self.swapPlayer(self.whoToSwap, 3)
                    self.whoToSwap = -1
                else:
                    raise SyntaxError ("Wtf")
            else:
                raise SyntaxError ("Wtf")
        
        
        
       
    def swapPlayer(self,x, y ):# angefangen bei 0 bis 3
        if(x == y):
            pass
        else:
            tmp = self.player[x]
            self.player[x] = self.player[y]
            self.player[y] = tmp
            
            tmp = self.playerIP[x]
            self.playerIP[x] = self.playerIP[y]
            self.playerIP[y] = tmp
            self.rdyPlayer = [False,False,False,False]
            
            self.rectNodPlayerArr[x].updateTextNode(self.player[x])
            self.rectNodPlayerArr[y].updateTextNode(self.player[y])
            self.gui.sendMsgToAll("notRdy")
    
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
        
         
    def updatePlayerLeft(self, ip):
        self.connectedPlayers-=1
        self.numberPlayers.updateTextForLobbyLine( "Players connected:", str(self.connectedPlayers)+"/"+ str(self.modus))
        i = 0
        b = False
        for j in range(self.modus):
            self.rdyPlayer[j] = False
        for i in range(self.modus):
            if(self.playerIP[i] == ip):
                if((i+1 < self.modus) & ((self.player[i+1] != "Attacker") & (self.player[i+1] != "Defender")) ):
                    self.player[i] = self.player[i+1]
                    self.playerIP[i] = self.playerIP[i+1]
                    (self.rectNodPlayerArr[i]).updateTextNode(self.player[i]) 
                else:
                    if((i == 0) | (i == 1)):
                        self.player[i] = "Defender"
                        self.playerIP[i] = ""
                        (self.rectNodPlayerArr[i]).updateTextNode("Defender") 
                    else:
                        self.player[i] = "Attacker"
                        self.playerIP[i] = ""
                        (self.rectNodPlayerArr[i]).updateTextNode("Attacker")
                b = True
            else:
                if(b):
                    if((i+1 < self.modus)&((self.player[i+1] != "Attacker") & (self.player[i+1] != "Defender"))):
                        self.player[i] = self.player[i+1]
                        self.playerIP[i] = self.playerIP[i+1]
                        (self.rectNodPlayerArr[i]).updateTextNode(self.player[i]) 
                    else:
                        if((i == 0) | (i == 1)):
                            self.player[i] = "Defender"
                            self.playerIP[i] = ""
                            (self.rectNodPlayerArr[i]).updateTextNode("Defender") 
                        else:
                            self.player[i] = "Attacker"
                            self.playerIP[i] = ""
                            (self.rectNodPlayerArr[i]).updateTextNode("Attacker")
           
        self.gui.sendMsgToAll("notRdy")
        
        
    def updateJoinedPlayerNumber(self, ip, name):
        if(self.connectedPlayers+1>self.modus):
            raise SyntaxError("Mehr Spieler als erlaubt; updateJoinedPlayerNumber")
        else:
            i = 0
            for i in range (self.modus):
                if(self.playerIP[i] == ""):
                    self.numberPlayers.updateTextForLobbyLine( "Players connected:", str(self.connectedPlayers+1)+"/"+ str(self.modus))
                    self.player[i] = name
                    (self.rectNodPlayerArr[i]).updateTextNode(name)
                    self.playerIP[i] = ip
                    self.connectedPlayers+=1
                    break
            