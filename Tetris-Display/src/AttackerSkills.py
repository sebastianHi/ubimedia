class AttackerSkills(object):
    
    def __init__(self,field,player):
        self.player = player
        self.field = field
        self.which = ""
    
    def inverseControl(self):
        self.field.inverseSteuerung = True
        self.inverseTimer = self.player.setInterval(20000, self.remoteInverseControl)
    
    def leftFreeze(self):
        self.field.freezeLeft = True
        self.leftFreezeTimer = self.player.setInterval(20000, self.remoteLeftFreezeControl)
    
    def rightFreeze(self):
        self.field.freezeRight = True
        self.rightFreezeTimer = self.player.setInterval(20000, self.remoteRightFreezeControl)

    def rotateFreeze(self):
        self.field.freezeRotate = True
        self.rotateFreezeTimer = self.player.setInterval(20000, self.remoteRotateFreezeControl)
        
    def speedUp(self):
        self.speedy = self.player.setInterval(20000, self.speedDownAgain)
        self.field.chanceSpeed(self.field.speed - 300)
    
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
                
                self.part1.opacity  = 0.0
                self.part2.opacity  = 0.0
                self.part3.opacity  = 0.0
                self.part4.opacity  = 0.0
                self.part5.opacity  = 0.0
                self.part6.opacity  = 0.0
                self.part7.opacity  = 0.0
                self.part8.opacity  = 0.0
                self.part9.opacity  = 0.0
                self.part10.opacity = 0.0
                
            elif ((self.field.block.blockType == "bomb") | (self.field.block.blockType == "rain")):
                self.which = "bomb"
                self.part1 = self.field.block.part1
                self.part1.opacity = 0.0
            else:
                self.part1  = self.field.block.part1
                self.part2  = self.field.block.part2
                self.part3  = self.field.block.part3
                self.part4  = self.field.block.part4
                
                self.part1.opacity  = 0.0
                self.part2.opacity  = 0.0
                self.part3.opacity  = 0.0
                self.part4.opacity  = 0.0
    
    def noPoints(self):
        self.duration = self.player.setInterval(10000, self.activateMoney)
        self.field.noMoneyForYou = True
        
    
    def speedDownAgain(self):
        self.player.clearInterval(self.speedy)
        self.field.chanceSpeed(self.field.speed)
    
    def makeBlockVisible(self):
        self.player.clearInterval(self.invisible)
        if (self.which == "super"):
            self.part1.opacity  = 1.0
            self.part2.opacity  = 1.0
            self.part3.opacity  = 1.0
            self.part4.opacity  = 1.0
            self.part5.opacity  = 1.0
            self.part6.opacity  = 1.0
            self.part7.opacity  = 1.0
            self.part8.opacity  = 1.0
            self.part9.opacity  = 1.0
            self.part10.opacity = 1.0
        elif (self.which == "bomb"):
            self.part1.opacity  = 1.0
        else:
            self.part1.opacity  = 1.0
            self.part2.opacity  = 1.0
            self.part3.opacity  = 1.0
            self.part4.opacity  = 1.0
    
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
        