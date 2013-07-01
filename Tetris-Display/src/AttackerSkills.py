'''
Created on 01.07.2013

@author: sebastian
'''
class AttackerSkills(object):
    
    def __init__(self,field,player):
        self.player = player
        self.field = field
    
    def inverseControl(self):
        self.field.inverseSteuerung = True
        self.inverseTimer = self.player.setInterval(2000, self.remoteInverseControl)
    
    def leftFreeze(self):
        self.field.freezeLeft = True
        self.leftFreezeTimer = self.player.setInterval(2000, self.remoteLeftFreezeControl)
    
    def rightFreeze(self):
        self.field.freezeRight = True
        self.rightFreezeTimer = self.player.setInterval(2000, self.remoteRightFreezeControl)
    
    def rotateFreeze(self):
        self.field.freezeRotate = True
        self.rotateFreezeTimer = self.player.setInterval(2000, self.remoteRotateFreezeControl)
        
    def speedUp(self):
        self.speedy = self.player.setInterval(1000, self.speedDownAgain)
        self.field.chanceSpeed(self.field.speed - 300)
    
    def makeBlockInvisible(self):
        self.invisible = self.player.setInterval(2000, self.makeBlockVisible)
        self.field.block.part1.active = False
        self.field.block.part2.active = False
        self.field.block.part3.active = False
        self.field.block.part4.active = False
    
    def noPoints(self):
        #TODO:
        pass
    
    def speedDownAgain(self):
        self.player.clearInterval(self.speedy)
        self.field.chanceSpeed(self.field.speed)
    
    def makeBlockVisible(self):
        self.player.clearInterval(self.invisible)
        self.field.block.part1.active = False
        self.field.block.part2.active = False
        self.field.block.part3.active = False
        self.field.block.part4.active = False
    
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