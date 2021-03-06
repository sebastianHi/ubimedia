from libavg import avg

class rainDropBlock(object):

    #moveBlockLeft                :  Laesst block nach links bewegen
    #moveBlockRight               :  Laesst block nach rechts bewegen
    #rotateLeft                   :  Laesst block nach linkts rotieren
    #rotateRight                  :  Laesst block nach rechts rotieren
    #hitGround                    :  Gibt wahr zurueck, wenn hindernis unten beruehrt.

    def __init__(self, GameMenue, Field, CurrentPosition):
        
        
        self.Field = Field
        self.gameMenue = GameMenue
        self.part1 = avg.ImageNode(href = "raindrop.jpg", parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben + (CurrentPosition[0] * GameMenue.blocksize), Field.yWertOben),
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )


        self.blockType = "rain"
        self.currPos1 = CurrentPosition
    
    def moveBlockLeft(self):
        pass
    
    def moveBlockRight(self):
        pass
    
    def rotateLeft(self):
        pass
    
    def rotateRight(self):
        pass
 
    def hitGround(self): # gibt True zurueck, wenn es den "Boden" bzw ein Hindernis beruehrt, sonst False
        if(self.currPos1[1] + 1 > 18):
            return True
        a = self.Field.matrix[self.currPos1[0]][self.currPos1[1] + 1]
        return a