'''
Created on 10.07.2013

@author: Niko
'''
class AttackerSpecials(object):

#TODO: Es werden 2 Felder benoetigt, das Feld vom Gegner wo die Specials benutzt werden und das Field wo das eigene
# score gesenkt werden muss ?!
    
    def __init__(self, Field, Player): 
        self.player = Player
        self.field = Field

        
    def orderSuperBlock(self):
        self.field.superBlock = True
        self.field.updateScore(-10)
        
    def orderRainOfBlocks(self):
        self.field.tetrisRainActivated = True
        self.field.updateScore(-10)
    
    def orderThunder(self):
        self.field.thunderActivated = True
        self.field.updateScore(-10)