'''
Created on 26.06.2013

@author: sebastian
'''
from libavg import avg
from src import FallingBlock,GameMenue

class IFallingBlock(FallingBlock):



    def __init__(self, GameMenue):
        
        self.part1 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (GameMenue.linksFeld1X+ (6 * GameMenue.blocksize), GameMenue.yOben), 
                                  fillcolor = "FFFF00", fillopacity = 1, color = "FFFF00", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part2 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (GameMenue.linksFeld1X+ (7 * GameMenue.blocksize), GameMenue.yOben), 
                                  fillcolor = "FFFF00", fillopacity = 1, color = "FFFF00", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part3 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (GameMenue.linksFeld1X+ (8 * GameMenue.blocksize), GameMenue.yOben), 
                                  fillcolor = "FFFF00", fillopacity = 1, color = "FFFF00", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part4 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (GameMenue.linksFeld1X+ (9 * GameMenue.blocksize), GameMenue.yOben), 
                                  fillcolor = "FFFF00", fillopacity = 1, color = "FFFF00", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.currPos1 = (5,0)
        self.currPos2 = (6,0)
        self.currPos3 = (7,0)
        self.currPos4 = (8,0)
        
    def moveBlockLeft(self, node):
        if(self.checkLeftBound(self.fallingBlock)):
            self.fallingBlock.pos = (self.fallingBlock.pos[0] - self.blocksize,self.fallingBlock.pos[0])
        
    def moveBlockRight(self, node):
        pass
    
    def rotateLeft(self, node):
        pass
    
    def rotateRight(self, node):
        pass
    
    
    def hitGround(self): #<-- ruf feld.hitground auf um zu zeigen neuer stein kann fallen.
        pass
    
    def checkLeftBound(self, node): #return true wenn bewegung moeglich
        pass
    
    def checkRightBound(self, node):#return true wenn bewegung moeglich
        pass