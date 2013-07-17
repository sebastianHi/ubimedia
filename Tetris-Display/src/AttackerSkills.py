class AttackerSkills(object):
    
    def __init__(self,field,player):
        self.player = player
        self.field = field
        self.which = ""
    
    # aktiviert inverse Steuerung
    def inverseControl(self):
        self.field.inverseSteuerung = True
        self.inverseTimer = self.player.setInterval(20000, self.remoteInverseControl)
    
    # aktiviert linker Freeze
    def leftFreeze(self):
        self.field.freezeLeft = True
        self.leftFreezeTimer = self.player.setInterval(20000, self.remoteLeftFreezeControl)
    

    # aktiviert rechter Freeze
    def rightFreeze(self):
        self.field.freezeRight = True
        self.rightFreezeTimer = self.player.setInterval(20000, self.remoteRightFreezeControl)

    # aktiviert rotate Freeze
    def rotateFreeze(self):
        self.field.freezeRotate = True
        self.rotateFreezeTimer = self.player.setInterval(20000, self.remoteRotateFreezeControl)
     
    # aktiviert geschwindigkeitserhoehung    
    def speedUp(self):
        self.field.chanceSpeed(self.field.speed - 300)
        self.speedy = self.player.setInterval(20000, self.speedDownAgain)
    
    # aktiviert Unsichtbarkeit der Bloecke
    def makeBlockInvisible(self):
        if(self.field.block != None):
            self.invisible = self.player.setInterval(2000, self.makeBlockVisible)
            if (self.field.block.blockType == "super"):
                self.which = "super"
                self.part1  = self.field.block.part1
                self.part2  = self.field.block.part2
                self.part3  = self.field.block.part3
                self.part4  = self.field.block.part4
                self.part5  = self.field.block.part5
                self.part6  = self.field.block.part6
                self.part7  = self.field.block.part7
                self.part8  = self.field.block.part8
                self.part9  = self.field.block.part9
                self.part10 = self.field.block.part10
                
                self.part1.active  = True
                self.part2.active  = True
                self.part3.active  = True
                self.part4.active  = True
                self.part5.active  = True
                self.part6.active  = True
                self.part7.active  = True
                self.part8.active  = True
                self.part9.active  = True
                self.part10.active = True
                
            elif ((self.field.block.blockType == "bomb") | (self.field.block.blockType == "rain")):
                self.which = "bomb"
                self.part1 = self.field.block.part1
                self.part1.active = True
            else:
                self.part1  = self.field.block.part1
                self.part2  = self.field.block.part2
                self.part3  = self.field.block.part3
                self.part4  = self.field.block.part4
                
                self.part1.active  = True
                self.part2.active  = True
                self.part3.active  = True
                self.part4.active  = True
    
    # aktiviert keine Punktevergabe
    def noPoints(self):
        self.duration = self.player.setInterval(10000, self.activateMoney)
        self.field.noMoneyForYou = True
        
    # deaktiviert geschwindigkeitserhoehung
    def speedDownAgain(self):
        self.player.clearInterval(self.speedy)
        self.field.chanceSpeed(self.field.speed)
    
    # deaktiviert Unsichtbarkeit der Bloecke
    def makeBlockVisible(self):
        self.player.clearInterval(self.invisible)
        if (self.which == "super"):
            self.part1.active  = True
            self.part2.active  = True
            self.part3.active  = True
            self.part4.active  = True
            self.part5.active  = True
            self.part6.active  = True
            self.part7.active  = True
            self.part8.active  = True
            self.part9.active  = True
            self.part10.active = True
        elif (self.which == "bomb"):
            self.part1.active  = True
        else:
            self.part1.active  = True
            self.part2.active  = True
            self.part3.active  = True
            self.part4.active  = True
    
    # deaktiviert inverse Steuerung
    def remoteInverseControl(self):
        self.player.clearInterval(self.inverseTimer)
        self.field.inverseSteuerung = False
     
    # deaktiviert linker Freeze 
    def remoteLeftFreezeControl(self):
        self.player.clearInterval(self.leftFreezeTimer)
        self.field.freezeLeft = False
     
    # deaktiviert rechter Freeze     
    def remoteRightFreezeControl(self):
        self.player.clearInterval(self.rightFreezeTimer)
        self.field.freezeRight = False
    
    # deaktiviert rotate Freeze    
    def remoteRotateFreezeControl(self):
        self.player.clearInterval(self.rotateFreezeTimer)
        self.field.freezeRotate = False 
    
    #  aktiviert Punktevergabe    
    def activateMoney(self):
        self.player.clearInterval(self.duration)
        self.field.noMoneyForYou = False
        