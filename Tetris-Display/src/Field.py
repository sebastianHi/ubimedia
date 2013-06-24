from Gravity import Gravity
from FallingBlock import FallingBlock

class Field(object):

    def __init__(self, xWertLinksOben, xWertRechtsOben, yWertOben, yWertUnten):
        self.fallingBlock = FallingBlock()
        self.gravity = Gravity()
        pass
        
        
    def checkLeftBound(self, node): #return true wenn bewegung moeglich
        pass
    
    def checkRightBound(self, node):#return true wenn bewegung moeglich
        pass
    
    def hitGround(self, node):#return true wenn bewegung moeglich
        pass
    
    def gravity (self, value):
        pass
  
    def newFallingStone(self, node):
        pass
    