'''
Created on 10.07.2013

@author: Niko
'''
class DefenderSkills(object):
    
    def __init__(self, Field, Player):
        self.player = Player
        self.field = Field
      
    def skipBlock(self):
        pass #TODO: this
        
    def slowPace(self):
        pass #TODO: this
    
    def orderBomb(self):
        self.field.bombActivated = True
        
    def reduceTime(self):
        pass #TODO: