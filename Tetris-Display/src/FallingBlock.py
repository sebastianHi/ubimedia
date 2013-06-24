'''
Created on 24.06.2013

@author: sebastian
'''

class fallingBlock(object):
  
    def __init__(self):
        pass
    
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