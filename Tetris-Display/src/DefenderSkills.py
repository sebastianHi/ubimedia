'''
Created on 10.07.2013

@author: Niko
'''
class DefenderSkills(object):
    
    def __init__(self, Field, Player):
        self.player = Player
        self.field = Field
      
    def skipBlock(self): #simply overrides the active block with a new one
        self.field.initBlock()
        self.field.updateScore(-5)
        
    def slowPace(self): # slows down the falling pace by half a second for 5 seconds
        self.field.chanceSpeed(self.field.speed + 500)
        self.duration = self.player.setInterval(5000, self.endSlowPace)
        self.field.updateScore(-5)
    
    def orderBomb(self):
        self.field.bombActivated = True
        self.field.updateScore(-10)
        
    def reduceTime(self): #lowers the time of the active round by 30 seconds
        oldValue = int (self.field.gameMenue.timerLimit.text)
        oldValue -= 30
        if (oldValue < 1):
            self.field.gameMenue.timerLimit.text = 1
        else:
            self.field.gameMenue.timerLimit.text = oldValue
        self.field.updateScore(-5)
        
    def endSlowPace(self):
        self.field.chanceSpeed(self.field.speed - 500)
        self.player.clearInterval(self.duration)