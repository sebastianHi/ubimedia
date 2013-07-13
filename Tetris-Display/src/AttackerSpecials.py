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
        self.field2.superBlock = True
        self.field1.updateScore(-10) #TODO: genug geld??
        
    def orderRainOfBlocks(self):
        self.field2.tetrisRainActivated = True
        self.field1.updateScore(-10)
    
    def orderThunder(self):
        self.field2.thunderActivated = True
        self.field1.updateScore(-10)