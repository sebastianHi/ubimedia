from libavg import avg

class BombBlock(object):



    def __init__(self, GameMenue, Field):
        
        self.Field = Field
        self.GameMenue = GameMenue
        
        self.part1 = avg.ImageNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (8 * GameMenue.blocksize), Field.yWertOben + GameMenue.blocksize), 
                                  fillcolor = "00FFFF", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize), href="bomb.png"
                                  )
        self.blockType = "bomb"
        self.currPos1 = (7,0)
        
    def moveBlockLeft(self):
        if(self.checkLeftBound()):
            self.currPos1 = (self.currPos1[0] - 1,self.currPos1[1])
            self.part1.pos = ((self.part1.pos[0] - self.GameMenue.blocksize),self.part1.pos[1])

        else:
            pass  # dont move dat shit
        
    def moveBlockRight(self):
        
        if(self.checkRightBound()):
            self.currPos1 = (self.currPos1[0] + 1,self.currPos1[1])
            self.part1.pos = ((self.part1.pos[0] + self.GameMenue.blocksize),self.part1.pos[1])

        else:
            pass  # dont move dat shit
        
    def hitGround(self): # gibt True zurueck, wenn es den "Boden" bzw ein Hindernis beruehrt, sonst False
        if(self.currPos1[1] + 1> 18 ):
            return True
        a = self.Field.matrix[self.currPos1[0]][self.currPos1[1] + 1]
        
        return a
    
    def checkLeftBound(self): #return true wenn bewegung moeglich
        
            if (self.currPos1[0] - 1 < 0):
                return False
            a = self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1]]
            return not a

            
    def checkRightBound(self):#return true wenn bewegung moeglich, prueft nur rechten unteren Block
       
            if (self.currPos1[0] + 1 > 13):
                return False
            a = self.Field.matrix[self.currPos1[0] + 1][self.currPos1[1]]
            
            return not a

    def explode(self): # deletes any active RectNodes surrounding the bomb
        
        #remove upper left block
        if ((self.currPos1[0] - 1 < 0) or (self.currPos1[1] - 1 < 0) or
            (self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1] - 1] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] - 1][self.currPos1[1] - 1]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] - 1][self.currPos1[1] - 1] = None
            self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1] - 1] = False
        
        #remove upper block    
        if ((self.currPos1[1] - 1 < 0) or
            (self.Field.matrix[self.currPos1[0]][self.currPos1[1] - 1] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0]][self.currPos1[1] - 1]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0]][self.currPos1[1] - 1] = None
            self.Field.matrix[self.currPos1[0]][self.currPos1[1] - 1] = False
            
        #remove upper right block
        if ((self.currPos1[0] + 1 > 13) or (self.currPos1[1] - 1 < 0) or
            (self.Field.matrix[self.currPos1[0] + 1][self.currPos1[1] - 1] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] + 1][self.currPos1[1] - 1]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] + 1][self.currPos1[1] - 1] = None
            self.Field.matrix[self.currPos1[0] + 1][self.currPos1[1] - 1] = False
        
        #remove left block
        if ((self.currPos1[0] - 1 < 0) or (self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1]] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] - 1][self.currPos1[1]]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] - 1][self.currPos1[1]] = None
            self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1]] = False
            
        #remove right block
        if ((self.currPos1[0] + 1 > 13) or (self.Field.matrix[self.currPos1[0] + 1][self.currPos1[1]] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] + 1][self.currPos1[1]]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] + 1][self.currPos1[1]] = None
            self.Field.matrix[self.currPos1[0] + 1][self.currPos1[1]] = False

        #remove lower left block
        if ((self.currPos1[0] - 1 < 0) or (self.currPos1[1] + 1 > 18) or
            (self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1] + 1] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] - 1][self.currPos1[1] + 1]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] - 1][self.currPos1[1] + 1] = None
            self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1] + 1] = False

        #remove lower block
        if ((self.currPos1[1] + 1 > 18) or (self.Field.matrix[self.currPos1[0]][self.currPos1[1] + 1] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0]][self.currPos1[1] + 1]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0]][self.currPos1[1] + 1] = None
            self.Field.matrix[self.currPos1[0]][self.currPos1[1] + 1] = False
            
        #remove lower right block
        if ((self.currPos1[0] + 1 > 13) or (self.currPos1[1] + 1 > 18) or
            (self.Field.matrix[self.currPos1[0] + 1][self.currPos1[1] + 1] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] + 1][self.currPos1[1] + 1]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] + 1][self.currPos1[1] + 1] = None
            self.Field.matrix[self.currPos1[0] + 1][self.currPos1[1] + 1] = False
            
        self.Field.player.clearInterval(self.Field.timer)
        self.Field.initBlock()
        self.Field.timer = self.Field.player.setInterval(500, self.Field.gravity)
        # eventuell hier noch sound abspielen einer explosion oder so

    def rotateLeft(self):
        pass
    
    def rotateRight(self):
        pass