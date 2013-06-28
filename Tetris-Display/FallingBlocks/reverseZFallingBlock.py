from libavg import avg
import src.FallingBlock, src.GameMenue

class reverseZFallingBlock(object):



    def __init__(self, GameMenue, Field):
        
        self.part1 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben + (7 * GameMenue.blocksize), Field.yWertOben), 
                                  fillcolor = "FFFFFF", fillopacity = 1, color = "FFFFFF", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part2 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben + (8 * GameMenue.blocksize), Field.yWertOben), 
                                  fillcolor = "FFFFFF", fillopacity = 1, color = "FFFFFF", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part3 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben + (6 * GameMenue.blocksize), Field.yWertOben + GameMenue.Blocksize), 
                                  fillcolor = "FFFFFF", fillopacity = 1, color = "FFFFFF", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part4 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben + (7 * GameMenue.blocksize), Field.yWertOben + GameMenue.Blocksize), 
                                  fillcolor = "FFFFFF", fillopacity = 1, color = "FFFFFF", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.Field = Field
        self.GameMenue = GameMenue
        self.currPos1 = (6,0)
        self.currPos2 = (7,0)
        self.currPos3 = (5,1)
        self.currPos4 = (6,1)
        self.rotatingPosition = 0
        self.blockType = "reverseZ"
        
    def moveBlockLeft(self):
        
        if(self.checkLeftBound()):
            self.currPos1 = self.currPos1[self.currPos1[0] - 1][self.currPos1[1]]
            self.currPos2 = self.currPos2[self.currPos2[0] - 1][self.currPos2[1]]
            self.currPos3 = self.currPos3[self.currPos3[0] - 1][self.currPos3[1]]
            self.currPos4 = self.currPos4[self.currPos4[0] - 1][self.currPos4[1]]
            self.part1.pos = ((self.part1.pos[0] - self.GameMenue.blocksize),self.part1.pos[1])
            self.part2.pos = ((self.part2.pos[0] - self.GameMenue.blocksize),self.part2.pos[1])
            self.part3.pos = ((self.part3.pos[0] - self.GameMenue.blocksize),self.part3.pos[1])
            self.part4.pos = ((self.part4.pos[0] - self.GameMenue.blocksize),self.part4.pos[1])
        else:
            pass  # dont move dat shit
        
        
    def moveBlockRight(self):
        
        if(self.checkRightBound()):
            self.currPos1 = self.currPos1[self.currPos1[0] + 1][self.currPos1[1]]
            self.currPos2 = self.currPos2[self.currPos2[0] + 1][self.currPos2[1]]
            self.currPos3 = self.currPos3[self.currPos3[0] + 1][self.currPos3[1]]
            self.currPos4 = self.currPos4[self.currPos4[0] + 1][self.currPos4[1]]
            self.part1.pos = ((self.part1.pos[0] + self.GameMenue.blocksize),self.part1.pos[1])
            self.part2.pos = ((self.part2.pos[0] + self.GameMenue.blocksize),self.part2.pos[1])
            self.part3.pos = ((self.part3.pos[0] + self.GameMenue.blocksize),self.part3.pos[1])
            self.part4.pos = ((self.part4.pos[0] + self.GameMenue.blocksize),self.part4.pos[1])
        else:
            pass  # dont move dat shit
    
    
    def rotate(self):
        if (self.rotatingPosition == 0):
            if (self.checkCollisionAtRotation(0)):
                pass
            else:
                self.currPos2 = self.currPos2[self.currPos2[0] - 1][self.currPos2[self.currPos2[1] - 1]]
                self.currPos3 = self.currPos3[self.currPos3[0] + 2][self.currPos3[1]]
                self.currPos4 = self.currPos4[self.currPos4[0] + 1][self.currPos4[self.currPos4[1] - 1]]
                self.part2.pos = ((self.part2.pos[0] - self.GameMenue.blocksize),self.part2.pos[1] - self.GameMenue.blocksize)
                self.part3.pos = (self.part3.pos[0] + (2 * self.GameMenue.blocksize),self.part3.pos[1])
                self.part4.pos = ((self.part4.pos[0] + self.GameMenue.blocksize),self.part4.pos[1] - self.GameMenue.blocksize)
                self.rotatingPosition = 1
        else:
            if (self.checkCollisionAtRotation(1)):
                pass
            else:
                self.currPos2 = self.currPos2[self.currPos2[0] + 1][self.currPos2[self.currPos2[1] + 1]]
                self.currPos3 = self.currPos3[self.currPos3[0] - 2][self.currPos3[1]]
                self.currPos4 = self.currPos4[self.currPos4[0] - 1][self.currPos4[self.currPos4[1] + 1]]
                self.part2.pos = ((self.part2.pos[0] + self.GameMenue.blocksize),self.part2.pos[1] + self.GameMenue.blocksize)
                self.part3.pos = (self.part3.pos[0] - (2 * self.GameMenue.blocksize),self.part3.pos[1])
                self.part4.pos = ((self.part4.pos[0] - self.GameMenue.blocksize),self.part4.pos[1] + self.GameMenue.blocksize)
                self.rotatingPosition = 0
    
    def hitGround(self): # gibt True zurueck, wenn es den "Boden" bzw ein Hindernis beruehrt, sonst False
        if (self.rotatingPosition == 0): #check part2, 3 und 4
            a = self.Field.matrix[self.currPos2[0]][self.currPos2[1] + self.GameMenue.blocksize]
            b = self.Field.matrix[self.currPos3[0]][self.currPos3[1] + self.GameMenue.blocksize]
            c = self.Field.matrix[self.currPos4[0]][self.currPos4[1] + self.GameMenue.blocksize]
            if (a[1] > 18) or (a == True) or (b[1] > 18) or (b == True) or (c[1] > 18) or (c == True):
                return True
            else:
                return False
        else: # check part1 und part 3
            a = self.Field.matrix[self.currPos1[0]][self.currPos1[1] + self.GameMenue.blocksize]
            b = self.Field.matrix[self.currPos3[0]][self.currPos3[1] + self.GameMenue.blocksize]
            if (a[1] > 18) or (a == True) or (b[1] > 18) or (b == True):
                return True
            else: 
                return False
    
    def checkLeftBound(self): #return true wenn bewegung moeglich
        
        if (self.rotatingPosition == 0): # pruefe part 1,3
            a = self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1]]
            b = self.Field.matrix[self.currPos3[0] - 1][self.currPos3[1]]
            if (b[0] < 0) or (a == True) or (b == True):
                return False
            else:
                return True
        else: # pruefe part1,2,3
            a = self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1]]
            b = self.Field.matrix[self.currPos2[0] - 1][self.currPos2[1]]
            c = self.Field.matrix[self.currPos3[0] - 1][self.currPos3[1]]
            if (b[0] < 0) or (a == True) or (b == True) or (c == True):
                return False
            else:
                return True
    
    def checkRightBound(self):#return true wenn bewegung moeglich
        
        if (self.rotatingPosition == 0): # pruefe part 2,4
            a = self.Field.matrix[self.currPos2[0] + 1][self.currPos2[1]]
            b = self.Field.matrix[self.currPos4[0] + 1][self.currPos4[1]]
            if (a[0] > 13) or (a == True) or (b == True):
                return False
            else:
                return True
        else: # pruefe part2,3,4
            a = self.Field.matrix[self.currPos2[0] + 1][self.currPos2[1]]
            b = self.Field.matrix[self.currPos3[0] + 1][self.currPos3[1]]
            c = self.Field.matrix[self.currPos4[0] + 1][self.currPos4[1]]
            if (b[0] > 13) or (a == True) or (b == True) or (c == True):
                return False
            else:
                return True
    
    def checkCollisionAtRotation(self, RotatingNumber): # True = Collison, False = No Collision
        
        if (RotatingNumber == 0):
            b = self.Field.matrix[self.currPos2[0] - 1][self.currPos2[1] - 1]
            c = self.Field.matrix[self.currPos3[0] + 2][self.currPos3[1]]
            d = self.Field.matrix[self.currPos4[0] + 1][self.currPos4[1] - 1]
            if (b[1] < 0) or (b == True) or (c == True) or (d == True):
                return True
            else:
                return False
                
        else:
            b = self.Field.matrix[self.currPos2[0] + 1][self.currPos2[1] + 1]
            c = self.Field.matrix[self.currPos3[0] - 2][self.currPos3[1]]
            d = self.Field.matrix[self.currPos4[0] - 1][self.currPos4[1] + 1]
            if (c[0] < 0) or (b == True) or (c == True) or (d == True):
                return True
            else:
                return False
            