from libavg import avg
from Field import Field
from WinLooseMenue import WinLooseMenue
from OptionMenue import OptionMenue
import random
from AttackerSkills import AttackerSkills
from AttackerSpecials import AttackerSpecials
from DefenderSkills import DefenderSkills

class GameMenue(object):
    
    def __init__(self, parent, player, modus, gui):
        self.alreadyFinished = False
        self.gui = gui
        self.modus = modus  # 0 = classic    1 = equal
        self.player = player
        self.rootNode = parent
        self.divNodeGameMenue= avg.DivNode(parent = self.rootNode, size  = self.rootNode.size, active = False)
        self.background = avg.ImageNode(parent = self.divNodeGameMenue, href = "DatBG.png", size = self.divNodeGameMenue.size)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.winLooseMenu = WinLooseMenue(self.rootNode)
        self.optionMenu = OptionMenue(self.rootNode)
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
        self.speed = [700,650,600,550,500]
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
                                      color = "F0F0F0", font = "arial", 
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
                                      color = "F0F0F0", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        
        self.hoeheMitlererBalken +=  4*fontS
        
        self.timeLimitCounter = self.player.setInterval(1000, self.timerLCountDown)
#----------------------------------------------------------------------------------------------------------------------------------------------------------- 
        
        self.roundText = avg.WordsNode(pos = (mittlererBalken, self.hoeheMitlererBalken),
                                      fontsize = fontS, 
                                      text ="Round", 
                                      parent = self.divNodeGameMenue, 
                                      color = "F0F0F0", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        self.hoeheMitlererBalken +=  fontS + fontS*0.5
#----------------------------------------------------------------------------------------------------------------------------------------------------------- 
        
        self.roundNumber = avg.WordsNode(pos = (mittlererBalken , self.hoeheMitlererBalken),
                                      fontsize = fontS, 
                                      text =str(self.round), 
                                      parent = self.divNodeGameMenue, 
                                      color = "F0F0F0", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        self.hoeheMitlererBalken +=  4*fontS
#---------------------------------------------------------------------------------------------------------------------------------------------------------- 
        
        self.speedText = avg.WordsNode(pos = (mittlererBalken , self.hoeheMitlererBalken),
                                      fontsize = fontS, 
                                      text ="Speed", 
                                      parent = self.divNodeGameMenue, 
                                      color = "F0F0F0", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        self.hoeheMitlererBalken +=  fontS + fontS*0.5
      
        self.speedNumber = avg.WordsNode(pos = (mittlererBalken , self.hoeheMitlererBalken),
                                      fontsize = fontS, 
                                      text ="1", 
                                      parent = self.divNodeGameMenue, 
                                      color = "F0F0F0", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        self.hoeheMitlererBalken += 4*fontS

         
        self.scoreTeam1 = avg.WordsNode(pos = ((self.xstartFeld1 + self.xendFeld1)/2 , self.divNodeGameMenue.size[1] * 0.94),
                                      fontsize = 0.035*self.divNodeGameMenue.size[1], 
                                      text ="Score :   0", 
                                      parent = self.divNodeGameMenue, 
                                      color = "F0F0F0", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
          
        self.scoreTeam2 = avg.WordsNode(pos = ((self.xstartFeld2 + self.xendFeld2)/2 , self.divNodeGameMenue.size[1] * 0.94),
                                      fontsize = 0.035*self.divNodeGameMenue.size[1], 
                                      text ="Score :   0",  
                                      parent = self.divNodeGameMenue, 
                                      color = "F0F0F0", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        #Optionevents
        self.background.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.background, self.startOptionMenu)
        self.optionMenu.buttonResume.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.optionMenu.buttonResume, self.stopOptionMenue)
        self.optionMenu.buttonFinish.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.optionMenu.buttonFinish, self.finishEarly)
        self.optionMenu.buttonSound.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.optionMenu.buttonSound, self.turnSoundOff)

        self.yUnten =  self.yOben + self.tetrishoehe
        self.field1 = Field(self.xstartFeld1, self.xendFeld1, self.yOben, self.yUnten,self.blocksize,self.player,self,1, self.gui)
        self.field2 = Field(self.xstartFeld2, self.xendFeld2, self.yOben, self.yUnten,self.blocksize,self.player,self,2, self.gui)
        
        self.attackerNormalField1 = AttackerSkills(self.field1,self.player)
        self.attackerNormalField2 = AttackerSkills(self.field2,self.player)
        
        self.attackerSpezialonField1 = AttackerSpecials(self.field2, self.field1,self.player,self.gui)
        self.attackerSpezialonField2 = AttackerSpecials(self.field1, self.field2,self.player,self.gui)
        
        self.defenderSkillsField1 = DefenderSkills(self.field1, self.player)
        self.defenderSkillsField2 = DefenderSkills(self.field2, self.player)
        
        self.playSound("gameStart")
        if(self.gui.lobbyMenu.modus != 2):
            self.SkillActivator = self.player.setInterval(120000, self.activateOneSkill)
        
        
        #print "Tetrisfeldbegrenzungen:   lF1:",self.xstartFeld1,"  rF1: ",self.xendFeld1,"   lF1F2: ",self.xstartFeld2,"  rF2:  ",self.xendFeld2,"  yO: ", self.yOben," yU: ", self.yUnten
        #print "Ein Feld:  Blocksize:  ", self.blocksize, "    Hoehe:   ", self.tetrishoehe, "    Breite:  ", self.xendFeld1-self.xstartFeld1
#buttoms werden initialisiert
        

#fuehrt  Bewegung des Felds auf
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
    #berechneLinkesXUntenYFeld1    
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
    # Time Counter Fuer Game    
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
    # beended spiel, deaktiviert alle intervalle und geht zum gametypemenue zurueck
    def endeSpiel(self, winner = "check"):
        if(not self.alreadyFinished):
            if(winner == "check"):
                scoreTeam1 = self.field1.score
                scoreTeam2 = self.field2.score
                if(scoreTeam1 == scoreTeam2):
                    winner = "Unentschieden"
                elif(scoreTeam1 > scoreTeam2):
                    winner = "Team 1 gewinnt"
                elif(scoreTeam1 < scoreTeam2):
                    winner = "Team 2 gewinnt"
            if(self.gui.lobbyMenu.modus != 2):
                self.player.clearInterval(self.SkillActivator)
            self.alreadyFinished = True
            self.field1.gravityPausieren()
            self.field2.gravityPausieren()
            self.player.clearInterval(self.timeLimitCounter)
            self.divNodeGameMenue.active = False
            self.optionMenu.divNodeOptionMenue.active = False
            self.winLooseMenu.buttonNextGame.sensitive = True
            self.winLooseMenu.buttonSomeOneWon.updateTextNode(winner)
            self.winLooseMenu.divNodeWinLooseMenue.active = True
            self.gui.sendMsgToAll("gameEnds")
            self.playSound("victory")
    
    def naechsteZahlDurch14Teilbar(self,value):
        x = value % 14
        return value - x
    
    #initialisiert das grafische feld
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
                                  
    #event um optionmenu zu aktivieren                              
    def startOptionMenu(self, event):
        self.divNodeGameMenue.active = False
        self.optionMenu.divNodeOptionMenue.active = True
        self.field1.gravityPausieren()
        self.player.clearInterval(self.timeLimitCounter)
    
    #event um optionmenu zu deaktivieren    
    def stopOptionMenue(self, event):
        self.divNodeGameMenue.active = True
        self.optionMenu.divNodeOptionMenue.active = False
        self.field1.gravityWiederStarten()
        self.timeLimitCounter = self.player.setInterval(1000, self.timerLCountDown)
        
    #event im menue zum beenden des spiels    
    def finishEarly(self, event):
        self.field1.score = 0
        self.field2.score = 0
        self.endeSpiel()
    #event im menue zum beenden der sounds   
    def turnSoundOff(self, event):
        text = self.optionMenu.buttonSound.getTextNode().text
        if(text == "Sound:  ON"):
            self.deactivateSound()
            self.optionMenu.buttonSound.updateTextNode("Sound:  OFF")
        else:
            self.activateSound()
            self.optionMenu.buttonSound.updateTextNode("Sound:  ON")

    #schaltet nach 2 minuten einen cooldown fuer den Angreifer frei, nur im 3 und 4 modus aktiviert
    def activateOneSkill(self): 
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
                ip = self.gui.lobbyMenu.playerIP[2]
                print ip+ "###"+freigeschalteterBlock
                self.gui.sendMsgToOne(ip,freigeschalteterBlock)
            elif(self.gui.lobbyMenu.modus == 4):
                ip1 = self.gui.lobbyMenu.playerIP[2]
                ip2 = self.gui.lobbyMenu.playerIP[3]
                self.gui.sendMsgToOne(ip1,freigeschalteterBlock)
                self.gui.sendMsgToOne(ip2,freigeschalteterBlock)
    
    # reseted das feld    
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
    
    #initialisiert die sounds   
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
    
    #ueberprueft welchen sound er abspielen soll    
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
    #deactivates all sound nodes    
    def deactivateSound(self): 
        self.bombSound.volume = 0.0
        self.cashSound.volume = 0.0
        self.deniedSound.volume = 0.0
        self.gameStartSound.volume = 0.0
        self.rainSound.volume = 0.0
        self.rotateSound.volume = 0.0
        self.roundSound.volume = 0.0
        self.skillUnlockedSound.volume = 0.0
        self.thunderSound.volume = 0.0
     
    #activates all sound nodes   
    def activateSound(self): 
        self.bombSound.volume = 1.0
        self.cashSound.volume = 1.0
        self.deniedSound.volume = 1.0
        self.gameStartSound.volume = 1.0
        self.rainSound.volume = 1.0
        self.rotateSound.volume = 1.0
        self.roundSound.volume = 1.0
        self.skillUnlockedSound.volume = 1.0
        self.thunderSound.volume = 1.0
