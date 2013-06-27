'''
Created on 24.06.2013

@author: sebastian
'''

class FallingBlock(object):
  
    
    ####hier stone generator
        
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