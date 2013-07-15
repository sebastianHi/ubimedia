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
       
        self.playstyleModus = ""
        self.modus = modus
        if(self.modus==2):
            self.playstyleModus = "1vs1"
            self.player[0] = "Player 1"
            self.player[1] = "Player 2"
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
            
#         
#     def updatePlayerName(self):
#         #self.player[1-4] om startlobby text updaten der rectnodes
#         pass
#     
#    
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
        for i in range(self.modus):
            if(b):
                if(i < self.modus):
                    self.player[i-1] = self.player[i] 
                    self.playerIP[i-1]  =self.playerIP[i] 
                    self.rdyPlayer[i-1] = self.rdyPlayer[i]
                    self.rectNodPlayerArr[i-1].updateTextNode(self.player[i-1])
                else:
                    self.player[i] = ""
                    self.playerIP[i] = ""
                    self.rdyPlayer[i] = False 
                    (self.rectNodPlayerArr[i]).updateTextNode("") 
            if(self.playerIP[i] == ip):
                self.player[i] = ""
                self.playerIP[i] = ""
                self.rdyPlayer[i] = False 
                (self.rectNodPlayerArr[i]).updateTextNode("") 
                b = True
    
            
     
    def swapPlayer(self,event):
#TODO: hier muss man drag und drop implementieren mit deren hilfe man den text der rectnodes tauschen kann
        pass
        
    def updateJoinedPlayerNumber(self, ip, name):
        if(self.connectedPlayers+1>self.modus):
            raise SyntaxError("Mehr Spieler als erlaubt; updateJoinedPlayerNumber")
        else:
            self.numberPlayers.updateTextForLobbyLine( "Players connected:", str(self.connectedPlayers+1)+"/"+ str(self.modus))
            self.player[self.connectedPlayers] = name
            (self.rectNodPlayerArr[self.connectedPlayers]).updateTextNode(name)
            self.playerIP[self.connectedPlayers] = ip
            self.connectedPlayers+=1
            