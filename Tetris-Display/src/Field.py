from FallingBlock import FallingBlock
from FallingBlocks import *
import random

class Field(object):

    def __init__(self, xWertLinksOben, xWertRechtsOben, yWertOben, yWertUnten, blocksize):
        self.xWertLinksOben = xWertLinksOben
        self.xWertRechtsOben = xWertRechtsOben
        self.yWertOben = yWertOben
        self.yWertUnten = yWertUnten
        self.gravity = 1
        #queue die gefuellt wird durch phone, new falling stone danach mit dem naechsten rufen
        self.Queue = []
        # Matrix hat die Form Matrix[0-13][0-19] und ist mit False initialisiert
        self.Matrix = [[False for i in range(20)] for j in range(14)]
        
        
        
    def generateRandomBlock(self):
        RandomNumber = random.randint(1,6)
        
        if (RandomNumber == 1):
            return cubeFallingBlock()
            
        elif (RandomNumber == 2):
            return IFallingBlock()
          
        elif (RandomNumber == 3):
            return LFallingBlock()
            
        elif (RandomNumber == 4):
            return reverseLFallingBlock()
            
        elif (RandomNumber == 5):
            return reverseZFallingBlock()
            
        else:
            return ZFallingBlock()
            
        
    
    def hitGround(self, node):#return true wenn bewegung moeglich
        pass
    
   
    def newFallingStone(self, node):#  <-- rufe stein, der macht den rest. gebe das feld mit.
        ##if queue leer dann random sonst erstes element der queue
        if not self.Queue:
            return self.generateRandomBlock()
        else:
            return self.Queue.pop()