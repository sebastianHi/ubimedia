from libavg import avg
import src.FallingBlock, src.GameMenue

class cubeFallingBlock(object):



    def __init__(self, GameMenue, Field):
        
        self.part1 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (7 * GameMenue.blocksize), Field.yWertOben), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "FF0000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part2 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (8 * GameMenue.blocksize), Field.yWertOben), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "FF0000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part3 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (7 * GameMenue.blocksize), Field.yWertOben+ GameMenue.blocksize), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "FF0000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part4 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (8 * GameMenue.blocksize), Field.yWertOben+ GameMenue.blocksize), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "FF0000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.currPos1 = (6,0)
        self.currPos2 = (7,0)
        self.currPos3 = (6,1)
        self.currPos4 = (7,1)
        self.blockType = "cube" 
        
    
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
        pass

    def hitGround(self): # gibt True zurueck, wenn es den "Boden" bzw ein Hindernis beruehrt, sonst False
        
            b = self.Field.matrix[self.currPos3[0]][self.currPos3[1] + self.GameMenue.blocksize]
            c = self.Field.matrix[self.currPos4[0]][self.currPos4[1] + self.GameMenue.blocksize]
            if (c[1] > 18) or (b == True) or (c == True):
                return True
            else:
                return False

    def checkLeftBound(self): #return true wenn bewegung moeglich
        # pruefe part 1,3
            a = self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1]]
            b = self.Field.matrix[self.currPos3[0] - 1][self.currPos3[1]]
            if (a[0] < 0) or (a == True) or (b == True):
                return False
            else:
                return True
 
            
    
    def checkRightBound(self, node):#return true wenn bewegung moeglich, prueft nur rechten unteren Block
        # pruefe part 2,4
            a = self.Field.matrix[self.currPos2[0] + 1][self.currPos2[1]]
            b = self.Field.matrix[self.currPos4[0] + 1][self.currPos4[1]]
            if (b[0] > 13) or (a == True) or (b == True):
                return False
            else:
                return True