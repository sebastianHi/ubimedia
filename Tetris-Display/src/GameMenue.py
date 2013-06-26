from libavg import avg
from TextRectNode import TextRectNode
from Field import Field

class GameMenue(object):
    
    def __init__(self, parent, player):
        self.player = player
        self.rootNode = parent
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
        
        self.linksFeld1X   = xstartFeld1 + self.divNodeGameMenue.size[0]*0.025
        self.rechtsFeld1X  = xendFeld1 -self.divNodeGameMenue.size[0]*0.025
        
        self.linksFeld2X   = xstartFeld2 + self.divNodeGameMenue.size[0]*0.025
        self.rechtsFeld2X  = xendFeld2 -self.divNodeGameMenue.size[0]*0.025
 
        self.yOben = self.divNodeGameMenue.size[1] * 0.03
        self.yUnten =  self.yOben + self.tetrishoehe
        self.field1 = Field(self.linksFeld1X, self.rechtsFeld1X, self.yOben, self.yUnten)
        self.field2 = Field(self.linksFeld2X, self.rechtsFeld2X, self.yOben, self.yUnten)
        
        print "Blocksize: ", self.blocksize
        print "Tetrisfeldbegrenzungen:   lX1:",self.linksFeld1X,"  rF1: ",self.rechtsFeld1X,"   lF2: ",self.linksFeld2X,"  rF2:  ",self.rechtsFeld2X,"  yO: ", self.yOben," yU: ", self.yUnten
        
        
        
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
       

        self.test1 = avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (self.linksFeld1X+ self.blocksize, self.yOben), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.blocksize ,self.blocksize)
                                  )
        self.test2 = avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (self.linksFeld1X+ self.blocksize+ self.blocksize, self.yOben), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.blocksize ,self.blocksize)
                                  )
        self.test3 = avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (self.linksFeld1X+ self.blocksize+ self.blocksize+ self.blocksize, self.yOben), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.blocksize ,self.blocksize)
                                  )
        self.test4 = avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (self.linksFeld1X+ self.blocksize+ self.blocksize, self.yOben+ self.blocksize), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.blocksize ,self.blocksize)
                                  )

    
        
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
                                  size = avg.Point2D(endX - startX ,self.divNodeGameMenue.size[1]*0.04))
           
        self.player.setInterval(5, self.drop)                       
                                  
    def timerLCountDown (self):
        count = int (self.timerLimit.text)
        count -= 1
        self.timerLimit.text = str(count)
        
    def drop(self):
        if(self.test3.pos[1]+2*self.blocksize<=self.yUnten):
            self.test1.pos = (self.test1.pos[0],self.test1.pos[1]+1)
            self.test2.pos = (self.test2.pos[0],self.test2.pos[1]+1)
            self.test3.pos = (self.test3.pos[0],self.test3.pos[1]+1)
            self.test4.pos = (self.test4.pos[0],self.test4.pos[1]+1)