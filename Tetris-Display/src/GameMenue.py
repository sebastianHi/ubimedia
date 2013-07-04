from libavg import avg
from Field import Field
from TextRectNode import TextRectNode

class GameMenue(object):
    
    def __init__(self, parent, player):
        self.player = player
        self.rootNode = parent
        self.divNodeGameMenue= avg.DivNode(parent = self.rootNode, size  = self.rootNode.size, active = False)
        self.background = avg.RectNode(parent = self.divNodeGameMenue, pos = (0,0), fillcolor = "0040FF", fillopacity = 1, color = "0040FF", size = self.divNodeGameMenue.size )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.menueLinkerXwert  = int(self.divNodeGameMenue.size[0]/2- self.divNodeGameMenue.size[0]*0.04)
        self.menueRechterXwert = int(self.divNodeGameMenue.size[0]/2+ self.divNodeGameMenue.size[0]*0.04)
        self.rahmenbreite = int(self.divNodeGameMenue.size[0]*0.025)
        self.yOben  = int(self.divNodeGameMenue.size[1] * 0.05) 
        self.untereBeschraenkung = self.divNodeGameMenue.size[1] * 0.92 - self.rahmenbreite
        self.xendFeld1 = self.menueLinkerXwert -self.rahmenbreite - self.divNodeGameMenue.size[1] * 0.03
        self.xstartFeld1, self.yUnten = self.berechneLinkesXUntenYFeld1(self.xendFeld1, self.untereBeschraenkung,self.yOben)
        sizefield = self.xendFeld1 - self.xstartFeld1
        self.xstartFeld2 = self.menueRechterXwert +self.rahmenbreite + self.divNodeGameMenue.size[1] * 0.03
        self.xendFeld2   = self.xstartFeld2 + sizefield
        self.blocksize = (self.xendFeld1 - self.xstartFeld1 )/14
        self.tetrishoehe = self.blocksize * 19
        
#Gui initialisierung
        self.initFeld(self.xstartFeld1, self.xendFeld1, self.yOben )
        self.initFeld(self.xstartFeld2, self.xendFeld2, self.yOben )

#fuer Matrix feld initialisierung 
        self.yUnten =  self.yOben + self.tetrishoehe
        self.field1 = Field(self.xstartFeld1, self.xendFeld1, self.yOben, self.yUnten,self.blocksize,self.player,self)
        #self.field2 = Field(self.xstartFeld2, self.xendFeld2, self.yOben, self.yUnten,self.blocksize,self.player,self)
        
        print "Tetrisfeldbegrenzungen:   lF1:",self.xstartFeld1,"  rF1: ",self.xendFeld1,"   lF1F2: ",self.xstartFeld2,"  rF2:  ",self.xendFeld2,"  yO: ", self.yOben," yU: ", self.yUnten
        print "Ein Feld:  Blocksize:  ", self.blocksize, "    Hoehe:   ", self.tetrishoehe, "    Breite:  ", self.xendFeld1-self.xstartFeld1
#buttoms werden initialisiert

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      

        self.hoeheMitlererBalken =  self.divNodeGameMenue.size[1] * 0.20
        mittlererBalken = self.divNodeGameMenue.size[0]/2
        
        self.timelimit =  avg.WordsNode(pos = (mittlererBalken , self.hoeheMitlererBalken),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="TimeLimit", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
        while(self.timelimit.size[0]>= (self.menueRechterXwert- self.menueLinkerXwert) | (self.timelimit.size[1]>= self.divNodeGameMenue.size[1]* 0.1 )):
            self.timelimit.fontsize-=1
            if(self.timelimit.fontsize<=0):
                self.timelimit.fontsize= 1
                break
        fontS = self.timelimit.fontsize  
        self.hoeheMitlererBalken +=  fontS + fontS*0.5
#-----------------------------------------------------------------------------------------------------------------------------------------------------------                 
        self.timerLimit = avg.WordsNode(pos = (mittlererBalken , self.hoeheMitlererBalken),
                                      fontsize = fontS, 
                                      text ="500", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
        self.hoeheMitlererBalken +=  4*fontS
        
        self.timeLimitCounter = self.player.setInterval(1000, self.timerLCountDown)
#----------------------------------------------------------------------------------------------------------------------------------------------------------- 
        
        self.roundText = avg.WordsNode(pos = (mittlererBalken, self.hoeheMitlererBalken),
                                      fontsize = fontS, 
                                      text ="Round", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        self.hoeheMitlererBalken +=  fontS + fontS*0.5
#----------------------------------------------------------------------------------------------------------------------------------------------------------- 
        
        self.roundNumber = avg.WordsNode(pos = (mittlererBalken , self.hoeheMitlererBalken),
                                      fontsize = fontS, 
                                      text ="1", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        self.hoeheMitlererBalken +=  4*fontS
#---------------------------------------------------------------------------------------------------------------------------------------------------------- 
        
        self.speedText = avg.WordsNode(pos = (mittlererBalken , self.hoeheMitlererBalken),
                                      fontsize = fontS, 
                                      text ="Speed", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        self.hoeheMitlererBalken +=  fontS + fontS*0.5
      
        self.speedNumber = avg.WordsNode(pos = (mittlererBalken , self.hoeheMitlererBalken),
                                      fontsize = fontS, 
                                      text ="1", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        self.hoeheMitlererBalken += 4*fontS

         
        self.scoreTeam1 = avg.WordsNode(pos = ((self.xstartFeld1 + self.xendFeld1)/2 , self.divNodeGameMenue.size[1] * 0.96),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="Score:  000000", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
          
        self.scoreTeam2 = avg.WordsNode(pos = ((self.xstartFeld2 + self.xendFeld2)/2 , self.divNodeGameMenue.size[1] * 0.96),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="Score:  000000",  
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
#-------------------------------------------------------------Tests UPDOWNROTATE---loeschbar spaeter----------------------------------------------------------------------------
        self.buttonMoveL = TextRectNode(parent = self.divNodeGameMenue, 
                                       pos = (self.divNodeGameMenue.size[0]*0.05,self.divNodeGameMenue.size[1] * 0.9),
                                       fillcolor ="000000",
                                       fillopacity=1,
                                       color = "000000",
                                       size = avg.Point2D(self.divNodeGameMenue.size[0]*0.1,self.divNodeGameMenue.size[1]*0.1))
        self.buttonMoveL.addTextGameTypeAndMain("L","FFFFFF")
        
        self.buttonRotateL = TextRectNode(parent = self.divNodeGameMenue, 
                                   pos = (self.divNodeGameMenue.size[0]*0.3,self.divNodeGameMenue.size[1] * 0.9),
                                   fillcolor ="000000",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodeGameMenue.size[0]*0.1,self.divNodeGameMenue.size[1]*0.1))
        self.buttonRotateL.addTextGameTypeAndMain("RL","FFFFFF")
        
        self.buttonRotateR = TextRectNode(parent = self.divNodeGameMenue, 
                                   pos = (self.divNodeGameMenue.size[0]*0.5,self.divNodeGameMenue.size[1] * 0.9),
                                   fillcolor ="000000",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodeGameMenue.size[0]*0.1,self.divNodeGameMenue.size[1]*0.1))
        self.buttonRotateR.addTextGameTypeAndMain("RR","FFFFFF")
        
        self.buttonMoveR = TextRectNode(parent = self.divNodeGameMenue, 
                                   pos = (self.divNodeGameMenue.size[0]*0.9,self.divNodeGameMenue.size[1] * 0.9),
                                   fillcolor ="000000",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodeGameMenue.size[0]*0.1,self.divNodeGameMenue.size[1]*0.1))
        self.buttonMoveR.addTextGameTypeAndMain("R","FFFFFF")
        
        self.buttonMoveL.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.buttonMoveL, self.eventMoveLinks) 
        self.buttonRotateL.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.buttonRotateL, self.eventRotateLinks) 
        self.buttonRotateR.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.buttonRotateR, self.eventRotateRechts) 
        self.buttonMoveR.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.buttonMoveR, self.eventMoveRechts) 

    def eventMoveLinks(self,event):
        self.field1.moveLeft()
    
    def eventRotateLinks(self,event):
        self.field1.rotateLeft()

    def eventRotateRechts(self,event):
        self.field1.rotateRight()

    def eventMoveRechts(self,event):
        self.field1.moveRight()




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





    # Ueberpruefung der FeldPunkte
#         avg.RectNode(pos=(self.xstartFeld1, self.yOben)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         avg.RectNode(pos=(self.xendFeld1, self.yOben)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         avg.RectNode(pos=(self.xstartFeld1, self.yUnten)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         avg.RectNode(pos=(self.xendFeld1, self.yUnten)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         avg.RectNode(pos=(self.xstartFeld2, self.yOben)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         avg.RectNode(pos=(self.xendFeld2, self.yOben)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         avg.RectNode(pos=(self.xstartFeld2, self.yUnten)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         avg.RectNode(pos=(self.xendFeld2, self.yUnten)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         
        
        
        
        
    def berechneLinkesXUntenYFeld1(self,rechteKante, untereSchranke, obereSchranke):
        linkesX = int(self.divNodeGameMenue.size[0] * 0.03) 
        size = rechteKante - linkesX
        size = self.naechsteZahlDurch14Teilbar(size)
        while(True):
            print "links ",linkesX, " rechts ",rechteKante," maxHoehe ", (untereSchranke - obereSchranke)
            blocksize = size / 14
            tetrishoehe = blocksize *19
            if((untereSchranke - obereSchranke) >= tetrishoehe):
                return ((rechteKante- size), obereSchranke-tetrishoehe)
            else:
                size-=14
                
        
        
        
    def timerLCountDown (self):
        count = int (self.timerLimit.text)
        count -= 1
        self.timerLimit.text = str(count)
        
    def naechsteZahlDurch14Teilbar(self,value):
        x = value % 14
        return value - x
    
    def initFeld (self, startX, endX, oben):
#linker Rahmen
        avg.RectNode(parent = self.divNodeGameMenue, sensitive = False,
                                  pos = (startX -self.rahmenbreite  , oben), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.rahmenbreite ,self.tetrishoehe) #self.divNodeGameMenue.size[1]* 0.87
                                  )
#rechter Rahmen
        avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (endX , oben), sensitive = False,
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.rahmenbreite, self.tetrishoehe)
                                  )
#Boden
        avg.RectNode(parent = self.divNodeGameMenue, sensitive = False,
                                  pos = (startX-self.rahmenbreite, self.tetrishoehe+oben), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(endX-startX+2*int(self.divNodeGameMenue.size[0]*0.025) ,self.rahmenbreite)
                                  )