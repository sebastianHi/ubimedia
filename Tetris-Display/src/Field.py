import rainDropBlock, superBlock, BombBlock, crossFallingBlock,cubeFallingBlock,IFallingBlock, LFallingBlock, reverseLFallingBlock, reverseZFallingBlock, ZFallingBlock
import random
from libavg import avg

class Field(object):

    def __init__(self, xWertLinksOben, xWertRechtsOben, yWertOben, yWertUnten, blocksize, player,gameMenue):
        self.score = 0
        self.gameMenue = gameMenue
        if(xWertLinksOben <= (self.gameMenue.divNodeGameMenue.size[0]/2)):
            self.feldScore = self.gameMenue.scoreTeam1
        else:
            self.feldScore = self.gameMenue.scoreTeam2
        self.inverseSteuerung = False
        self.freezeLeft = False
        self.freezeRight = False
        self.freezeRotate = False
        self.speedToGround = False
        self.superBlock = False
        self.bombActivated = False
        self.thunderActivated = False
        self.tetrisRainActivated = True
        self.noMoneyForYou = False
        self.rainDropCount = 0
        self.player = player
        self.speed = self.gameMenue.speed[0]
        self.xWertLinksOben = xWertLinksOben
        self.xWertRechtsOben = xWertRechtsOben
        self.yWertOben = yWertOben
        self.yWertUnten = yWertUnten
        #queue die gefuellt wird durch phone, new falling stone danach mit dem naechsten rufen
        self.Queue = []
        # Matrix hat die Form Matrix[0-13][0-18] und ist mit False initialisiert
        self.matrix = [[False for i in range(19)] for j in range(14)] #@UnusedVariable
        self.matrixSteadyRectNodes = [[None for i in range(19)] for j in range(14)]#@UnusedVariable
        self.timer = self.player.setInterval(self.speed, self.gravity)
        self.initBlock();

             
    def initBlock(self):
        self.block = self.newFallingStone()  
   
    def blockHitGround(self):
        self.checkRows()
        self.initBlock()
        self.timer = self.player.setInterval(self.speed, self.gravity)
        
    
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
        
        
# #prints fuer felder
#         for y in range(0,19):
#             s = ""
#             for x in range(0,14):
#                 if(self.matrix[x][y]):
#                     s +=( str(y)+"  "+str(x)+": "+ str(self.matrix[x][y])+" " + "  ")
#                 else:
#                     s +=( str(y)+"  "+str(x)+": "+ str(self.matrix[x][y]) + "  ")
#             print s
#             print ""
#             print ""
                  
    def checkRows(self):
        amountOfRows = 0
        for j  in range(0,19):
            b = True
            for i in range(0,14):
                b = b & (self.matrix[i][j])
            if(b):
                self.dropOneRow(j)
                amountOfRows +=1
                j-=1
                
        if(amountOfRows>0):
            if (self.noMoneyForYou):
                this = avg.SoundNode(href="denied.mp3", loop=False, volume=1.0, parent = self.gameMenue.rootNode)
                this.play()
            else:
                self.updateScore(amountOfRows)
        
    def updateScore(self, points):
        self.score += points
        s = ""
        for strg in self.feldScore.text:
            if(strg == ':'):
                s += strg
                break
            s += strg
        s += " "
        s += str(self.score)
        self.feldScore.text = s
    
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
        this = avg.SoundNode(href="cash.mp3", loop=False, volume=1.0, parent = self.gameMenue.rootNode)
        this.play()
#         for y in range(0,19):
#             s = ""
#             for x in range(0,14):
#                 if(self.matrix[x][y]):
#                     s +=( str(y)+"  "+str(x)+": "+ str(self.matrix[x][y])+" " + "  ")
#                 else:
#                     s +=( str(y)+"  "+str(x)+": "+ str(self.matrix[x][y]) + "  ")
#             print s
#             print ""
#             print ""
                   
    def generateRandomBlock(self):
        RandomNumber = random.randint(1,7)

        if (RandomNumber == 1):
            a = self.checkSpawn("cube")
            if a:
                return cubeFallingBlock.cubeFallingBlock(self.gameMenue, self)
            else:
                self.gameMenue.endeSpiel()
            
        elif (RandomNumber == 2):
            a = self.checkSpawn("I")
            if a:
                return IFallingBlock.IFallingBlock(self.gameMenue, self)
            else:
                self.gameMenue.endeSpiel()
          
        elif (RandomNumber == 3):
            a = self.checkSpawn("L")
            if a:
                return LFallingBlock.LFallingBlock(self.gameMenue, self)
            else:
                self.gameMenue.endeSpiel()
            
        elif (RandomNumber == 4):
            a = self.checkSpawn("reverseL")
            if a:
                return reverseLFallingBlock.reverseLFallingBlock(self.gameMenue, self)
            else:
                self.gameMenue.endeSpiel()
            
        elif (RandomNumber == 5):
            a = self.checkSpawn("reverseZ")
            if a:
                return reverseZFallingBlock.reverseZFallingBlock(self.gameMenue, self)
            else:
                self.gameMenue.endeSpiel() 
            
        elif (RandomNumber == 6):
            a = self.checkSpawn("Z")
            if a:
                return ZFallingBlock.ZFallingBlock(self.gameMenue, self)
            else:
                self.gameMenue.endeSpiel()
        else:
            a = self.checkSpawn("cross")
            if a: 
                return crossFallingBlock.crossFallingBlock(self.gameMenue, self)
            else:
                self.gameMenue.endeSpiel() 
    
    
    def newFallingStone(self):#  <-- rufe stein, der macht den rest. gebe das feld mit.
        
        if (self.tetrisRainActivated and self.rainDropCount == 0):
            this = avg.SoundNode(href="rain.mp3", loop=False, volume=1.0, parent = self.gameMenue.rootNode)
            this.play()
            block = self.letItRain()
            self.rainDropCount += 1
            if (self.rainDropCount > 29):
                
                self.tetrisRainActivated = False
                self.rainDropCount = 0
                self.gravityPausieren()
                self.gravityWiederStarten()
            return block
        
        elif (self.tetrisRainActivated):
            block = self.letItRain()
            self.rainDropCount += 1
            if (self.rainDropCount > 30):
                
                self.tetrisRainActivated = False
                self.rainDropCount = 0
                self.gravityPausieren()
                self.gravityWiederStarten()
            return block
        
        elif(self.thunderActivated):
            this = avg.SoundNode(href="thunder.wav", loop=False, volume=1.0, parent = self.gameMenue.rootNode)
            this.play()
            randomNumber = random.randint(0,13)
            for i in range(19):
                randomInc = random.randint(-1,1)
                if ((self.matrix[randomNumber][i] < 0) or (self.matrix[randomNumber][i] > 13)):
                    randomNumber += randomInc
                    if (randomNumber < 0):
                        randomNumber = 0
                    elif (randomNumber > 13):
                        randomNumber = 13
                    else:
                        pass
                else:
                    self.matrix[randomNumber][i] = False
                    if (self.matrixSteadyRectNodes[randomNumber][i] is not None):
                        (self.matrixSteadyRectNodes[randomNumber][i]).unlink()
                        self.matrixSteadyRectNodes[randomNumber][i] = None
                        randomNumber += randomInc
                        if (randomNumber < 0):
                            randomNumber = 0
                        elif (randomNumber > 13):
                            randomNumber = 13
                        else:
                            pass
                    else:
                        randomNumber += randomInc
                        if (randomNumber < 0):
                            randomNumber = 0
                        elif (randomNumber > 13):
                            randomNumber = 13
                        else:
                            pass
            self.thunderActivated = False
            block = self.newFallingStone()
            return block
             
        elif (self.bombActivated):
            
            bomb = BombBlock.BombBlock(self.gameMenue,self)
            a = self.checkSpawn("bomb")
            if (a):
                return bomb
            else:
                bomb.explode()
                
        elif (self.superBlock):
            a = self.checkSpawn("super")
            if (a):
                return superBlock.superBlock(self.gameMenue, self)
            else:
                self.gameMenue.endeSpiel()

        ##if queue leer dann random sonst erstes element der queue
        elif not self.Queue:
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
                self.gameMenue.endeSpiel()
        
    
    def checkSpawn(self, string): # returns False if spawn is not possible, true otherwise
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
        elif (string == "bomb"):
            if (self.matrix[7][0] == True):
                return False
            else:
                return True
        elif (string == "super"):
            if ((self.matrix[6][0] == True) or (self.matrix[5][1] == True) or (self.matrix[6][1] == True) 
                or (self.matrix[4][2] == True) or (self.matrix[5][2] == True) or (self.matrix[7][2] == True) 
                or (self.matrix[8][2] == True) or (self.matrix[6][3] == True) or (self.matrix[7][3] == True) 
                or (self.matrix[6][4] == True)):
                return False
            else:
                return True
        else:
            return False

    def gravity(self):
        if (self.block is None):
            pass
        elif (self.block.blockType == "bomb"):
            if (self.block.hitGround()):
                self.block.explode()
            else:
                self.block.currPos1 = (self.block.currPos1[0] ,self.block.currPos1[1] + 1)
                self.block.part1.pos = (self.block.part1.pos[0],self.block.part1.pos[1] + self.gameMenue.blocksize)
        elif (self.block.blockType == "super"):
            if (self.block.hitGround()):
                self.block.steadyBlockSuper()
                self.superBlock = False
                self.blockHitGround()
               
            else:
                self.block.setBlock()
        elif (self.block.blockType == "rain"):
            if (self.block.hitGround()):
                self.matrixSteadyRectNodes[self.block.currPos1[0]][self.block.currPos1[1]] = self.block.part1
                self.matrix[self.block.currPos1[0]][self.block.currPos1[1]] = True
                self.checkRows()
                self.initBlock()
            else:
                self.block.currPos1 = (self.block.currPos1[0] ,self.block.currPos1[1] + 1)
                self.block.part1.pos = (self.block.part1.pos[0],self.block.part1.pos[1] + self.gameMenue.blocksize)
        #test
        elif(self.block.hitGround()):     
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
            

        
    def moveLeft(self):
        if((self.block is None) | self.freezeLeft):
            this = avg.SoundNode(href="denied.mp3", loop=False, volume=1.0, parent = self.gameMenue.rootNode)
            this.play()
        elif(self.inverseSteuerung):
            self.block.moveBlockRight()
        else:
            self.block.moveBlockLeft()
    
    
    def moveRight(self):
        if((self.block is None)| self.freezeRight):
            this = avg.SoundNode(href="denied.mp3", loop=False, volume=1.0, parent = self.gameMenue.rootNode)
            this.play()
        elif(self.inverseSteuerung):
            self.block.moveBlockLeft()
        else:
            self.block.moveBlockRight()
    
    
    def rotateLeft(self):
        if((self.block is None)| self.freezeRotate):
            this = avg.SoundNode(href="denied.mp3", loop=False, volume=1.0, parent = self.gameMenue.rootNode)
            this.play()
        elif(self.inverseSteuerung):
            this = avg.SoundNode(href="rotate.wav", loop=False, volume=1.0, parent = self.gameMenue.rootNode)
            this.play()
            self.block.rotateRight()
        else:
            this = avg.SoundNode(href="rotate.wav", loop=False, volume=1.0, parent = self.gameMenue.rootNode)
            this.play()
            self.block.rotateLeft()
            
    
    def rotateRight(self):
        if((self.block is None)| self.freezeRotate):
            this = avg.SoundNode(href="denied.mp3", loop=False, volume=1.0, parent = self.gameMenue.rootNode)
            this.play()
        elif(self.inverseSteuerung):
            this = avg.SoundNode(href="rotate.wav", loop=False, volume=1.0, parent = self.gameMenue.rootNode)
            this.play()
            self.block.rotateLeft()
        else:
            this = avg.SoundNode(href="rotate.wav", loop=False, volume=1.0, parent = self.gameMenue.rootNode)
            this.play()
            self.block.rotateRight()
            
    def speedDown(self):
        self.chanceSpeed(50)
            
    def chanceSpeed(self, newSpeedInMs):
        self.player.clearInterval(self.timer)
        self.timer = self.player.setInterval(newSpeedInMs, self.gravity)
    
    def equalModus(self):
        for reihe in range(0,10):
            for spalte in range (14):
                if(self.matrix[spalte][reihe]):
                    self.matrix[spalte][reihe] = False
                    (self.matrixSteadyRectNodes[spalte][reihe]).unlink()
                    self.matrixSteadyRectNodes[spalte][reihe] = None
    
    def clearForNextRound(self):
        self.player.clearInterval(self.timer)
        
        if(self.block.blockType == "super"):
            self.block.part1.unlink()
            self.block.part2.unlink()
            self.block.part3.unlink()
            self.block.part4.unlink()
            self.block.part5.unlink()
            self.block.part6.unlink()
            self.block.part7.unlink()
            self.block.part8.unlink()
            self.block.part9.unlink()
            self.block.part10.unlink()
        elif (self.block.blockType == "bomb"):
            self.block.part1.unlink()
        else:        
            self.block.part1.unlink()
            self.block.part2.unlink()
            self.block.part3.unlink()
            self.block.part4.unlink()
        self.block = None
        self.equalModus()  
        
    def gravityPausieren(self):
        self.player.clearInterval(self.timer)
        
    def gravityWiederStarten(self):
        self.timer = self.player.setInterval(self.speed, self.gravity)

    def letItRain(self):

        self.randomNumber = random.randint(0,13)
        if (self.matrix[self.randomNumber][0]):
            self.gameMenue.endeSpiel()
        else:
            
            block = rainDropBlock.rainDropBlock(self.gameMenue, self, (self.randomNumber,0))
            self.gravityPausieren()
            self.timer = self.player.setInterval(20, self.gravity)
            return block