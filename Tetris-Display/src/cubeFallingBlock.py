from libavg import avg


class cubeFallingBlock(object):



    def __init__(self, GameMenue, Field):
        
        self.part1 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (6 * GameMenue.blocksize), Field.yWertOben), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part2 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (7 * GameMenue.blocksize), Field.yWertOben), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part3 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (6 * GameMenue.blocksize), Field.yWertOben+ GameMenue.blocksize), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part4 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (7 * GameMenue.blocksize), Field.yWertOben+ GameMenue.blocksize), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        
        self.GameMenue = GameMenue
        self.Field = Field
        self.currPos1 = (6,0)
        self.currPos2 = (7,0)
        self.currPos3 = (6,1)
        self.currPos4 = (7,1)
        self.blockType = "cube" 
        
    
    def moveBlockLeft(self):
        if(self.checkLeftBound()):
            self.currPos1 = (self.currPos1[0] - 1,self.currPos1[1])
            self.currPos2 = (self.currPos2[0] - 1,self.currPos2[1])
            self.currPos3 = (self.currPos3[0] - 1,self.currPos3[1])
            self.currPos4 = (self.currPos4[0] - 1,self.currPos4[1])
            self.part1.pos = ((self.part1.pos[0] - self.GameMenue.blocksize),self.part1.pos[1])
            self.part2.pos = ((self.part2.pos[0] - self.GameMenue.blocksize),self.part2.pos[1])
            self.part3.pos = ((self.part3.pos[0] - self.GameMenue.blocksize),self.part3.pos[1])
            self.part4.pos = ((self.part4.pos[0] - self.GameMenue.blocksize),self.part4.pos[1])
        else:
            pass  # dont move dat shit
        
    def moveBlockRight(self):
        
        if(self.checkRightBound()):
            self.currPos1 = (self.currPos1[0] + 1,self.currPos1[1])
            self.currPos2 = (self.currPos2[0] + 1,self.currPos2[1])
            self.currPos3 = (self.currPos3[0] + 1,self.currPos3[1])
            self.currPos4 = (self.currPos4[0] + 1,self.currPos4[1])
            self.part1.pos = ((self.part1.pos[0] + self.GameMenue.blocksize),self.part1.pos[1])
            self.part2.pos = ((self.part2.pos[0] + self.GameMenue.blocksize),self.part2.pos[1])
            self.part3.pos = ((self.part3.pos[0] + self.GameMenue.blocksize),self.part3.pos[1])
            self.part4.pos = ((self.part4.pos[0] + self.GameMenue.blocksize),self.part4.pos[1])
        else:
            pass  # dont move dat shit
        
    def rotateLeft(self):
        pass
    
    def rotateRight(self):
        pass
    
    def hitGround(self): # gibt True zurueck, wenn es den "Boden" bzw ein Hindernis beruehrt, sonst False
        if((self.currPos1[1]+1 > 18) | (self.currPos2[1]+1 > 18) | (self.currPos3[1]+1 > 18) | (self.currPos4[1]+1 > 18)):
            return True
        else:
            a1 = self.Field.matrix[self.currPos3[0]][self.currPos3[1] + 1]   
            a2 = self.Field.matrix[self.currPos3[0]][self.currPos3[1] + 1]
            a3 = self.Field.matrix[self.currPos4[0]][self.currPos4[1] + 1]
            a4 = self.Field.matrix[self.currPos3[0]][self.currPos3[1] + 1]
            if (a1 | a2 | a3 | a4):
                return True
            else:
                return False

    def checkLeftBound(self): #return true wenn bewegung moeglich
        # pruefe part 1,3
        if((self.currPos1[0]-1 < 0)  | (self.currPos3[0]-1 < 0)):
            return False
        else:
            a = self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1]]
            b = self.Field.matrix[self.currPos3[0] - 1][self.currPos3[1]]
            if (a or b ):
                return False
            else:
                return True
 
            
    
    def checkRightBound(self):#return true wenn bewegung moeglich, prueft nur rechten unteren Block
        # pruefe part 2,4
        if((self.currPos2[0]+1 > 13) | (self.currPos4[0]+1 > 13) ):
            return False
        else:
            a = self.Field.matrix[self.currPos2[0] + 1][self.currPos2[1]]
            b = self.Field.matrix[self.currPos4[0] + 1][self.currPos4[1]]
            if (a or b ):
                return False
            else:
                return True