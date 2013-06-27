from FallingBlock import FallingBlock
from FallingBlocks import *
import random

class Field(object):

    def __init__(self, xWertLinksOben, xWertRechtsOben, yWertOben, yWertUnten, blocksize, player):
        self.player = player
        self.xWertLinksOben = xWertLinksOben
        self.xWertRechtsOben = xWertRechtsOben
        self.yWertOben = yWertOben
        self.yWertUnten = yWertUnten
        self.gravity = 1
        #queue die gefuellt wird durch phone, new falling stone danach mit dem naechsten rufen
        self.Queue = []
        # Matrix hat die Form Matrix[0-13][0-18] und ist mit False initialisiert
        self.Matrix = [[False for i in range(19)] for j in range(14)]
        self.matrixSteadyRectNodes = [[None for i in range(19)] for j in range(14)]
        self.initBlock();
        self.timer = self.player.setInterval(1000, self.gravity)
        
        
        
    def initBlock(self):
        self.block = self.newFallingStone()
        if(not (self.checkSpawn(self.block.blockType))):
            #TODO:  Someone lost!
            pass
    
    
    def blockHitGround(self):
        self.checkRows()
        self.initblock()
        self.timer = self.player.setInterval(1000, self.gravity)
        
    def steadyBlock(self):
        self.matrixSteadyRectNodes[self.currPos1[0]][self.currPos1[1]] = self.block.part1
        self.matrixSteadyRectNodes[self.currPos2[0]][self.currPos2[1]] = self.block.part2
        self.matrixSteadyRectNodes[self.currPos3[0]][self.currPos3[1]] = self.block.part3
        self.matrixSteadyRectNodes[self.currPos4[0]][self.currPos4[1]] = self.block.part4
        self.block.part1
        self.block.part2
        self.player.clearInterval(self.timer)
    
    def checkRows(self):
        breaked = False
        amountOfRows = 0
        while(breaked):
            for i  in range(14):
                b = True
                for j in range(20):
                    b = b & self.Matrix[i][j]
                if(b):
                    self.dropOneRow(j)
                    amountOfRows +=1
                    breaked = True
                    break
                else:
                    breaked = False
        if(amountOfRows>0):
            pass
        #TODO: update Money
    
    
    def dropOneRow(self, row):
        for l in range (14):
            self.Matrix[l][row] = False
            #TODO: nicht inactive sondern loeschen
            (self.matrixSteadyRectNodes[l][row]).inactive = False
            self.matrixSteadyRectNodes[l][row] = None
            
        j = row
        for i in range(14):
            for k in range(row+1,20):
                self.matrixSteadyRectNodes[i][j]= self.matrixSteadyRectNodes[i][k]
                self.Matrix[i][j] = self.matrix[i][k]
                self.matrixSteadyRectNodes[i][k] = None
                self.matrix[i][k] = False
                 
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
             
    def newFallingStone(self):#  <-- rufe stein, der macht den rest. gebe das feld mit.
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
        
    def deleteRows(self): # soll volle Reihen loeschen und Matrix und alles umsetzen
        pass
    
    def gravity(self):
        if(self.block.hitGround()):     
            self.steadyBlock()
            self.blockHitGround()
        else:
            self.block.currPos1 = self.currPos1[self.currPos1[0]][self.currPos1[1]+1]
            self.block.currPos2 = self.currPos2[self.currPos2[0]][self.currPos2[1]+1]
            self.block.currPos3 = self.currPos3[self.currPos3[0]][self.currPos3[1]+1]
            self.block.currPos4 = self.currPos4[self.currPos4[0]][self.currPos4[1]+1]
            self.block.part1.pos = (self.part1.pos[0],self.part1.pos[1] + self.GameMenue.blocksize)
            self.block.part2.pos = (self.part2.pos[0],self.part2.pos[1] + self.GameMenue.blocksize)
            self.block.part3.pos = (self.part3.pos[0],self.part3.pos[1] + self.GameMenue.blocksize)
            self.block.part4.pos = (self.part4.pos[0],self.part4.pos[1] + self.GameMenue.blocksize)
