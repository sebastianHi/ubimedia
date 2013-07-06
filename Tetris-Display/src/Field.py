import crossFallingBlock,cubeFallingBlock,IFallingBlock, LFallingBlock, reverseLFallingBlock, reverseZFallingBlock, ZFallingBlock
import random


class Field(object):

    def __init__(self, xWertLinksOben, xWertRechtsOben, yWertOben, yWertUnten, blocksize, player,gameMenue):
        self.inverseSteuerung = False
        self.freezeLeft = False
        self.freezeRight = False
        self.freezeRotate = False
        self.speedToGround = False
        self.gameMenue = gameMenue
        self.player = player
        self.speed = 400
        self.gameMenue = gameMenue
        self.xWertLinksOben = xWertLinksOben
        self.xWertRechtsOben = xWertRechtsOben
        self.yWertOben = yWertOben
        self.yWertUnten = yWertUnten
        #queue die gefuellt wird durch phone, new falling stone danach mit dem naechsten rufen
        self.Queue = []
        # Matrix hat die Form Matrix[0-13][0-18] und ist mit False initialisiert
        self.matrix = [[False for i in range(19)] for j in range(14)] #@UnusedVariable
        self.matrixSteadyRectNodes = [[None for i in range(19)] for j in range(14)]#@UnusedVariable
        self.initBlock();
        self.timer = self.player.setInterval(self.speed, self.gravity)
        
        
        
    def initBlock(self):
        self.block = self.newFallingStone()
        if(not (self.checkSpawn(self.block.blockType))):
            #TODO:  Someone lost!
            pass
    
   
    def blockHitGround(self):
        self.checkRows()
        self.initBlock()
        self.timer = self.player.setInterval(500, self.gravity)
        
    
    def steadyBlock(self):
        self.matrixSteadyRectNodes[self.block.currPos1[0]][self.block.currPos1[1]] = self.block.part1
        self.matrixSteadyRectNodes[self.block.currPos2[0]][self.block.currPos2[1]] = self.block.part2
        self.matrixSteadyRectNodes[self.block.currPos3[0]][self.block.currPos3[1]] = self.block.part3
        self.matrixSteadyRectNodes[self.block.currPos4[0]][self.block.currPos4[1]] = self.block.part4
        self.matrix[self.block.currPos1[0]][self.block.currPos1[1]] = True
        self.matrix[self.block.currPos2[0]][self.block.currPos2[1]] = True
        self.matrix[self.block.currPos3[0]][self.block.currPos3[1]] = True
        self.matrix[self.block.currPos4[0]][self.block.currPos4[1]] = True
        self.player.clearInterval(self.timer)
        
        
#prints fuer felder
        for y in range(0,19):
            s = ""
            for x in range(0,14):
                if(self.matrix[x][y]):
                    s +=( str(y)+"  "+str(x)+": "+ str(self.matrix[x][y])+" " + "  ")
                else:
                    s +=( str(y)+"  "+str(x)+": "+ str(self.matrix[x][y]) + "  ")
            print s
            print ""
            print ""
                 
    
    
    def checkRows(self):
        breaked = True
        amountOfRows = 0
        while(breaked):
            for j  in range(0,19):
                b = True
                for i in range(0,14):
                    b = b & (self.matrix[i][j])
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
            self.matrix[l][row] = False
            (self.matrixSteadyRectNodes[l][row]).unlink()
            self.matrixSteadyRectNodes[l][row] = None
         
        for spalte in range (14):
            for reihe in range(row,0,-1):
                self.matrix[spalte][reihe] = self.matrix[spalte][reihe-1]
                self.matrix[spalte][reihe-1] = False
                self.matrixSteadyRectNodes[spalte][reihe] = self.matrixSteadyRectNodes[spalte][reihe-1]
                self.matrixSteadyRectNodes[spalte][reihe-1] = None
                if(self.matrix[spalte][reihe]):
                    (self.matrixSteadyRectNodes[spalte][reihe]).pos = (self.matrixSteadyRectNodes[spalte][reihe].pos[0],self.matrixSteadyRectNodes[spalte][reihe].pos[1] + self.gameMenue.blocksize)           
         
        for s in range (14):
            self.matrix[s][0] = False
            self.matrixSteadyRectNodes[s][0] = None

        for y in range(0,19):
            s = ""
            for x in range(0,14):
                if(self.matrix[x][y]):
                    s +=( str(y)+"  "+str(x)+": "+ str(self.matrix[x][y])+" " + "  ")
                else:
                    s +=( str(y)+"  "+str(x)+": "+ str(self.matrix[x][y]) + "  ")
            print s
            print ""
            print ""
                
                 
    
    def generateRandomBlock(self):
        RandomNumber = random.randint(1,7)
###########################################################################################################################################
# je nachdem was du erzeugst  1-7
###########################################################################################################################################
        if (RandomNumber == 1):
            a = self.checkSpawn("cube")
            if a:
                return cubeFallingBlock.cubeFallingBlock(self.gameMenue, self)
            else:
                pass # spawn geht nicht - Spiel beenden oder neue Runde
            
        elif (RandomNumber == 2):
            a = self.checkSpawn("I")
            if a:
                return IFallingBlock.IFallingBlock(self.gameMenue, self)
            else:
                pass  # spawn geht nicht - Spiel beenden oder neue Runde
          
        elif (RandomNumber == 3):
            a = self.checkSpawn("L")
            if a:
                return LFallingBlock.LFallingBlock(self.gameMenue, self)
            else:
                pass  # spawn geht nicht - Spiel beenden oder neue Runde
            
        elif (RandomNumber == 4):
            a = self.checkSpawn("reverseL")
            if a:
                return reverseLFallingBlock.reverseLFallingBlock(self.gameMenue, self)
            else:
                pass  # spawn geht nicht - Spiel beenden oder neue Runde
            
        elif (RandomNumber == 5):
            a = self.checkSpawn("reverseZ")
            if a:
                return reverseZFallingBlock.reverseZFallingBlock(self.gameMenue, self)
            else:
                pass  # spawn geht nicht - Spiel beenden oder neue Runde
            
        elif (RandomNumber == 6):
            a = self.checkSpawn("Z")
            if a:
                return ZFallingBlock.ZFallingBlock(self.gameMenue, self)
            else:
                pass  # spawn geht nicht - Spiel beenden oder neue Runde
        else:
            a = self.checkSpawn("cross")
            if a: 
                return crossFallingBlock.crossFallingBlock(self.gameMenue, self)
            else:
                pass  # spawn geht nicht - Spiel beenden oder neue Runde
    
    
    def newFallingStone(self):#  <-- rufe stein, der macht den rest. gebe das feld mit.
        ##if queue leer dann random sonst erstes element der queue
        if not self.Queue:
            return self.generateRandomBlock()
        else:
            a = self.Queue.pop()
            b = self.checkSpawn(a)
            if b:
                if (a == "cube"):
                    return cubeFallingBlock.cubeFallingBlock(self.gameMenue, self)
                elif (a == "I"):
                    return IFallingBlock.IFallingBlock(self.gameMenue, self)
                elif (a== "L"):
                    return LFallingBlock.LFallingBlock(self.gameMenue, self)
                elif (a == "Z"):
                    return ZFallingBlock.ZFallingBlock(self.gameMenue, self)
                elif (a == "reverseL"):
                    return reverseLFallingBlock.reverseLFallingBlock(self.gameMenue, self)
                elif (a == "reverseZ"):
                    return reverseZFallingBlock.reverseZFallingBlock(self.gameMenue, self)
                elif (a == "cross"):
                    return crossFallingBlock.crossFallingBlock(self.gameMenue,self)
                else:
                    pass
            else: 
                pass # spawn geht nicht - Spiel beenden oder neue Runde
        
    
    def checkSpawn(self, string):
        if (string == "cube"):
            if (self.matrix[7][0] == True) or (self.matrix[8][0] == True) or (self.matrix[7][1] == True) or (self.matrix[8][1] == True):
                return False
            else: 
                return True
        elif (string == "I"):
            if (self.matrix[6][0] == True) or (self.matrix[7][0] == True) or (self.matrix[8][0] == True) or (self.matrix[9][0] == True):
                return False
            else: 
                return True
        elif (string == "Z"):
            if (self.matrix[6][0] == True) or (self.matrix[7][0] == True) or (self.matrix[7][1] == True) or (self.matrix[8][1] == True):
                return False
            else: 
                return True
        elif (string == "reverseZ"):
            if (self.matrix[7][0] == True) or (self.matrix[8][0] == True) or (self.matrix[6][1] == True) or (self.matrix[7][1] == True):
                return False
            else: 
                return True
        elif (string == "L"):
            if (self.matrix[6][0] == True) or (self.matrix[7][0] == True) or (self.matrix[8][0] == True) or (self.matrix[6][1] == True):
                return False
            else: 
                return True
        elif (string == "reverseL"):
            if (self.matrix[6][0] == True) or (self.matrix[7][0] == True) or (self.matrix[8][0] == True) or (self.matrix[8][1] == True):
                return False
            else: 
                return True
        elif (string == "cross"):
            if (self.matrix[6][0] == True) or (self.matrix[7][0] == True) or (self.matrix[8][0] == True) or (self.matrix[7][1] == True):
                return False
            else:
                return True
        else:
            return False
        
    
    def deleteRows(self): # soll volle Reihen loeschen und Matrix und alles umsetzen
        pass
    
    
    def gravity(self):
        #test
        if(self.block.hitGround()):     
            self.steadyBlock()
            self.blockHitGround()
        else:
            self.block.currPos1 = (self.block.currPos1[0] ,self.block.currPos1[1] +1)
            self.block.currPos2 = (self.block.currPos2[0] ,self.block.currPos2[1] +1)
            self.block.currPos3 = (self.block.currPos3[0] ,self.block.currPos3[1] +1)
            self.block.currPos4 = (self.block.currPos4[0] ,self.block.currPos4[1] +1)  
            self.block.part1.pos = (self.block.part1.pos[0],self.block.part1.pos[1] + self.gameMenue.blocksize)
            self.block.part2.pos = (self.block.part2.pos[0],self.block.part2.pos[1] + self.gameMenue.blocksize)
            self.block.part3.pos = (self.block.part3.pos[0],self.block.part3.pos[1] + self.gameMenue.blocksize)
            self.block.part4.pos = (self.block.part4.pos[0],self.block.part4.pos[1] + self.gameMenue.blocksize)
            
            
###########################################################################################################################################
            #i = random.randint(0,3)
            #self.randomMove(i)  # methode hinschreiben die nach jeder gravity ausgefuehrt werden soll
###########################################################################################################################################

        
    def moveLeft(self):
        if((self.block == None) | self.freezeLeft):
            pass
        elif(self.inverseSteuerung):
            self.block.moveBlockRight()
        else:
            self.block.moveBlockLeft()
    
    
    def moveRight(self):
        if((self.block == None)| self.freezeRight):
            pass
        elif(self.inverseSteuerung):
            self.block.moveBlockLeft()
        else:
            self.block.moveBlockRight()
    
    
    def rotateLeft(self):
        if((self.block == None)| self.freezeRotate):
            pass
        elif(self.inverseSteuerung):
            self.block.rotateRight()
        else:
            self.block.rotateLeft()
            
    
    def rotateRight(self):
        if((self.block == None)| self.freezeRotate):
            pass
        elif(self.inverseSteuerung):
            self.block.rotateLeft()
        else:
            self.block.rotateRight()
            
    def speedDown(self):
        self.chanceSpeed(50)
            
    def chanceSpeed(self, newSpeedInMs):
        self.player.clearInterval(self.timer)
        self.timer = self.player.setInterval(newSpeedInMs, self.gravity)
        
    def randomMove(self, integer):
        if (integer == 1):
            self.block.rotateLeft()
        elif (integer == 2):
            self.block.rotateRight()
        elif (integer == 3):
            self.block.moveBlockLeft()
        else:
            self.block.moveBlockRight()    