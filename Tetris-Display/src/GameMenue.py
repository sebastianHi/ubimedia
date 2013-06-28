from libavg import avg
from Field import Field

class GameMenue(object):
    
    def __init__(self, parent, player):
        self.player = player
        self.rootNode = parent
        self.divNodeGameMenue= avg.DivNode(parent = self.rootNode, size  = self.rootNode.size, active = False)
        self.background = avg.RectNode(parent = self.divNodeGameMenue, pos = (0,0), fillcolor = "0040FF", fillopacity = 1, color = "0040FF", size = self.divNodeGameMenue.size )
        self.yOben  = int(self.divNodeGameMenue.size[1] * 0.03)
#feld1 berechnungen
        self.xstartFeld1 = self.divNodeGameMenue.size[0] * 0.045
        self.xendFeld1   = int(self.divNodeGameMenue.size[0] * 0.45) - int(self.divNodeGameMenue.size[0]*0.025)
        sizeField = self.xendFeld1 - self.xstartFeld1
        resizedField = self.naechsteZahlDurch14Teilbar(sizeField)
        self.xstartFeld1 = self.xendFeld1 - resizedField

#feld2 berechnungen
        self.xendFeld2 = self.divNodeGameMenue.size[0] -self.xstartFeld1
        self.xstartFeld2 = self.xendFeld2 - resizedField

        self.blocksize = (self.xendFeld1 - self.xstartFeld1 )/14
        self.tetrishoehe = self.blocksize * 19
        
#Gui initialisierung
        self.initFeld(self.xstartFeld1, self.xendFeld1, self.yOben )
        self.initFeld(self.xstartFeld2, self.xendFeld2, self.yOben )

#fuer Matrix feld initialisierung 
        self.komischAlternativZuyObnloeschbar = self.yOben
        self.yUnten =  self.yOben + self.tetrishoehe
        self.field1 = Field(self.xstartFeld1, self.xendFeld1, self.yOben, self.yUnten,self.blocksize,self.player,self)
        self.field2 = Field(self.xstartFeld2, self.xendFeld2, self.yOben, self.yUnten,self.blocksize,self.player,self)
        
        print "Tetrisfeldbegrenzungen:   lF1:",self.xstartFeld1,"  rF1: ",self.xendFeld1,"   lF1F2: ",self.xstartFeld2,"  rF2:  ",self.xendFeld2,"  yO: ", self.yOben," yU: ", self.yUnten
        print "Ein Feld:  Blocksize:  ", self.blocksize, "    Hoehe:   ", self.tetrishoehe, "    Breite:  ", self.xendFeld1-self.xstartFeld1
#buttoms werden initialisiert

        positionMittlereButtons = self.divNodeGameMenue.size[0]*0.5
        self.timelimit =  avg.WordsNode(pos = (positionMittlereButtons , self.divNodeGameMenue.size[1] * 0.20),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="TimeLimit", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        self.timerLimit = avg.WordsNode(pos = (positionMittlereButtons , self.divNodeGameMenue.size[1] * 0.23),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="500", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
        self.timeLimitCounter = self.player.setInterval(1000, self.timerLCountDown)
        
        self.roundText = avg.WordsNode(pos = (positionMittlereButtons , self.divNodeGameMenue.size[1] * 0.33),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="Round", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
        self.roundNumber = avg.WordsNode(pos = (positionMittlereButtons , self.divNodeGameMenue.size[1] * 0.36),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="1", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
        self.speedText = avg.WordsNode(pos = (positionMittlereButtons , self.divNodeGameMenue.size[1] * 0.46),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="Speed", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
        self.speedNumber = avg.WordsNode(pos = (positionMittlereButtons , self.divNodeGameMenue.size[1] * 0.49),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="1", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
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
##loeschbar
        ##TODO:self.testFallingNode()

    
        
    def initFeld (self, startX, endX, oben):
#linker Rahmen
        avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (startX -int(self.divNodeGameMenue.size[0]*0.025)  , oben), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(int(self.divNodeGameMenue.size[0]*0.025) ,self.tetrishoehe) #self.divNodeGameMenue.size[1]* 0.87
                                  )
#rechter Rahmen
        avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (endX , oben), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(int(self.divNodeGameMenue.size[0]*0.025), self.tetrishoehe)
                                  )
#Boden
        avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (startX-int(self.divNodeGameMenue.size[0]*0.025), self.tetrishoehe+oben), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(endX-startX+2*int(self.divNodeGameMenue.size[0]*0.025) ,self.divNodeGameMenue.size[1]*0.04))
            
                              
                                  
    def timerLCountDown (self):
        count = int (self.timerLimit.text)
        count -= 1
        self.timerLimit.text = str(count)
        
    def naechsteZahlDurch14Teilbar(self,value):
        x = value % 14
        return value - x
    
##-------------------------------------------Nur fuer test---------------------------------------------------------------------------------------------------------------------------
    def testFallingNode(self):
        self.test1 = avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (self.xstartFeld1, self.komischAlternativZuyObnloeschbar), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.blocksize ,self.blocksize)
                                  )
        self.test2 = avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (self.xendFeld1- self.blocksize, self.komischAlternativZuyObnloeschbar), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.blocksize ,self.blocksize)
                                  )
        self.test3 = avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (self.xstartFeld2, self.komischAlternativZuyObnloeschbar), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.blocksize ,self.blocksize)
                                  )
        self.test4 = avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (self.xendFeld2- self.blocksize, self.komischAlternativZuyObnloeschbar+ self.blocksize), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.blocksize ,self.blocksize)
                                  )
        self.player.setInterval(5, self.drop)
    
    def drop(self):
        if(self.test3.pos[1]+2*self.blocksize<self.yUnten):
            self.test1.pos = (self.test1.pos[0],self.test1.pos[1]+1)
            self.test2.pos = (self.test2.pos[0],self.test2.pos[1]+1)
            self.test3.pos = (self.test3.pos[0],self.test3.pos[1]+1)
            self.test4.pos = (self.test4.pos[0],self.test4.pos[1]+1)        