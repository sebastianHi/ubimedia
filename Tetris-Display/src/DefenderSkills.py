'''
Created on 10.07.2013

@author: Niko
'''
class DefenderSkills(object):
    
    def __init__(self, Field, Player):
        self.player = Player
        self.field = Field
        
    # ueberspringt den aktuellen fallenden Block  
    def skipBlock(self): #simply overrides the active block with a new one
        
        if (self.field.score - 1 < 0):
            pass
        else:
            self.field.updateScore(-1)
            self.player.clearInterval(self.field.timer)
            if (self.field.block is None):
                pass
            elif(self.field.block.blockType == "super"):
                self.field.block.part1.unlink()
                self.field.block.part2.unlink()
                self.field.block.part3.unlink()
                self.field.block.part4.unlink()
                self.field.block.part5.unlink()
                self.field.block.part6.unlink()
                self.field.block.part7.unlink()
                self.field.block.part8.unlink()
                self.field.block.part9.unlink()
                self.field.block.part10.unlink()
            elif (self.field.block.blockType == "bomb") or (self.field.block.blockType == "rain"):
                self.field.block.part1.unlink()
            else:        
                self.field.block.part1.unlink()
                self.field.block.part2.unlink()
                self.field.block.part3.unlink()
                self.field.block.part4.unlink()
            self.field.block = None
            self.field.blockHitGround()
            
    # slows down the falling pace by half a second for 5 seconds        
    def slowPace(self): 

        if (self.field.score - 1 < 0):
            pass
        else:
            self.field.updateScore(-1)
            self.field.chanceSpeed(self.field.speed + 200)
            self.duration = self.player.setInterval(5000, self.endSlowPace)
    
    # erzeugt eine Bombe         
    def orderBomb(self):
        
        if (self.field.score - 3 < 0):
            pass
        else:
            self.field.updateScore(-3)
            self.field.specialsQueue.append("bomb")
     
    #lowers the time of the active round by 30 seconds      
    def reduceTime(self): 
        
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
    
    #beendet langsame geschwindigkeit    
    def endSlowPace(self):
        self.field.chanceSpeed(self.field.speed - 200)
        self.player.clearInterval(self.duration)