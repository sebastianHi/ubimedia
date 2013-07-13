'''
Created on 10.07.2013

@author: Niko
'''
class DefenderSkills(object):
    
    def __init__(self, Field, Player):
        self.player = Player
        self.field = Field
      
    def skipBlock(self): #simply overrides the active block with a new one
        
        if (self.field.score - 5 < 0):
            pass
        else:
            self.field.updateScore(-5)
            self.field.initBlock()
            
    def slowPace(self): # slows down the falling pace by half a second for 5 seconds

        if (self.field.score - 5 < 0):
            pass
        else:
            self.field.updateScore(-5)
            self.field.chanceSpeed(self.field.speed + 500)
            self.duration = self.player.setInterval(5000, self.endSlowPace)
            
    def orderBomb(self):
        
        if (self.field.score - 8 < 0):
            pass
        else:
            self.field.updateScore(-8)
            self.field.specialsQueue.append("bomb")
            
    def reduceTime(self): #lowers the time of the active round by 30 seconds
        
        if (self.field.score - 5 < 0):
            pass
        else:
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