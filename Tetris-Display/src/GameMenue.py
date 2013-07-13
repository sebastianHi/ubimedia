from libavg import avg
from Field import Field
from TextRectNode import TextRectNode
from WinLooseMenue import WinLooseMenue
from OptionMenue import OptionMenue
import random
from AttackerSkills import AttackerSkills
from AttackerSpecials import AttackerSpecials
from DefenderSkills import DefenderSkills

class GameMenue(object):
    
    def __init__(self, parent, player, modus):
        self.modus = modus  # 0 = classic    1 = equal
        self.player = player
        self.rootNode = parent
        self.divNodeGameMenue= avg.DivNode(parent = self.rootNode, size  = self.rootNode.size, active = False)
        self.background = avg.RectNode(parent = self.divNodeGameMenue, pos = (0,0), fillcolor = "0040FF", fillopacity = 1, color = "0040FF", size = self.divNodeGameMenue.size )
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
        self.speed = [750,650,600,500,400]
        
        self.countOfSkillsActivated = 0
        self.inverseControlActive = False
        self.leftFreezeActive = False
        self.rightFreezeActive = False
        self.rotateFreezeActive = False
        self.speedUpActive = False
        self.makeBlockInvisibleActive = False
        self.noPointsActive = False
        self.skillsOnCooldown = False        
        
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

         
        self.scoreTeam1 = avg.WordsNode(pos = ((self.xstartFeld1 + self.xendFeld1)/2 , self.divNodeGameMenue.size[1] * 0.96),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="Score :   0", 
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
          
        self.scoreTeam2 = avg.WordsNode(pos = ((self.xstartFeld2 + self.xendFeld2)/2 , self.divNodeGameMenue.size[1] * 0.96),
                                      fontsize = 0.022*self.divNodeGameMenue.size[1], 
                                      text ="Score :   0",  
                                      parent = self.divNodeGameMenue, 
                                      color = "000000", font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        #Optionevents
        self.background.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.background, self.startOptionMenu)
        self.optionMenu.buttonResume.connectEventHandler(avg.CURSORDOWN, avg.TOUCH, self.optionMenu.buttonResume, self.stopOptionMenue)
#fuer Matrix feld initialisierung 
        self.yUnten =  self.yOben + self.tetrishoehe
        self.field1 = Field(self.xstartFeld1, self.xendFeld1, self.yOben, self.yUnten,self.blocksize,self.player,self)
        self.field2 = Field(self.xstartFeld2, self.xendFeld2, self.yOben, self.yUnten,self.blocksize,self.player,self)
        self.attackerNormalField1 = AttackerSkills(self.field1,self.player)
        self.attackerNormalField2 = AttackerSkills(self.field2,self.player)
        self.attackerSpezialonField1 = AttackerSpecials(self.field2, self.field1,self.player)
        self.attackerSpezialonField2 = AttackerSpecials(self.field1, self.field2,self.player)
        self.defenderSkillsField1 = DefenderSkills(self.field1, self.player)
        self.defenderSkillsField2 = DefenderSkills(self.field2, self.player)
        this = avg.SoundNode(href="gameStart.mp3", loop=False, volume=1.0, parent = self.rootNode)
        this.play()
        self.SkillActivator = self.player.setInterval(120000, self.activateOneSkill)
        
        #TODO: loeschbarmacen:
        self.field2.chanceSpeed(8000);
        
        print "Tetrisfeldbegrenzungen:   lF1:",self.xstartFeld1,"  rF1: ",self.xendFeld1,"   lF1F2: ",self.xstartFeld2,"  rF2:  ",self.xendFeld2,"  yO: ", self.yOben," yU: ", self.yUnten
        print "Ein Feld:  Blocksize:  ", self.blocksize, "    Hoehe:   ", self.tetrishoehe, "    Breite:  ", self.xendFeld1-self.xstartFeld1
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





    # Ueberpruefung der FeldPunkte
#         avg.RectNode(pos=(self.xstartFeld1, self.yOben)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         avg.RectNode(pos=(self.xendFeld1, self.yOben)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         avg.RectNode(pos=(self.xstartFeld1, self.yUnten)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         avg.RectNode(pos=(self.xendFeld1, self.yUnten)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         avg.RectNode(pos=(self.xstartFeld2, self.yOben)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         avg.RectNode(pos=(self.xendFeld2, self.yOben)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         avg.RectNode(pos=(self.xstartFeld2, self.yUnten)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         avg.RectNode(pos=(self.xendFeld2, self.yUnten)
#                      ,size =avg.Point2D(self.blocksize,self.blocksize),
#                      parent = self.divNodeGameMenue)
#         
        
        
        
        
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
                    if(self.round >= 4):
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
                #self.field2.chanceSpeed(self.speed[self.round-1])
                self.round += 1
                if(self.round >= 4):
                    self.field1.clearForNextRound()
                    self.player.clearInterval(self.timeLimitCounter)
                    
                    self.endeSpiel()
                else:
                    self.roundNumber.text = str(self.round)
                    self.speedNumber.text = str(self.round)
            else:
                count -= 1
                self.timerLimit.text = str(count)
    
#TODO: eventuell Spiel beenden lassen      
    def rundenWechsel(self):
        self.field1.clearForNextRound()
        #TODO: self.field2.clearForNextRound()
        self.round += 1
        self.roundNumber.text = str(self.round)
        self.speedNumber.text = str(self.round)
        this = avg.SoundNode(href="round.mp3", loop=False, volume=1.0, parent = self.rootNode)
        this.play()

        
    def fieldChanceRundenWechsel(self):
        
        self.field1.speed = self.speed[(self.round -1)]
        self.field1.timer = self.field1.player.setInterval(self.field1.speed, self.field1.gravity)
        #self.field2.speed = self.speed[(self.round -1)]
        #self.field2.timer = self.field2.player.setInterval(self.field2.speed, self.field2.gravity)
        self.field1.initBlock()
#TODO:         self.field2.initBlock()

        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
    def endeSpiel(self, winner = "check"):
        if(winner == "check"):
            scoreTeam1 = self.field1.score
            scoreTeam2 = self.field2.score
            if(scoreTeam1 == scoreTeam2):
                winner = "Unentschieden"
            elif(scoreTeam1 > scoreTeam2):
                winner = "Team 1"
            elif(scoreTeam1 < scoreTeam2):
                winner = "Team 2"
        self.divNodeGameMenue.active = False
        self.winLooseMenu.buttonNextGame.sensitive = True
        self.winLooseMenu.buttonSomeOneWon.updateTextNode(winner)
        self.winLooseMenu.divNodeWinLooseMenue.active = True
        this = avg.SoundNode(href="victory.mp3", loop=False, volume=1.0, parent = self.rootNode)
        this.play()
    
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
        
        
    def activateOneSkill(self): #schaltet nach 2 minuten einen cooldown fuer den Angreifer frei

        randomNumber = random.randint(1,7)
        if (randomNumber == 1):
            if (self.rightFreezeActive == True):
                self.activateOneSkill()
            else:
                self.rightFreezeActive = True
                self.countOfSkillsActivated += 1
                this = avg.SoundNode(href="skillUnlocked.mp3", loop=False, volume=1.0, parent = self.rootNode)
                this.play()
        elif (randomNumber == 2):
            if (self.leftFreezeActive == True):
                self.activateOneSkill()
            else:
                self.leftFreezeActive = True
                self.countOfSkillsActivated += 1
                this = avg.SoundNode(href="skillUnlocked.mp3", loop=False, volume=1.0, parent = self.rootNode)
                this.play()
        elif (randomNumber == 3):
            if (self.rotateFreezeActive == True):
                self.activateOneSkill()
            else:
                self.rotateFreezeActive = True
                self.countOfSkillsActivated += 1
                this = avg.SoundNode(href="skillUnlocked.mp3", loop=False, volume=1.0, parent = self.rootNode)
                this.play()
        elif (randomNumber == 4):
            if (self.noPointsActive == True):
                self.activateOneSkill()
            else:
                self.noPointsActive = True
                self.countOfSkillsActivated += 1
                this = avg.SoundNode(href="skillUnlocked.mp3", loop=False, volume=1.0, parent = self.rootNode)
                this.play()
        elif (randomNumber == 5):
            if (self.inverseControlActive == True):
                self.activateOneSkill()
            else:
                self.inverseControlActive = True
                self.countOfSkillsActivated += 1
                this = avg.SoundNode(href="skillUnlocked.mp3", loop=False, volume=1.0, parent = self.rootNode)
                this.play()
        elif (randomNumber == 6):
            if (self.makeBlockInvisibleActive == True):
                self.activateOneSkill()
            else:
                self.makeBlockInvisibleActive = True
                self.countOfSkillsActivated += 1
                this = avg.SoundNode(href="skillUnlocked.mp3", loop=False, volume=1.0, parent = self.rootNode)
                this.play()
        else:
            if (self.speedUpActive == True):
                self.activateOneSkill()
            else:
                self.speedUpActive = True
                self.countOfSkillsActivated += 1
                this = avg.SoundNode(href="skillUnlocked.mp3", loop=False, volume=1.0, parent = self.rootNode)
                this.play()
        if (self.countOfSkillsActivated == 7):
            avg.Player.clearInterval(self.SkillActivator)
