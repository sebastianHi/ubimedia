from libavg import avg

class AttackerSkills(object):
    
    def __init__(self,field,player):
        self.player = player
        self.field = field
    
    def inverseControl(self):
        
        if (self.field.gameMenue.skillsOnCooldown == True):
            this = avg.SoundNode(href="denied.mp3", loop=False, volume=1.0, parent = self.field.gameMenue.rootNode)
            this.play()
        else:
            
            self.field.gameMenue.skillsOnCooldown = True
            self.cooldown = self.player.setInterval(30000, self.removeCooldown)
            self.field.inverseSteuerung = True
            self.inverseTimer = self.player.setInterval(2000, self.remoteInverseControl)
    
    def leftFreeze(self):
        
        if (self.field.gameMenue.skillsOnCooldown == True):
            this = avg.SoundNode(href="denied.mp3", loop=False, volume=1.0, parent = self.field.gameMenue.rootNode)
            this.play()
        else:
            
            self.field.gameMenue.skillsOnCooldown = True
            self.cooldown = self.player.setInterval(30000, self.removeCooldown)
            self.field.freezeLeft = True
            self.leftFreezeTimer = self.player.setInterval(2000, self.remoteLeftFreezeControl)
    
    def rightFreeze(self):
        
        if (self.field.gameMenue.skillsOnCooldown == True):
            this = avg.SoundNode(href="denied.mp3", loop=False, volume=1.0, parent = self.field.gameMenue.rootNode)
            this.play()
        else:
            
            self.field.gameMenue.skillsOnCooldown = True
            self.cooldown = self.player.setInterval(30000, self.removeCooldown)
            self.field.freezeRight = True
            self.rightFreezeTimer = self.player.setInterval(2000, self.remoteRightFreezeControl)
    
    def rotateFreeze(self):
        
        if (self.field.gameMenue.skillsOnCooldown == True):
            this = avg.SoundNode(href="denied.mp3", loop=False, volume=1.0, parent = self.field.gameMenue.rootNode)
            this.play()
        else:
            
            self.field.gameMenue.skillsOnCooldown = True
            self.cooldown = self.player.setInterval(30000, self.removeCooldown)
            self.field.freezeRotate = True
            self.rotateFreezeTimer = self.player.setInterval(2000, self.remoteRotateFreezeControl)
        
    def speedUp(self):
        
        if (self.field.gameMenue.skillsOnCooldown == True):
            this = avg.SoundNode(href="denied.mp3", loop=False, volume=1.0, parent = self.field.gameMenue.rootNode)
            this.play()
        else:
            
            self.field.gameMenue.skillsOnCooldown = True
            self.cooldown = self.player.setInterval(30000, self.removeCooldown)
            self.speedy = self.player.setInterval(1000, self.speedDownAgain)
            self.field.chanceSpeed(self.field.speed - 200)
    
    def makeBlockInvisible(self):
        if (self.field.gameMenue.skillsOnCooldown == True):
            this = avg.SoundNode(href="denied.mp3", loop=False, volume=1.0, parent = self.field.gameMenue.rootNode)
            this.play()
        else:
            
            self.field.gameMenue.skillsOnCooldown = True
            self.cooldown = self.player.setInterval(30000, self.removeCooldown)
            self.invisible = self.player.setInterval(2000, self.makeBlockVisible)
            if (self.field.block.blockType == "super"):
                self.field.block.part1.active = False
                self.field.block.part2.active = False
                self.field.block.part3.active = False
                self.field.block.part4.active = False
                self.field.block.part5.active = False
                self.field.block.part6.active = False
                self.field.block.part7.active = False
                self.field.block.part8.active = False
                self.field.block.part9.active = False
                self.field.block.part10.active = False
            elif (self.field.block.blockType == "bomb"):
                
                self.field.block.part1.active = False
            else:
                self.field.block.part1.active = False
                self.field.block.part2.active = False
                self.field.block.part3.active = False
                self.field.block.part4.active = False
    
    def noPoints(self):

        if (self.field.gameMenue.skillsOnCooldown == True):
            this = avg.SoundNode(href="denied.mp3", loop=False, volume=1.0, parent = self.field.gameMenue.rootNode)
            this.play()
        else:
            
            self.field.gameMenue.skillsOnCooldown = True
            self.cooldown = self.player.setInterval(30000, self.removeCooldown)
            self.duration = self.player.setInterval(10000, self.activateMoney)
            self.field.noMoneyForYou = True
        
    
    def speedDownAgain(self):

        self.player.clearInterval(self.speedy)
        self.field.chanceSpeed(self.field.speed)
    
    def makeBlockVisible(self):
        self.player.clearInterval(self.invisible)
        if (self.field.block.blockType == "super"):
            self.field.block.part1.active = True
            self.field.block.part2.active = True
            self.field.block.part3.active = True
            self.field.block.part4.active = True
            self.field.block.part5.active = True
            self.field.block.part6.active = True
            self.field.block.part7.active = True
            self.field.block.part8.active = True
            self.field.block.part9.active = True
            self.field.block.part10.active = True
        elif (self.field.block.blockType == "bomb"):
            
            self.field.block.part1.active = True
        else:
            self.field.block.part1.active = True
            self.field.block.part2.active = True
            self.field.block.part3.active = True
            self.field.block.part4.active = True
    
    def remoteInverseControl(self):
        self.player.clearInterval(self.inverseTimer)
        self.field.inverseSteuerung = False
        
    def remoteLeftFreezeControl(self):
        self.player.clearInterval(self.leftFreezeTimer)
        self.field.freezeLeft = False
        
    def remoteRightFreezeControl(self):
        self.player.clearInterval(self.rightFreezeTimer)
        self.field.freezeRight = False
        
    def remoteRotateFreezeControl(self):
        self.player.clearInterval(self.rotateFreezeTimer)
        self.field.freezeRotate = False 
        
    def activateMoney(self):
        self.player.clearInterval(self.duration)
        self.field.noMoneyForYou = False
        
    def removeCooldown(self):
        self.field.gameMenue.skillsOnCooldown = False
        self.player.clearInterval(self.cooldown)