from libavg import avg
from src import FallingBlock,GameMenue

class ZFallingBlock(FallingBlock):



    def __init__(self, GameMenue, Field):
        
        self.part1 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (GameMenue.linksFeld1X+ (6 * GameMenue.blocksize), GameMenue.yOben), 
                                  fillcolor = "FF00FF", fillopacity = 1, color = "FF00FF", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part2 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (GameMenue.linksFeld1X+ (7 * GameMenue.blocksize), GameMenue.yOben), 
                                  fillcolor = "FF00FF", fillopacity = 1, color = "FF00FF", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part3 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (GameMenue.linksFeld1X+ (7 * GameMenue.blocksize), GameMenue.yOben + GameMenue.Blocksize), 
                                  fillcolor = "FF00FF", fillopacity = 1, color = "FF00FF", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part4 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (GameMenue.linksFeld1X+ (8 * GameMenue.blocksize), GameMenue.yOben + GameMenue.Blocksize), 
                                  fillcolor = "FF00FF", fillopacity = 1, color = "FF00FF", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.Field = Field
        self.GameMenue = GameMenue
        self.currPos1 = (5,0)
        self.currPos2 = (6,0)
        self.currPos3 = (6,1)
        self.currPos4 = (7,1)
        self.RotatingPosition = 0
        
        
    
    def moveBlockLeft(self, node):
        
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
        
    def moveBlockRight(self, node):
        
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
        if (self.RotatingPosition == 0):
            if (self.checkCollisionAtRotation(0)):
                pass
            else:
                self.currPos1 = self.currPos1[self.currPos1[0] - 1][self.currPos1[1]]
                self.currPos2 = self.currPos2[self.currPos2[0] - 1][self.currPos2[1]]
                self.currPos3 = self.currPos3[self.currPos3[0] - 1][self.currPos3[1]]
                self.currPos4 = self.currPos4[self.currPos4[0] - 1][self.currPos4[1]]
                self.part1.pos = ((self.part1.pos[0] - self.GameMenue.blocksize),self.part1.pos[1])
                self.part2.pos = ((self.part2.pos[0] - self.GameMenue.blocksize),self.part2.pos[1])
                self.part3.pos = ((self.part3.pos[0] - self.GameMenue.blocksize),self.part3.pos[1])
                self.part4.pos = ((self.part4.pos[0] - self.GameMenue.blocksize),self.part4.pos[1])
        else:
            pass
            
            
    
    def hitGround(self): #<-- ruf feld.hitground auf um zu zeigen neuer stein kann fallen.
        pass
    
    def checkLeftBound(self): #return true wenn bewegung moeglich, prüft nur linken oberen Block
        
        return self.Field.Matrix[self.currPos1[0] - 1][self.currPos1[1]]
    
    def checkRightBound(self, node):#return true wenn bewegung moeglich, prüft nur rechten unteren Block
        
        return self.Field.Matrix[self.currPos4[0] + 1][self.currPos1[1]]
    
    def checkCollisionAtRotation(self, RotatingNumber): # True = Collison, False = No Collision
        
            