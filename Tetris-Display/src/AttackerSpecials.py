'''
Created on 10.07.2013

@author: Niko
'''
class AttackerSpecials(object):
    
    def __init__(self, Field, Player):
        self.player = Player
        self.field = Field

        
    def orderSuperBlock(self):
        self.field.superBlock = True
        
    def orderRainOfBlocks(self):
        pass #TODO: have fun
    
    def orderThunder(self):
        pass #TODO: muss unbedingt nen sound mit abspielen, sonst wird das recht unspektakulaer und nicht mal bemerkbar