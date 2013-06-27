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
            a = self.checkSpawn("cube")
            if (a == True):
                return cubeFallingBlock()
            else:
                pass # throw shit
            
        elif (RandomNumber == 2):
            a = self.checkSpawn("I")
            if (a == True):
                return IFallingBlock()
            else:
                pass
          
        elif (RandomNumber == 3):
            a = self.checkSpawn("L")
            if (a == True):
                return LFallingBlock()
            else:
                pass
            
        elif (RandomNumber == 4):
            a = self.checkSpawn("reverseL")
            if (a == True):
                return reverseLFallingBlock()
            else:
                pass
            
        elif (RandomNumber == 5):
            a = self.checkSpawn("reverseZ")
            if (a == True):
                return reverseZFallingBlock()
            else:
                pass
        else:
            a = self.checkSpawn("Z")
            if (a == True):
                return ZFallingBlock()
            else:
                pass
            
        
    
    def hitGround(self, node):#return true wenn bewegung moeglich
        pass
    
   
    def newFallingStone(self, node):#  <-- rufe stein, der macht den rest. gebe das feld mit.
        ##if queue leer dann random sonst erstes element der queue
        if not self.Queue:
            return self.generateRandomBlock()
        else:
            a = self.Queue.pop()
            b = self.checkSpawn(a)
            if (b == True):
                if (a == "cube"):
                    return cubeFallingBlock()
                elif (a == "I"):
                    return IFallingBlock()
                elif (a== "L"):
                    return LFallingBlock()
                elif (a == "Z"):
                    return ZFallingBlock()
                elif (a == "reverseL"):
                    return reverseLFallingBlock()
                elif (a == "reverseZ"):
                    return reverseZFallingBlock()
                else:
                    pass
            else: 
                pass # throw shit
        
    def checkSpawn(self, string):
        if (string == "cube"):
            if (self.matrix[6][0] == True) or (self.matrix[7][0] == True) or (self.matrix[6][1] == True) or (self.matrix[7][1] == True):
                return False
            else: 
                return True
        elif (string == "I"):
            if (self.matrix[5][0] == True) or (self.matrix[6][0] == True) or (self.matrix[7][0] == True) or (self.matrix[8][0] == True):
                return False
            else: 
                return True
        elif (string == "Z"):
            if (self.matrix[5][0] == True) or (self.matrix[6][0] == True) or (self.matrix[6][1] == True) or (self.matrix[7][1] == True):
                return False
            else: 
                return True
        elif (string == "reverseZ"):
            if (self.matrix[6][0] == True) or (self.matrix[7][0] == True) or (self.matrix[5][1] == True) or (self.matrix[6][1] == True):
                return False
            else: 
                return True
        elif (string == "L"):
            if (self.matrix[5][0] == True) or (self.matrix[6][0] == True) or (self.matrix[7][0] == True) or (self.matrix[8][0] == True):
                return False
            else: 
                return True
        elif (string == "reverseL"):
            if (self.matrix[5][0] == True) or (self.matrix[6][0] == True) or (self.matrix[7][0] == True) or (self.matrix[8][0] == True):
                return False
            else: 
                return True
        else:
            return False
        
    def deleteRows(self): # soll volle Reihen löschen und Matrix und alles umsetzen
        pass
    
    
