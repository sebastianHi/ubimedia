'''
Created on 10.07.2013

@author: Niko
'''
class AttackerSpecials(object):

#TODO: Es werden 2 Felder benoetigt, das Feld vom Gegner wo die Specials benutzt werden und das Field wo das eigene
# score gesenkt werden muss ?!
    
    def __init__(self, FieldAttacker, FieldDefender, Player): 
        self.player = Player
        self.field1 = FieldAttacker
        self.field2 = FieldDefender

        
    def orderSuperBlock(self):
        self.field2.superBlock = True
        self.field1.updateScore(-10)
        
    def orderRainOfBlocks(self):
        self.field2.tetrisRainActivated = True
        self.field1.updateScore(-10)
    
    def orderThunder(self):
        self.field2.thunderActivated = True
        self.field1.updateScore(-10)