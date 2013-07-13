'''
Created on 10.07.2013

@author: Niko
'''
class AttackerSpecials(object):
    
    def __init__(self, FieldAttacker, FieldDefender, Player): 
        self.player = Player
        self.field1 = FieldAttacker
        self.field2 = FieldDefender

        
    def orderSuperBlock(self):
        
        if (self.field1.score - 10 < 0):
            pass
        else:
            self.field1.updateScore(-10)
            self.field2.specialsQueue.append("super")
    
    def orderRainOfBlocks(self):
        
        if (self.field1.score - 10 < 0):
            pass
        else:
            self.field1.updateScore(-20)
            self.field2.specialsQueue.append("rain")
    
    def orderThunder(self):
        
        if (self.field1.score - 10 < 0):
            pass
        else:
            self.field1.updateScore(-15)
            self.field2.specialsQueue.append("thunder")