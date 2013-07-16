from libavg import avg
from Field import Field
from TextRectNode import TextRectNode
from WinLooseMenue import WinLooseMenue
from GrafikChanceMenue import GrafikChanceMenue
from OptionMenue import OptionMenue
import random
from AttackerSkills import AttackerSkills
from AttackerSpecials import AttackerSpecials
from DefenderSkills import DefenderSkills

class GameMenue(object):
    
    def __init__(self, parent, player, modus, gui):
        self.gui = gui
        self.modus = modus  # 0 = classic    1 = equal
        self.player = player
        self.rootNode = parent
        self.divNodeGameMenue= avg.DivNode(parent = self.rootNode, size  = self.rootNode.size, active = False)
        self.background = avg.RectNode(parent = self.divNodeGameMenue, pos = (0,0), fillcolor = "0040FF", fillopacity = 1, color = "0040FF", size = self.divNodeGameMenue.size )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.winLooseMenu = WinLooseMenue(self.rootNode)
        self.optionMenu = OptionMenue(self.rootNode)
        self.grafikMenu = GrafikChanceMenue(self.rootNode, self.player)
        self.menueLinkerXwert  = int(self.divNodeGameMenue.size[0]/2- self.divNodeGameMenue.size[0]*0.04)
        self.menueRechterXwert = int(self.divNodeGameMenue.size[0]/2+ self.divNodeGameMenue.size[0]*0.04)
        self.rahmenbreite = int(self.divNodeGameMenue.size[0]*0.025)
        self.yOben  = int(self.divNodeGameMenue.size[1] * 0.05) 
        self.untereBeschraenkung = self.divNodeGameMenue.size[1] * 0.92 - self.rahmenbreite
        self.xendFeld1 = self.menueLinkerXwert -self.rahmenbreite - self.divNodeGameMenue.size[1] * 0.03
        self.xstartFeld1, self.yUnten = self.berechneLinkesXUntenYFeld1(self.xendFeld1, self.untereBeschraenkung,self.yOben)
        sizefield = self.xendFeld1 - self.xstartFeld1
        self.xstartFeld2 = self.menueRechterXwert +self.rahmenbreite + self.divNodeGameMenue.size[1] * 0.03
        self.xendFeld2   = self.xstartFeld2 + sizefield
        self.blocksize = (self.xendFeld1 - self.xstartFeld1 )/14
        self.tetrishoehe = self.blocksize * 19
        self.round = 1
        self.rundenDauer = 180
        self.speed = [750,700,650,600,550]
        self.countOfSkillsActivated = 0
        self.inverseControlActive = False
        self.leftFreezeActive = False
        self.rightFreezeActive = False
        self.rotateFreezeActive = False
        self.speedUpActive = False
        self.makeBlockInvisibleActive = False
        self.noPointsActive = False       
        self.initSounds()
#Gui initialisierung
        self.initFeld(self.xstartFeld1, self.xendFeld1, self.yOben )
        self.initFeld(self.xstartFeld2, self.xendFeld2, self.yOben )

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      

        self.hoeheMitlererBalken =  self.divNodeGameMenue.size[1] * 0.20
        mittlererBalken = self.divNodeGameMenue.size[0]/2
        
        self.timelimit =  avg.WordsNode(pos = (mittlererBalken , self.hoeheMitlererBalken),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="TimeLimit", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
        while(self.timelimit.size[0]>= (self.menueRechterXwert- self.menueLinkerXwert) | (self.timelimit.size[1]>= self.divNodeGameMenue.size[1]* 0.1 )):
            self.timelimit.fontsize-=1
            if(self.timelimit.fontsize<=0):
                self.timelimit.fontsize= 1
                break
        fontS = self.timelimit.fontsize  
        self.hoeheMitlererBalken +=  fontS + fontS*0.5
#-----------------------------------------------------------------------------------------------------------------------------------------------------------                 
        self.timerLimit = avg.WordsNode(pos = (mittlererBalken , self.hoeheMitlererBalken),
                                      fontsize = fontS, 
                                      text =str(self.rundenDauer ), 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
        self.hoeheMitlererBalken +=  4*fontS
        
        self.timeLimitCounter = self.player.setInterval(1000, self.timerLCountDown)
#----------------------------------------------------------------------------------------------------------------------------------------------------------- 
        
        self.roundText = avg.WordsNode(pos = (mittlererBalken, self.hoeheMitlererBalken),
                                      fontsize = fontS, 
                                      text ="Round", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        self.hoeheMitlererBalken +=  fontS + fontS*0.5
#----------------------------------------------------------------------------------------------------------------------------------------------------------- 
        
        self.roundNumber = avg.WordsNode(pos = (mittlererBalken , self.hoeheMitlererBalken),
                                      fontsize = fontS, 
                                      text =str(self.round), 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        self.hoeheMitlererBalken +=  4*fontS
#---------------------------------------------------------------------------------------------------------------------------------------------------------- 
        
        self.speedText = avg.WordsNode(pos = (mittlererBalken , self.hoeheMitlererBalken),
                                      fontsize = fontS, 
                                      text ="Speed", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        self.hoeheMitlererBalken +=  fontS + fontS*0.5
      
        self.speedNumber = avg.WordsNode(pos = (mittlererBalken , self.hoeheMitlererBalken),
                                      fontsize = fontS, 
                                      text ="1", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        self.hoeheMitlererBalken += 4*fontS

         
        self.scoreTeam1 = avg.WordsNode(pos = ((self.xstartFeld1 + self.xendFeld1)/2 , self.divNodeGameMenue.size[1] * 0.94),
                                      fontsize = 0.035*self.divNodeGameMenue.size[1], 
                                      text ="Score :   0", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
          
        self.scoreTeam2 = avg.WordsNode(pos = ((self.xstartFeld2 + self.xendFeld2)/2 , self.divNodeGameMenue.size[1] * 0.94),
                                      fontsize = 0.035*self.divNodeGameMenue.size[1], 
                                      text ="Score :   0",  
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        #Optionevents
        self.background.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.background, self.startOptionMenu)
        self.optionMenu.buttonResume.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.optionMenu.buttonResume, self.stopOptionMenue)
        self.optionMenu.buttonGrafik.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.optionMenu.buttonGrafik, self.clickOnOptionGrafikButtom)
        self.optionMenu.buttonFinish.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.optionMenu.buttonFinish, self.finishEarly)
        self.optionMenu.buttonSound.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.optionMenu.buttonSound, self.turnSoundOff)
        #grafikchancebottoms
        self.grafikMenu.buttonBreiteM.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.grafikMenu.buttonBreiteM, self.clickBreiteM)
        self.grafikMenu.buttonBreiteMM.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.grafikMenu.buttonBreiteMM, self.clickBreiteMM)
        self.grafikMenu.buttonBreitePP.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.grafikMenu.buttonBreitePP, self.clickBreitePP)
        self.grafikMenu.buttonBreiteP.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.grafikMenu.buttonBreiteP, self.clickBreiteP)
        
        self.grafikMenu.buttonLaengeM.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.grafikMenu.buttonLaengeM, self.clickLaengeM)
        self.grafikMenu.buttonLaengeMM.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.grafikMenu.buttonLaengeMM, self.clickLaengeMM)
        self.grafikMenu.buttonLaengeP.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.grafikMenu.buttonLaengeP, self.clickLaengeP)
        self.grafikMenu.buttonLaengePP.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.grafikMenu.buttonLaengePP, self.clickLaengePP)
        
        self.grafikMenu.buttonBack.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.grafikMenu.buttonBack, self.clickOnBackButtomGrafikChanceMenue)
#fuer Matrix feld initialisierung 
        self.yUnten =  self.yOben + self.tetrishoehe
        self.field1 = Field(self.xstartFeld1, self.xendFeld1, self.yOben, self.yUnten,self.blocksize,self.player,self,1, self.gui)
        self.field2 = Field(self.xstartFeld2, self.xendFeld2, self.yOben, self.yUnten,self.blocksize,self.player,self,2, self.gui)
        self.attackerNormalField1 = AttackerSkills(self.field1,self.player)
        self.attackerNormalField2 = AttackerSkills(self.field2,self.player)
        self.attackerSpezialonField1 = AttackerSpecials(self.field2, self.field1,self.player)
        self.attackerSpezialonField2 = AttackerSpecials(self.field1, self.field2,self.player)
        self.defenderSkillsField1 = DefenderSkills(self.field1, self.player)
        self.defenderSkillsField2 = DefenderSkills(self.field2, self.player)
        self.playSound("gameStart")
        self.SkillActivator = self.player.setInterval(120000, self.activateOneSkill)
        
        
        #print "Tetrisfeldbegrenzungen:   lF1:",self.xstartFeld1,"  rF1: ",self.xendFeld1,"   lF1F2: ",self.xstartFeld2,"  rF2:  ",self.xendFeld2,"  yO: ", self.yOben," yU: ", self.yUnten
        #print "Ein Feld:  Blocksize:  ", self.blocksize, "    Hoehe:   ", self.tetrishoehe, "    Breite:  ", self.xendFeld1-self.xstartFeld1
#buttoms werden initialisiert
        
#-------------------------------------------------------------Tests UPDOWNROTATE---loeschbar spaeter----------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.buttonMoveL = TextRectNode(parent = self.divNodeGameMenue, 
                                       pos = (self.divNodeGameMenue.size[0]*0.05,self.divNodeGameMenue.size[1] * 0.9),
                                       fillcolor ="000000",
                                       fillopacity=1,
                                       color = "000000",
                                       size = avg.Point2D(self.divNodeGameMenue.size[0]*0.1,self.divNodeGameMenue.size[1]*0.1))
        self.buttonMoveL.addTextGameTypeAndMain("L","FFFFFF")
        
        self.buttonRotateL = TextRectNode(parent = self.divNodeGameMenue, 
                                   pos = (self.divNodeGameMenue.size[0]*0.3,self.divNodeGameMenue.size[1] * 0.9),
                                   fillcolor ="000000",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodeGameMenue.size[0]*0.1,self.divNodeGameMenue.size[1]*0.1))
        self.buttonRotateL.addTextGameTypeAndMain("RL","FFFFFF")
        
        self.buttonRotateR = TextRectNode(parent = self.divNodeGameMenue, 
                                   pos = (self.divNodeGameMenue.size[0]*0.6,self.divNodeGameMenue.size[1] * 0.9),
                                   fillcolor ="000000",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodeGameMenue.size[0]*0.1,self.divNodeGameMenue.size[1]*0.1))
        self.buttonRotateR.addTextGameTypeAndMain("RR","FFFFFF")
        
        self.buttonMoveR = TextRectNode(parent = self.divNodeGameMenue, 
                                   pos = (self.divNodeGameMenue.size[0]*0.9,self.divNodeGameMenue.size[1] * 0.9),
                                   fillcolor ="000000",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodeGameMenue.size[0]*0.1,self.divNodeGameMenue.size[1]*0.1))
        self.buttonMoveR.addTextGameTypeAndMain("R","FFFFFF")
        
        self.buttonSpeed = TextRectNode(parent = self.divNodeGameMenue, 
                                   pos = (self.divNodeGameMenue.size[0]*0.45,self.divNodeGameMenue.size[1] * 0.9),
                                   fillcolor ="000000",
                                   fillopacity=1,
                                   color = "000000",
                                   size = avg.Point2D(self.divNodeGameMenue.size[0]*0.1,self.divNodeGameMenue.size[1]*0.1))
        self.buttonSpeed.addTextGameTypeAndMain("SD","FFFFFF")
        
        self.buttonMoveL.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.buttonMoveL, self.eventMoveLinks) 
        self.buttonRotateL.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.buttonRotateL, self.eventRotateLinks) 
        self.buttonRotateR.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.buttonRotateR, self.eventRotateRechts) 
        self.buttonMoveR.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.buttonMoveR, self.eventMoveRechts)
        self.buttonSpeed.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.buttonSpeed, self.eventSpeedDown )

    def eventMoveLinks(self,event):
        self.field1.moveLeft()
    
    def eventRotateLinks(self,event):
        self.field1.rotateLeft()

    def eventRotateRechts(self,event):
        self.field1.rotateRight()

    def eventMoveRechts(self,event):
        self.field1.moveRight()
        
    def eventSpeedDown(self,event):
        self.field1.speedDown()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        
    def berechneLinkesXUntenYFeld1(self,rechteKante, untereSchranke, obereSchranke):
        linkesX = int(self.divNodeGameMenue.size[0] * 0.03) 
        size = rechteKante - linkesX
        size = self.naechsteZahlDurch14Teilbar(size)
        while(True):
            blocksize = size / 14
            tetrishoehe = blocksize *19
            if((untereSchranke - obereSchranke) >= tetrishoehe):
                return ((rechteKante- size), obereSchranke-tetrishoehe)
            else:
                size-=14
                
        
#----------------------------------------------Rundenuebergang---------------------------------------------------------------------------------------------------    
        
    def timerLCountDown (self):
        count = int (self.timerLimit.text)
        if(self.modus == 1):#EqualModus, dh reihen loeschen bei der mitte und fallender stein wird geloescht
            if(count >=0):
                if(count <= 0):
                    self.timerLimit.text = str(-3)
                    self.rundenWechsel()
                    if(self.round > 5):
                        self.player.clearInterval(self.timeLimitCounter)
                        self.endeSpiel()
                else:
                    count -= 1
                    self.timerLimit.text = str(count)
            else:
                count+=1
                self.timerLimit.text = str(count)
                if(count >= 0):
                    self.fieldChanceRundenWechsel()
                    self.timerLimit.text = str(self.rundenDauer)
        else:
            if(count <= 0):#ClassicModus
                self.timerLimit.text = str(self.rundenDauer)
        
                self.field1.chanceSpeed(self.speed[self.round-1])
                self.field2.chanceSpeed(self.speed[self.round-1])
                self.round += 1
                if(self.round > 5):
                    self.field1.clearForNextRound()
                    self.player.clearInterval(self.timeLimitCounter)
                    
                    self.endeSpiel()
                else:
                    self.roundNumber.text = str(self.round)
                    self.speedNumber.text = str(self.round)
            else:
                count -= 1
                self.timerLimit.text = str(count)
         
    def rundenWechsel(self):
        self.field1.clearForNextRound()
        self.field2.clearForNextRound()
        self.resetField(self.field1)
        self.resetField(self.field2)
        self.round += 1
        self.roundNumber.text = str(self.round)
        self.speedNumber.text = str(self.round)
        self.playSound("round")

        
    def fieldChanceRundenWechsel(self):
        
        self.field1.speed = self.speed[(self.round -1)]
        self.field1.timer = self.field1.player.setInterval(self.field1.speed, self.field1.gravity)
        self.field2.speed = self.speed[(self.round -1)]
        self.field2.timer = self.field2.player.setInterval(self.field2.speed, self.field2.gravity)
        self.field1.initBlock()
        self.field2.initBlock()

        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
    def endeSpiel(self, winner = "check"):
        if(winner == "check"):
            scoreTeam1 = self.field1.score
            scoreTeam2 = self.field2.score
            if(scoreTeam1 == scoreTeam2):
                winner = "Unentschieden"
            elif(scoreTeam1 > scoreTeam2):
                winner = "Team 1 gewinnt"
            elif(scoreTeam1 < scoreTeam2):
                winner = "Team 2 gewinnt"
        self.player.clearInterval(self.SkillActivator)
        self.field1.gravityPausieren()
        self.field2.gravityPausieren()
        self.player.clearInterval(self.timeLimitCounter)
        self.divNodeGameMenue.active = False
        self.optionMenu.divNodeOptionMenue.active = False
        self.winLooseMenu.buttonNextGame.sensitive = True
        self.winLooseMenu.buttonSomeOneWon.updateTextNode(winner)
        self.winLooseMenu.divNodeWinLooseMenue.active = True

        self.playSound("victory")
    
    def naechsteZahlDurch14Teilbar(self,value):
        x = value % 14
        return value - x
    
    def initFeld (self, startX, endX, oben):
#linker Rahmen
        avg.RectNode(parent = self.divNodeGameMenue, sensitive = False,
                                  pos = (startX -self.rahmenbreite  , oben), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.rahmenbreite ,self.tetrishoehe) #self.divNodeGameMenue.size[1]* 0.87
                                  )
#rechter Rahmen
        avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (endX , oben), sensitive = False,
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(self.rahmenbreite, self.tetrishoehe)
                                  )
#Boden
        avg.RectNode(parent = self.divNodeGameMenue, sensitive = False,
                                  pos = (startX-self.rahmenbreite, self.tetrishoehe+oben), 
                                  fillcolor = "000000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(endX-startX+2*int(self.divNodeGameMenue.size[0]*0.025) ,self.rahmenbreite)
                                  )
                                  
                                  
    def startOptionMenu(self, event):
        self.divNodeGameMenue.active = False
        self.optionMenu.divNodeOptionMenue.active = True
        self.field1.gravityPausieren()
        self.player.clearInterval(self.timeLimitCounter)
        
    def stopOptionMenue(self, event):
        self.divNodeGameMenue.active = True
        self.optionMenu.divNodeOptionMenue.active = False
        self.field1.gravityWiederStarten()
        self.timeLimitCounter = self.player.setInterval(1000, self.timerLCountDown)
        
        
    def finishEarly(self, event):
        self.field1.score = 0
        self.field2.score = 0
        self.endeSpiel()
        
    def turnSoundOff(self, event):
        text = self.optionMenu.buttonSound.getTextNode().text
        if(text == "Sound:  An"):
            self.deactivateSound()
            self.optionMenu.buttonSound.updateTextNode("Sound:  Aus")
        else:
            self.activateSound()
            self.optionMenu.buttonSound.updateTextNode("Sound:  An")
    
    
    def clickOnOptionGrafikButtom(self,event):
        self.optionMenu.divNodeOptionMenue.active = False
        self.grafikMenu.divNodeGrafikMenue.active = True
        
    def clickOnBackButtomGrafikChanceMenue(self, event):
        self.grafikMenu.divNodeGrafikMenue.active = False
        self.optionMenu.divNodeOptionMenue.active = True
            
    def clickBreiteP(self,event):
        #TODO: Breite  +
        pass
    
    def clickBreitePP(self,event):
        #TODO: Breite + +
        pass
    
    def clickBreiteM(self,event):
        #TODO: Breite -
        pass
    
    def clickBreiteMM(self,event):
        #TODO: Breite --
        pass
    
    def clickLaengeP(self,event):
        #TODO: Laenge +
        pass
    
    def clickLaengePP(self,event):
        #TODO: Laenge + +
        pass
    
    def clickLaengeM(self,event):
        #TODO: Laenge -
        pass
    
    def clickLaengeMM(self,event):
        #TODO: Laenge --
        pass
        
    def activateOneSkill(self): #schaltet nach 2 minuten einen cooldown fuer den Angreifer frei

        randomNumber = random.randint(1,7)
        freigeschalteterBlock = ""
        if (randomNumber == 1):
            if (self.rightFreezeActive == True):
                self.activateOneSkill()
            else:
                self.rightFreezeActive = True
                self.countOfSkillsActivated += 1
                self.playSound("skillUnlocked")
                freigeschalteterBlock = "unlockRightFreeze"

        elif (randomNumber == 2):
            if (self.leftFreezeActive == True):
                self.activateOneSkill()
            else:
                self.leftFreezeActive = True
                self.countOfSkillsActivated += 1
                self.playSound("skillUnlocked")
                freigeschalteterBlock = "unlockLeftFreeze"

        elif (randomNumber == 3):
            if (self.rotateFreezeActive == True):
                self.activateOneSkill()
            else:
                self.rotateFreezeActive = True
                self.countOfSkillsActivated += 1
                self.playSound("skillUnlocked")
                freigeschalteterBlock = "unlockRotateFreeze"
        elif (randomNumber == 4):
            if (self.noPointsActive == True):
                self.activateOneSkill()
            else:
                self.noPointsActive = True
                self.countOfSkillsActivated += 1
                self.playSound("skillUnlocked")
                freigeschalteterBlock = "unlockNoPoints"

        elif (randomNumber == 5):
            if (self.inverseControlActive == True):
                self.activateOneSkill()
            else:
                self.inverseControlActive = True
                self.countOfSkillsActivated += 1
                self.playSound("skillUnlocked")
                freigeschalteterBlock = "unlockInverseControl"
        elif (randomNumber == 6):
            if (self.makeBlockInvisibleActive == True):
                self.activateOneSkill()
            else:
                self.makeBlockInvisibleActive = True
                self.countOfSkillsActivated += 1
                self.playSound("skillUnlocked")
                freigeschalteterBlock = "unlockBlockInvisible"
        else:
            if (self.speedUpActive == True):
                self.activateOneSkill()
            else:
                self.speedUpActive = True
                self.countOfSkillsActivated += 1
                self.playSound("skillUnlocked")
                freigeschalteterBlock = "unlockSpeedUp"
        if (self.countOfSkillsActivated == 7):
            self.player.clearInterval(self.SkillActivator)
        #sende
        if(freigeschalteterBlock != ""):
            if(self.gui.lobbyMenu.modus == 3):
                ip = self.gui.lobbyMenu.playerID[2]
                self.gui.sendMsgToAll(ip+ "###"+freigeschalteterBlock)
            elif(self.gui.lobbyMenu.modus == 4):
                ip1 = self.gui.lobbyMenu.playerID[2]
                ip2 = self.gui.lobbyMenu.playerID[3]
                self.gui.sendMsgToAll(ip1+"###"+freigeschalteterBlock)
                self.gui.sendMsgToAll(ip2+"###"+freigeschalteterBlock)
        
    def resetField(self, Field):
        
        Field.inverseSteuerung = False
        Field.freezeLeft = False
        Field.freezeRight = False
        Field.freezeRotate = False
        Field.speedToGround = False
        Field.superBlock = False
        Field.bombActivated = False
        Field.thunderActivated = False
        Field.tetrisRainActivated = False
        Field.noMoneyForYou = False
        Field.rainDropCount = 0
        
    def initSounds(self):
        self.deniedSound = avg.SoundNode(href="denied.mp3", loop=False, volume=1.0, parent = self.rootNode)
        self.skillUnlockedSound = avg.SoundNode(href="skillUnlocked.mp3", loop=False, volume=1.0, parent = self.rootNode)
        self.gameStartSound = avg.SoundNode(href="gameStart.mp3", loop=False, volume=1.0, parent = self.rootNode)
        self.rotateSound = avg.SoundNode(href="rotate.wav", loop=False, volume=1.0, parent = self.rootNode)
        self.victorySound = avg.SoundNode(href="victory.mp3", loop=False, volume=1.0, parent = self.rootNode)
        self.thunderSound = avg.SoundNode(href="thunder.wav", loop=False, volume=1.0, parent = self.rootNode)
        self.roundSound = avg.SoundNode(href="round.mp3", loop=False, volume=1.0, parent = self.rootNode)
        self.rainSound = avg.SoundNode(href="rain.mp3", loop=False, volume=1.0, parent = self.rootNode)
        self.bombSound = avg.SoundNode(href="bomb.wav", loop=False, volume=1.0, parent = self.rootNode)
        self.cashSound = avg.SoundNode(href="cash.mp3", loop=False, volume=1.0, parent = self.rootNode)
        
    def playSound(self, String):
        if (String == "rain"):
            self.rainSound.play()
        elif (String == "bomb"):
            self.bombSound.play()
        elif (String == "cash"):
            self.cashSound.play()
        elif (String == "round"):
            self.roundSound.play()
        elif (String == "thunder"):
            self.thunderSound.play()
        elif (String == "victory"):
            self.victorySound.play()
        elif (String == "rotate"):
            self.rotateSound.play()
        elif (String == "denied"):
            self.deniedSound.play()
        elif (String == "gameStart"):
            self.gameStartSound.play()
        elif (String == "skillUnlocked"):
            self.skillUnlockedSound.play()
        else:
            pass
        
    def deactivateSound(self): #deactivates all sound nodes
        self.bombSound.volume = 0.0
        self.cashSound.volume = 0.0
        self.deniedSound.volume = 0.0
        self.gameStartSound.volume = 0.0
        self.rainSound.volume = 0.0
        self.rotateSound.volume = 0.0
        self.roundSound.volume = 0.0
        self.skillUnlockedSound.volume = 0.0
        self.thunderSound.volume = 0.0
        
    def activateSound(self): #activates all sound nodes
        self.bombSound.volume = 1.0
        self.cashSound.volume = 1.0
        self.deniedSound.volume = 1.0
        self.gameStartSound.volume = 1.0
        self.rainSound.volume = 1.0
        self.rotateSound.volume = 1.0
        self.roundSound.volume = 1.0
        self.skillUnlockedSound.volume = 1.0
        self.thunderSound.volume = 1.0
