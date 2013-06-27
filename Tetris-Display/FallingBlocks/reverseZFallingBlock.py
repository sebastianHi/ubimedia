from libavg import avg
from src import FallingBlock,GameMenue

class reverseZFallingBlock(FallingBlock):



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
    
    def hitGround(self): # gibt True zurück, wenn es den "Boden" bzw ein Hindernis berührt, sonst False
        if (self.rotatingPosition == 0): #check part2, 3 und 4
            a = self.Field.Matrix[self.currPos2[0]][self.currPos2[1] + self.GameMenue.blocksize]
            b = self.Field.Matrix[self.currPos3[0]][self.currPos3[1] + self.GameMenue.blocksize]
            c = self.Field.Matrix[self.currPos4[0]][self.currPos4[1] + self.GameMenue.blocksize]
            if (a[1] > 18) or (a[1] == True) or (b[1] > 18) or (b[1] == True) or (c[1] > 18) or (c[1] == True):
                return True
            else:
                return False
        else: # check part1 und part 3
            a = self.Field.Matrix[self.currPos1[0]][self.currPos1[1] + self.GameMenue.blocksize]
            b = self.Field.Matrix[self.currPos3[0]][self.currPos3[1] + self.GameMenue.blocksize]
            if (a[1] > 18) or (a[1] == True) or (b[1] > 18) or (b[1] == True):
                return True
            else: return False
    
    def checkLeftBound(self): #return true wenn bewegung moeglich
        
        if (self.rotatingPosition == 0): # prüfe part 1,3
            a = self.Field.Matrix[self.currPos1[0] - 1][self.currPos1[1]]
            b = self.Field.Matrix[self.currPos3[0] - 1][self.currPos3[1]]
            if (b[0] < 0) or (a[0] == True) or (b[0] == True):
                return False
            else:
                return True
        else: # prüfe part1,2,3
            a = self.Field.Matrix[self.currPos1[0] - 1][self.currPos1[1]]
            b = self.Field.Matrix[self.currPos2[0] - 1][self.currPos2[1]]
            c = self.Field.Matrix[self.currPos3[0] - 1][self.currPos3[1]]
            if (b[0] < 0) or (a[0] == True) or (b[0] == True) or (c[0] == True):
                return False
            else:
                return True
    
    def checkRightBound(self):#return true wenn bewegung moeglich
        
        if (self.rotatingPosition == 0): # prüfe part 2,4
            a = self.Field.Matrix[self.currPos2[0] + 1][self.currPos2[1]]
            b = self.Field.Matrix[self.currPos4[0] + 1][self.currPos4[1]]
            if (a[0] > 13) or (a[0] == True) or (b[0] == True):
                return False
            else:
                return True
        else: # prüfe part2,3,4
            a = self.Field.Matrix[self.currPos2[0] + 1][self.currPos2[1]]
            b = self.Field.Matrix[self.currPos3[0] + 1][self.currPos3[1]]
            c = self.Field.Matrix[self.currPos4[0] + 1][self.currPos4[1]]
            if (b[0] > 13) or (a[0] == True) or (b[0] == True) or (c[0] == True):
                return False
            else:
                return True
    
    def checkCollisionAtRotation(self, RotatingNumber): # True = Collison, False = No Collision
        
        # muss in beiden Fällen currPos1 und currPos4 abfragen
        if (RotatingNumber == 0):
            a = self.Field.Matrix[self.currPos2[0] - 2][self.currPos2[1] - 1]
            b = self.Field.Matrix[self.currPos4[0] - 1][self.currPos1[1] + 1]
            if (a[1] < 0) or (b[1] > 18):
                return True
            elif (b == True):
                    return True
            else:
                    return False
                
        else:
            a = self.Field.Matrix[self.currPos1[0] - 2][self.currPos1[1] + 1]
            b = self.Field.Matrix[self.currPos4[0] + 1][self.currPos1[1] - 1]
            if (a[0] < 0) or (b[0] > 18):
                return True
            elif (b == True) or (a == True):
                    return True
            else:
                    return False