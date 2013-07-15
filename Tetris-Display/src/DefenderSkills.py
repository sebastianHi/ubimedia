'''
Created on 10.07.2013

@author: Niko
'''
class DefenderSkills(object):
    
    def __init__(self, Field, Player):
        self.player = Player
        self.field = Field
      
    def skipBlock(self): #simply overrides the active block with a new one
        
        if (self.field.score - 1 < 0):
            pass
        else:
            self.field.updateScore(-1)
            self.player.clearInterval(self.timer)
            if (self.block is None):
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
            self.field.blockHitGround()
            
    def slowPace(self): # slows down the falling pace by half a second for 5 seconds

        if (self.field.score - 1 < 0):
            pass
        else:
            self.field.updateScore(-1)
            self.field.chanceSpeed(self.field.speed + 500)
            self.duration = self.player.setInterval(5000, self.endSlowPace)
            
    def orderBomb(self):
        
        if (self.field.score - 3 < 0):
            pass
        else:
            self.field.updateScore(-3)
            self.field.specialsQueue.append("bomb")
            
    def reduceTime(self): #lowers the time of the active round by 30 seconds
        
        if (self.field.score - 3 < 0):
            pass
        else:
            oldValue = int (self.field.gameMenue.timerLimit.text)
            oldValue -= 30
            if (oldValue < 1):
                self.field.gameMenue.timerLimit.text = str(1)
            else:
                self.field.gameMenue.timerLimit.text = str(oldValue)
            self.field.updateScore(-3)
        
    def endSlowPace(self):
        self.field.chanceSpeed(self.field.speed - 500)
        self.player.clearInterval(self.duration)