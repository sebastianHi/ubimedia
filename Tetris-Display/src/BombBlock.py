from libavg import avg

class BombBlock(object):
    #moveBlockLeft        :  Laesst block nach links bewegen
    #moveBlockRight       :  Laesst block nach rechts bewegen
    #rotateLeft           :  Laesst block nach linkts rotieren
    #rotateRight          :  Laesst block nach rechts rotieren
    #hitGround            :  Gibt wahr zurueck, wenn hindernis unten beruehrt.
    #checkRightBound      :  Gibt false zurueck, wenn ein hindernis rechts befindetet
    #checkLeftBound       :  Gibt false zurueck, wenn ein hindernis links befindetet
    #explode              :  Loescht Bloecke mit Radius 2 um sich herum


    def __init__(self, GameMenue, Field):
        
        self.Field = Field
        self.gameMenue = GameMenue
        
        self.part1 = avg.ImageNode(href="bomb.png", parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (7 * GameMenue.blocksize), Field.yWertOben),  
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize), 
                                  )
        self.blockType = "bomb"
        self.currPos1 = (7,0)
        
    def moveBlockLeft(self):
        if(self.checkLeftBound()):
            self.currPos1 = (self.currPos1[0] - 1,self.currPos1[1])
            self.part1.pos = ((self.part1.pos[0] - self.gameMenue.blocksize),self.part1.pos[1])

        else:
            pass  # dont move dat shit
        
    def moveBlockRight(self):
        
        if(self.checkRightBound()):
            self.currPos1 = (self.currPos1[0] + 1,self.currPos1[1])
            self.part1.pos = ((self.part1.pos[0] + self.gameMenue.blocksize),self.part1.pos[1])

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

    def explode(self): # deletes any active RectNodes surrounding the bomb in a radius of 2
        
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
#---------------------------------radius 2 now -----------------------------------------------------------------            
        #remove top left block
        if ((self.currPos1[0] - 2 < 0) or (self.currPos1[1] - 2 < 0) or
            (self.Field.matrix[self.currPos1[0] - 2][self.currPos1[1] - 2] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] - 2][self.currPos1[1] - 2]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] - 2][self.currPos1[1] - 2] = None
            self.Field.matrix[self.currPos1[0] - 2][self.currPos1[1] - 2] = False
        
        #remove top left center block
        if ((self.currPos1[0] - 1 < 0) or (self.currPos1[1] - 2 < 0) or
            (self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1] - 2] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] - 1][self.currPos1[1] - 2]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] - 1][self.currPos1[1] - 2] = None
            self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1] - 2] = False
        
        #remove top block    
        if ((self.currPos1[1] - 2 < 0) or
            (self.Field.matrix[self.currPos1[0]][self.currPos1[1] - 2] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0]][self.currPos1[1] - 2]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0]][self.currPos1[1] - 2] = None
            self.Field.matrix[self.currPos1[0]][self.currPos1[1] - 2] = False
            
        #remove top right center block
        if ((self.currPos1[0] + 1 > 13) or (self.currPos1[1] - 2 < 0) or
            (self.Field.matrix[self.currPos1[0] + 1][self.currPos1[1] - 2] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] + 1][self.currPos1[1] - 2]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] + 1][self.currPos1[1] - 2] = None
            self.Field.matrix[self.currPos1[0] + 1][self.currPos1[1] - 2] = False
            
        #remove top right block
        if ((self.currPos1[0] + 2 > 13) or (self.currPos1[1] - 2 < 0) or
            (self.Field.matrix[self.currPos1[0] + 2][self.currPos1[1] - 2] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] + 2][self.currPos1[1] - 2]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] + 2][self.currPos1[1] - 2] = None
            self.Field.matrix[self.currPos1[0] + 2][self.currPos1[1] - 2] = False
        
        #remove far upper left center block
        if ((self.currPos1[0] - 2 < 0) or (self.currPos1[1] - 1 < 0) or 
            (self.Field.matrix[self.currPos1[0] - 2][self.currPos1[1] - 1] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] - 2][self.currPos1[1] - 1]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] - 2][self.currPos1[1] - 1] = None
            self.Field.matrix[self.currPos1[0] - 2][self.currPos1[1] - 1] = False
            
        #remove far left block
        if ((self.currPos1[0] - 2 < 0) or (self.Field.matrix[self.currPos1[0] - 2][self.currPos1[1]] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] - 2][self.currPos1[1]]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] - 2][self.currPos1[1]] = None
            self.Field.matrix[self.currPos1[0] - 2][self.currPos1[1]] = False
            
        #remove far lower left center block
        if ((self.currPos1[0] - 2 < 0) or (self.currPos1[1] + 1 > 18) or 
            (self.Field.matrix[self.currPos1[0] - 2][self.currPos1[1] + 1] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] - 2][self.currPos1[1] + 1]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] - 2][self.currPos1[1] + 1] = None
            self.Field.matrix[self.currPos1[0] - 2][self.currPos1[1] + 1] = False
            
        #remove far upper right center block
        if ((self.currPos1[0] + 2 > 13) or (self.currPos1[1] - 1 < 0) or 
            (self.Field.matrix[self.currPos1[0] + 2][self.currPos1[1] - 1] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] + 2][self.currPos1[1] - 1]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] + 2][self.currPos1[1] - 1] = None
            self.Field.matrix[self.currPos1[0] + 2][self.currPos1[1] - 1] = False
            
        #remove far right block
        if ((self.currPos1[0] + 2 > 13) or (self.Field.matrix[self.currPos1[0] + 2][self.currPos1[1]] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] + 2][self.currPos1[1]]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] + 2][self.currPos1[1]] = None
            self.Field.matrix[self.currPos1[0] + 2][self.currPos1[1]] = False
            
        #remove far lower right center block
        if ((self.currPos1[0] + 2 > 13) or (self.currPos1[1] + 1 > 18) or 
            (self.Field.matrix[self.currPos1[0] + 2][self.currPos1[1] + 1] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] + 2][self.currPos1[1] + 1]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] + 2][self.currPos1[1] + 1] = None
            self.Field.matrix[self.currPos1[0] + 2][self.currPos1[1] + 1] = False

        #remove bottom left block
        if ((self.currPos1[0] - 2 < 0) or (self.currPos1[1] + 2 > 18) or
            (self.Field.matrix[self.currPos1[0] - 2][self.currPos1[1] + 2] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] - 2][self.currPos1[1] + 2]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] - 2][self.currPos1[1] + 2] = None
            self.Field.matrix[self.currPos1[0] - 2][self.currPos1[1] + 2] = False

        #remove bottom left center block
        if ((self.currPos1[0] - 1 < 0) or (self.currPos1[1] + 2 > 18) or
            (self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1] + 2] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] - 1][self.currPos1[1] + 2]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] - 1][self.currPos1[1] + 2] = None
            self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1] + 2] = False
            
        #remove bottom block
        if ((self.currPos1[1] + 2 > 18) or (self.Field.matrix[self.currPos1[0]][self.currPos1[1] + 2] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0]][self.currPos1[1] + 2]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0]][self.currPos1[1] + 2] = None
            self.Field.matrix[self.currPos1[0]][self.currPos1[1] + 2] = False
            
        #remove bottom right center block
        if ((self.currPos1[0] + 1 > 13) or (self.currPos1[1] + 2 > 18) or
            (self.Field.matrix[self.currPos1[0] + 1][self.currPos1[1] + 2] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] + 1][self.currPos1[1] + 2]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] + 1][self.currPos1[1] + 2] = None
            self.Field.matrix[self.currPos1[0] + 1][self.currPos1[1] + 2] = False
            
        #remove bottom right block
        if ((self.currPos1[0] + 2 > 13) or (self.currPos1[1] + 2 > 18) or
            (self.Field.matrix[self.currPos1[0] + 2][self.currPos1[1] + 2] == False)):
            pass
        else:
            (self.Field.matrixSteadyRectNodes[self.currPos1[0] + 2][self.currPos1[1] + 2]).unlink()
            self.Field.matrixSteadyRectNodes[self.currPos1[0] + 2][self.currPos1[1] + 2] = None
            self.Field.matrix[self.currPos1[0] + 2][self.currPos1[1] + 2] = False
        self.gameMenue.playSound("bomb")    
        self.Field.player.clearInterval(self.Field.timer)
        self.part1.unlink()
        self.Field.bombActivated = False
        self.Field.blockHitGround("Bomb")
        # eventuell hier noch sound abspielen einer explosion oder so

    def rotateLeft(self):
        pass
    
    def rotateRight(self):
        pass