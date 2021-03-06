import rainDropBlock, superBlock, BombBlock, crossFallingBlock,cubeFallingBlock,IFallingBlock, LFallingBlock, reverseLFallingBlock, reverseZFallingBlock, ZFallingBlock
import random
from collections import deque

class Field(object):

    def __init__(self, xWertLinksOben, xWertRechtsOben, yWertOben, yWertUnten, blocksize, player,gameMenue, idd, gui):
        self.gui = gui
        self.id = idd
        self.score = 0
        self.gameMenue = gameMenue
        if(xWertLinksOben <= (self.gameMenue.divNodeGameMenue.size[0]/2)):
            self.feldScore = self.gameMenue.scoreTeam1
        else:
            self.feldScore = self.gameMenue.scoreTeam2
        self.countBlocks = 0
        
        self.inverseSteuerung = False
        self.freezeLeft = False
        self.freezeRight = False
        self.freezeRotate = False
        self.speedToGround = False
        self.superBlock = False
        self.bombActivated = False
        self.thunderActivated = False
        self.tetrisRainActivated = False
        self.noMoneyForYou = False
        
        self.rainDropCount = 0
        self.player = player
        self.speed = self.gameMenue.speed[0]
        self.xWertLinksOben = xWertLinksOben
        self.xWertRechtsOben = xWertRechtsOben
        self.yWertOben = yWertOben
        self.yWertUnten = yWertUnten
        #queue die gefuellt wird durch phone, new falling stone danach mit dem naechsten rufen
        self.specialsQueue = deque()
        self.Queue = deque()
        # Matrix hat die Form Matrix[0-13][0-18] und ist mit False initialisiert
        self.matrix = [[False for i in range(19)] for j in range(14)] #@UnusedVariable
        self.matrixSteadyRectNodes = [[None for i in range(19)] for j in range(14)]#@UnusedVariable
        self.initBlock();
        self.timer = self.player.setInterval(self.speed, self.gravity)
    
    #erzeugt einen neuen fallenden block         
    def initBlock(self):

        if (self.tetrisRainActivated):
            self.letItRainScript()
        elif (self.thunderActivated or self.superBlock or self.bombActivated):
            self.block = self.newFallingStone()
        else: 
            if (not self.specialsQueue):
                self.block = self.newFallingStone()
            else:
                string = self.specialsQueue.popleft()
                self.processSpecialsQueue(string)
                self.block = self.newFallingStone()
  
    # wenn block boden beruehrt werden reihen ueberprueft und neuer block erzeugt
    def blockHitGround(self, spezialblock = ""):
        self.checkRows()
        if(spezialblock == ""):
            if(self.gui.lobbyMenu.modus == 3):
                self.countBlocks+= 1
                #print self.gameMenue.field1.countBlocks,self.gameMenue.field2.countBlocks, self.id
                if(self.id == 1):
                    if(self.gameMenue.field2.countBlocks <= self.countBlocks):
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[2], "dropBlock")
                else:
                    if(self.gameMenue.field1.countBlocks < self.countBlocks):
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[2], "dropBlock")
            elif(self.gui.lobbyMenu.modus == 4):
                if(id == 1):
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[3], "dropBlock")
                else:
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[2], "dropBlock")
        self.initBlock()
        self.timer = self.player.setInterval(self.speed, self.gravity)
        
    # fuegt fallenden block der matrix hinzu
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
        
        
    # ueberprueft die reihen nach eventuell vollen              
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
                self.gameMenue.playSound("denied")
            else:
                if  (amountOfRows == 1):
                    self.updateScore(1)#<-----1 fuer 1
                elif(amountOfRows == 2):
                    self.updateScore(3)#<-----3 fuer 2
                elif(amountOfRows == 3):
                    self.updateScore(5)#<-----5 fuer 3
                elif(amountOfRows == 4):
                    self.updateScore(7)#<-----7 fuer 4
    
    #vergibt punkte , erhoeht score    
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
    
    # loescht row aus der matrix und versetzt alle anderen nodes nach unten
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
        self.gameMenue.playSound("cash")
    
    #generiert einen zufaelligen block               
    def generateRandomBlock(self):
        RandomNumber = random.randint(1,7)

        if (RandomNumber == 1):
            a = self.checkSpawn("cube")
            if a:
                if(self.id == 1):
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[0],"cube")
                else:
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[1],"cube")
                    
                return cubeFallingBlock.cubeFallingBlock(self.gameMenue, self)
            else:
                if(self.id == 1):
                    self.gameMenue.endeSpiel("Team 2 gewinnt")
                else:
                    self.gameMenue.endeSpiel("Team 1 gewinnt")
            
        elif (RandomNumber == 2):
            a = self.checkSpawn("I")
            if a:
                if(self.id == 1):
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[0],"I")
                else:
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[1],"I")
                    
                return IFallingBlock.IFallingBlock(self.gameMenue, self)
            else:
                if(self.id == 1):
                    self.gameMenue.endeSpiel("Team 2 gewinnt")
                else:
                    self.gameMenue.endeSpiel("Team 1 gewinnt")
          
        elif (RandomNumber == 3):
            a = self.checkSpawn("L")
            if a:
                if(self.id == 1):
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[0],"L")
                else:
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[1],"L")
                return LFallingBlock.LFallingBlock(self.gameMenue, self)
            else:
                if(self.id == 1):
                    self.gameMenue.endeSpiel("Team 2 gewinnt")
                else:
                    self.gameMenue.endeSpiel("Team 1 gewinnt")
            
        elif (RandomNumber == 4):
            a = self.checkSpawn("reverseL")
            if a:
                if(self.id == 1):
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[0],"reverseL")
                else:
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[1],"reverseL")
                    
                return reverseLFallingBlock.reverseLFallingBlock(self.gameMenue, self)
            else:
                if(self.id == 1):
                    self.gameMenue.endeSpiel("Team 2 gewinnt")
                else:
                    self.gameMenue.endeSpiel("Team 1 gewinnt")
            
        elif (RandomNumber == 5):
            a = self.checkSpawn("reverseZ")
            if a:
                if(self.id == 1):
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[0],"reverseZ")
                else:
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[1],"reverseZ")
                 
                return reverseZFallingBlock.reverseZFallingBlock(self.gameMenue, self)
            else:
                if(self.id == 1):
                    self.gameMenue.endeSpiel("Team 2 gewinnt")
                else:
                    self.gameMenue.endeSpiel("Team 1 gewinnt") 
            
        elif (RandomNumber == 6):
            a = self.checkSpawn("Z")
            if a:
                if(self.id == 1):
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[0],"Z")
                else:
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[1],"Z")
                 
                return ZFallingBlock.ZFallingBlock(self.gameMenue, self)
            else:
                if(self.id == 1):
                    self.gameMenue.endeSpiel("Team 2 gewinnt")
                else:
                    self.gameMenue.endeSpiel("Team 1 gewinnt")
        elif(RandomNumber == 7):
            a = self.checkSpawn("cross")
            if a: 
                if(self.id == 1):
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[0],"cross")
                else:
                    self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[1],"cross")
                 
                return crossFallingBlock.crossFallingBlock(self.gameMenue, self)
            else:
                if(self.id == 1):
                    self.gameMenue.endeSpiel("Team 2 gewinnt")
                else:
                    self.gameMenue.endeSpiel("Team 1 gewinnt")
                     
        elif (RandomNumber == 8):
            self.specialsQueue.append("bomb")
            return crossFallingBlock.crossFallingBlock(self.gameMenue, self)
        
        elif (RandomNumber == 9):
            self.specialsQueue.append("rain")
            return ZFallingBlock.ZFallingBlock(self.gameMenue, self)
        
        elif (RandomNumber == 10):
            #self.specialsQueue.append("thunder")
            return reverseZFallingBlock.reverseZFallingBlock(self.gameMenue, self)
        
        else:
            #self.specialsQueue.append("super")
            return reverseLFallingBlock.reverseLFallingBlock(self.gameMenue, self)
    
    # erzeugt neuen fallingblock fuer init
    def newFallingStone(self):
        
        if(self.thunderActivated):
            self.gameMenue.playSound("thunder")
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
                if(self.id):
                    self.gameMenue.endeSpiel("Team 2 gewinnt")
                else:
                    self.gameMenue.endeSpiel("Team 1 gewinnt")

        ##if queue leer dann random sonst erstes element der queue
        elif not self.Queue:
            return self.generateRandomBlock()
        else:
            a = self.Queue.popleft()
            b = self.checkSpawn(a)
            if b:
                if (a == "cube"):
                    if(self.id == 1):
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[0],"cube")
                    else:
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[1],"cube")
                 
                    return cubeFallingBlock.cubeFallingBlock(self.gameMenue, self)
                elif (a == "I"):
                    if(self.id == 1):
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[0],"I")
                    else:
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[1],"I")
                 
                    
                    return IFallingBlock.IFallingBlock(self.gameMenue, self)
                elif (a== "L"):
                    if(self.id == 1):
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[0],"L")
                    else:
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[1],"L")
                 
                    
                    return LFallingBlock.LFallingBlock(self.gameMenue, self)
                elif (a == "Z"):
                    if(self.id == 1):
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[0],"Z")
                    else:
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[1],"Z")
                 
                    
                    return ZFallingBlock.ZFallingBlock(self.gameMenue, self)
                elif (a == "reverseL"):
                    if(self.id == 1):
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[0],"reverseL")
                    else:
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[1],"reverseL")
                 
                    
                    return reverseLFallingBlock.reverseLFallingBlock(self.gameMenue, self)
                elif (a == "reverseZ"):
                    if(self.id == 1):
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[0],"reverseZ")
                    else:
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[1],"reverseZ")
                 
                    
                    return reverseZFallingBlock.reverseZFallingBlock(self.gameMenue, self)
                elif (a == "cross"):
                    if(self.id == 1):
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[0],"cross")
                    else:
                        self.gui.sendMsgToOne(self.gui.lobbyMenu.playerIP[1],"cross")
                 
                    
                    return crossFallingBlock.crossFallingBlock(self.gameMenue,self)
                else:
                    pass
            else: 
                if(self.id == 1):
                    self.gameMenue.endeSpiel("Team 2 gewinnt")
                else:
                    self.gameMenue.endeSpiel("Team 1 gewinnt")
        
    # returns False if spawn is not possible, true otherwise
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

    # ist fuer das fallen der bloecke zustaendig
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
                self.blockHitGround("super")               
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
            

    # gibt bewegung an fallenden block weiter    
    def moveLeft(self):
        if((self.block == None) | self.freezeLeft):
            self.gameMenue.playSound("denied")
        elif(self.inverseSteuerung):
            self.block.moveBlockRight()
        else:
            self.block.moveBlockLeft()
    
    # gibt bewegung an fallenden block weiter 
    def moveRight(self):
        if((self.block == None)| self.freezeRight):
            self.gameMenue.playSound("denied")
        elif(self.inverseSteuerung):
            self.block.moveBlockLeft()
        else:
            self.block.moveBlockRight()
    
    # gibt bewegung an fallenden block weiter 
    def rotateLeft(self):
        if((self.block == None)| self.freezeRotate):
            self.gameMenue.playSound("denied")
        elif(self.inverseSteuerung):
            self.gameMenue.playSound("rotate")
            self.block.rotateRight()
        else:
            self.gameMenue.playSound("rotate")
            self.block.rotateLeft()
            
    # gibt bewegung an fallenden block weiter 
    def rotateRight(self):
        if((self.block == None)| self.freezeRotate):
            self.gameMenue.playSound("denied")
        elif(self.inverseSteuerung):
            self.gameMenue.playSound("rotate")
            self.block.rotateLeft()
        else:
            self.gameMenue.playSound("rotate")
            self.block.rotateRight()
    
    #erhoeht die geschwindigkeit        
    def speedDown(self):
        self.chanceSpeed(50)
        
    # setzt geschwindigkeit der gravity auf neuen wert        
    def chanceSpeed(self, newSpeedInMs):
        self.player.clearInterval(self.timer)
        self.timer = self.player.setInterval(newSpeedInMs, self.gravity)
    
    # loescht im equalmodus die obersten 9 reihen
    def equalModus(self):
        for reihe in range(0,10):
            for spalte in range (14):
                if(self.matrix[spalte][reihe]):
                    self.matrix[spalte][reihe] = False
                    (self.matrixSteadyRectNodes[spalte][reihe]).unlink()
                    self.matrixSteadyRectNodes[spalte][reihe] = None
    
    # runden wechsel, alle intervalle werden umgesetzt
    def clearForNextRound(self):
        self.player.clearInterval(self.timer)
        if (self.block == None):
            pass
        elif(self.block.blockType == "super"):
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
        elif (self.block.blockType == "bomb") or (self.block.blockType == "rain"):
            self.block.part1.unlink()
        else:        
            self.block.part1.unlink()
            self.block.part2.unlink()
            self.block.part3.unlink()
            self.block.part4.unlink()
        self.block = None
        self.equalModus()  
    
    #pausiert gravity    
    def gravityPausieren(self):
        self.player.clearInterval(self.timer)
     
    #starten gravity    
    def gravityWiederStarten(self):
        self.timer = self.player.setInterval(self.speed, self.gravity)

    #returns a rainDrop at a random location at the top or ends the game
    def letItRain(self, RandomNumber): 

        if (self.matrix[RandomNumber][0]):
            if(self.id == 1):
                self.gameMenue.endeSpiel("Team 2 gewinnt")
            else:
                self.gameMenue.endeSpiel("Team 1 gewinnt")
        else:
            
            return rainDropBlock.rainDropBlock(self.gameMenue, self, (self.randomNumber,0))
    
    #Wirft 30 Rainblocks in das tetrisfeld
    def letItRainScript(self):
        
        b = True
        for i in range (14):
            b = b and self.matrix[i][0]
        if b:
            if(self.id == 1):
                self.gameMenue.endeSpiel("Team 2 gewinnt")
            else:
                self.gameMenue.endeSpiel("Team 1 gewinnt")
        
        elif (self.tetrisRainActivated and self.rainDropCount == 0):
            self.randomNumber = random.randint(0,13)
            if (self.matrix[self.randomNumber][0]):
                self.letItRainScript()
            else:
                self.block = self.letItRain(self.randomNumber)
                self.gameMenue.playSound("rain")
                self.rainDropCount += 1
                self.timer1 = self.player.setInterval(20, self.gravity)
        
        elif (self.tetrisRainActivated):
            
            self.randomNumber = random.randint(0,13)
            if (self.matrix[self.randomNumber][0]):
                self.letItRainScript()
            else:
                self.rainDropCount += 1
                if (self.rainDropCount > 29):
                    
                    self.tetrisRainActivated = False
                    self.rainDropCount = 0
                    self.player.clearInterval(self.timer1)
                    self.block = self.newFallingStone()
                else:
                    self.block = self.letItRain(self.randomNumber)
        else:
            pass

    #arbeitet die spezialfaehigkeitenqueue ab
    def processSpecialsQueue(self, QueueString):
        if (QueueString == "rain"):
            self.tetrisRainActivated = True
        elif (QueueString == "bomb"):
            self.bombActivated = True
        elif (QueueString == "super"):
            self.superBlock = True
        elif (QueueString == "thunder"):
            self.thunderActivated = True
        else:
            pass
        