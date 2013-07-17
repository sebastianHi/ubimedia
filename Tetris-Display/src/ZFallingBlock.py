from libavg import avg

class ZFallingBlock(object):
    #moveBlockLeft                :  Laesst block nach links bewegen
    #moveBlockRight               :  Laesst block nach rechts bewegen
    #rotateLeft                   :  Laesst block nach linkts rotieren
    #rotateRight                  :  Laesst block nach rechts rotieren
    #hitGround                    :  Gibt wahr zurueck, wenn hindernis unten beruehrt.
    #checkRightBound              :  Gibt false zurueck, wenn ein hindernis rechts befindetet
    #checkLeftBound               :  Gibt false zurueck, wenn ein hindernis links befindetet
    #checkCollisionAtRotation     :  Gibt false zurueck, wenn rotation nach rechts nicht moeglich


    def __init__(self, GameMenue, Field):
        
        self.Field = Field
        self.gameMenue = GameMenue
        
        self.part1 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben + (6 * GameMenue.blocksize), Field.yWertOben), 
                                  fillcolor = "FF00FF", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part2 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben + (7 * GameMenue.blocksize), Field.yWertOben), 
                                  fillcolor = "FF00FF", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part3 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben + (7 * GameMenue.blocksize), Field.yWertOben + GameMenue.blocksize), 
                                  fillcolor = "FF00FF", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part4 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben + (8 * GameMenue.blocksize), Field.yWertOben + GameMenue.blocksize), 
                                  fillcolor = "FF00FF", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )

        self.currPos1 = (6,0)
        self.currPos2 = (7,0)
        self.currPos3 = (7,1)
        self.currPos4 = (8,1)
        self.rotatingPosition = 0
        self.blockType = "Z"
        
        
    def moveBlockLeft(self):
        if(self.checkLeftBound()):
            self.currPos1 = (self.currPos1[0] - 1,self.currPos1[1])
            self.currPos2 = (self.currPos2[0] - 1,self.currPos2[1])
            self.currPos3 = (self.currPos3[0] - 1,self.currPos3[1])
            self.currPos4 = (self.currPos4[0] - 1,self.currPos4[1])
            self.part1.pos = ((self.part1.pos[0] - self.gameMenue.blocksize),self.part1.pos[1])
            self.part2.pos = ((self.part2.pos[0] - self.gameMenue.blocksize),self.part2.pos[1])
            self.part3.pos = ((self.part3.pos[0] - self.gameMenue.blocksize),self.part3.pos[1])
            self.part4.pos = ((self.part4.pos[0] - self.gameMenue.blocksize),self.part4.pos[1])
        else:
            pass  # dont move dat shit
        
    def moveBlockRight(self):
        
        if(self.checkRightBound()):
            self.currPos1 = (self.currPos1[0] + 1,self.currPos1[1])
            self.currPos2 = (self.currPos2[0] + 1,self.currPos2[1])
            self.currPos3 = (self.currPos3[0] + 1,self.currPos3[1])
            self.currPos4 = (self.currPos4[0] + 1,self.currPos4[1])
            self.part1.pos = ((self.part1.pos[0] + self.gameMenue.blocksize),self.part1.pos[1])
            self.part2.pos = ((self.part2.pos[0] + self.gameMenue.blocksize),self.part2.pos[1])
            self.part3.pos = ((self.part3.pos[0] + self.gameMenue.blocksize),self.part3.pos[1])
            self.part4.pos = ((self.part4.pos[0] + self.gameMenue.blocksize),self.part4.pos[1])
        else:
            pass  # dont move dat shit
    
    def rotateLeft(self):
        if (self.rotatingPosition == 0):
            if (self.checkCollisionAtRotation(0)):
                pass
            else:
                self.currPos1 = (self.currPos1[0] + 2,self.currPos1[1] - 1)
                self.currPos2 = (self.currPos2[0] + 1,self.currPos2[1])
                self.currPos3 = (self.currPos3[0],self.currPos3[1] - 1)
                self.currPos4 = (self.currPos4[0] - 1,self.currPos4[1])
                self.part1.pos = ((self.part1.pos[0] + (2 *  self.gameMenue.blocksize)),self.part1.pos[1] - self.gameMenue.blocksize)
                self.part2.pos = ((self.part2.pos[0] + self.gameMenue.blocksize),self.part2.pos[1])
                self.part3.pos = (self.part3.pos[0],self.part3.pos[1] - self.gameMenue.blocksize)
                self.part4.pos = ((self.part4.pos[0] - self.gameMenue.blocksize),self.part4.pos[1])
                self.rotatingPosition = 1
        else:
            if (self.checkCollisionAtRotation(1)):
                pass
            else:
                self.currPos1 = (self.currPos1[0] - 2,self.currPos1[1] + 1)
                self.currPos2 = (self.currPos2[0] - 1,self.currPos2[1])
                self.currPos3 = (self.currPos3[0],self.currPos3[1] + 1)
                self.currPos4 = (self.currPos4[0] + 1,self.currPos4[1])
                self.part1.pos = ((self.part1.pos[0] - (2 *  self.gameMenue.blocksize)),self.part1.pos[1] + self.gameMenue.blocksize)
                self.part2.pos = ((self.part2.pos[0] - self.gameMenue.blocksize),self.part2.pos[1])
                self.part3.pos = (self.part3.pos[0],self.part3.pos[1] + self.gameMenue.blocksize)
                self.part4.pos = ((self.part4.pos[0] + self.gameMenue.blocksize),self.part4.pos[1])
                self.rotatingPosition = 0
            
    def rotateRight(self):
        self.rotateLeft()

    
    def hitGround(self): # gibt True zurueck, wenn es den "Boden" bzw ein Hindernis beruehrt, sonst False
        if((self.currPos2[1] + 1 > 18) | (self.currPos3[1] + 1 > 18) | (self.currPos4[1] + 1> 18) |(self.currPos1[1] + 1> 18) ):
            return True
        a = self.Field.matrix[self.currPos2[0]][self.currPos2[1] + 1]
        b = self.Field.matrix[self.currPos3[0]][self.currPos3[1] + 1]
        c = self.Field.matrix[self.currPos4[0]][self.currPos4[1] + 1]
        d = self.Field.matrix[self.currPos1[0]][self.currPos1[1] + 1]
        
        if (a or b or c or d):
            return True
        else:
            return False
    
    def checkLeftBound(self): #return true wenn bewegung moeglich
        if (self.rotatingPosition == 0): # pruefe part 1,3
            if (self.currPos1[0] - 1 < 0):
                return False
            a = self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1]]
            b = self.Field.matrix[self.currPos3[0] - 1][self.currPos3[1]]
            if  (a or b):
                return False
            else:
                return True
        else: # pruefe part1,3,4
            if (self.currPos3[0] - 1 < 0):
                return False
            a = self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1]]
            b = self.Field.matrix[self.currPos3[0] - 1][self.currPos3[1]]
            c = self.Field.matrix[self.currPos4[0] - 1][self.currPos4[1]]
            if  (a or b or c):
                return False
            else:
                return True
            
    
    def checkRightBound(self):#return true wenn bewegung moeglich, prueft nur rechten unteren Block
        if (self.rotatingPosition == 0): # pruefe part 2,4
            if (self.currPos4[0] + 1 > 13):
                return False
            a = self.Field.matrix[self.currPos2[0] + 1][self.currPos2[1]]
            b = self.Field.matrix[self.currPos4[0] + 1][self.currPos4[1]]
            if  (a or b):
                return False
            else:
                return True
        else: # pruefe part1,2,4
            if (self.currPos2[0] + 1 > 13):
                return False
            a = self.Field.matrix[self.currPos1[0] + 1][self.currPos1[1]]
            b = self.Field.matrix[self.currPos2[0] + 1][self.currPos2[1]]
            c = self.Field.matrix[self.currPos4[0] + 1][self.currPos4[1]]
            if  (a or b or c):
                return False
            else:
                return True
    
    def checkCollisionAtRotation(self, RotatingNumber): # True = Collison, False = No Collision
        
        if (RotatingNumber == 0):
            if (self.currPos1[1] - 1 < 0):
                return True
            a = self.Field.matrix[self.currPos1[0] + 2][self.currPos1[1] - 1]
            b = self.Field.matrix[self.currPos2[0] + 1][self.currPos2[1]]
            c = self.Field.matrix[self.currPos3[0]][self.currPos3[1] - 1]
            d = self.Field.matrix[self.currPos4[0] - 1][self.currPos4[1]]
            if  (a or b or c or d):
                return True
            else:
                return False
                
        else:
            if (self.currPos1[0] - 2 < 0):
                return True
            a = self.Field.matrix[self.currPos1[0] - 2][self.currPos1[1] + 1]
            b = self.Field.matrix[self.currPos2[0] - 1][self.currPos2[1]]
            c = self.Field.matrix[self.currPos3[0]][self.currPos3[1] + 1]
            d = self.Field.matrix[self.currPos4[0] + 1][self.currPos4[1]]
            if  (a or b or c or d):
                return True
            else:
                return False
            