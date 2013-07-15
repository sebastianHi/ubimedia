'''
Created on 20.06.2013

@author: sebastian
'''
from libavg import avg

class TextRectNode(avg.RectNode):
    
    def addText(self, text , color = "000000"):
        self.textNode = avg.WordsNode(pos = (self.pos[0] + self.size[0]/2, self.pos[1]+ self.size[1]/2 - (0.30*self.size[1]/2)),
                                      fontsize = 0.5*self.size[1], 
                                      text ="Classic-Mode", 
                                      parent = self.getParent(), 
                                      color = color, 
                                      font = "arial", 
                                      alignment = "center",
                                      sensitive = False
                                      )
        while((self.textNode.size[0] >= self.size[0])):
            self.textNode.fontsize -=1
        self.textNode.text = text
            
        
    def addTextGameTypeAndMain(self, text , color = "000000"):
        self.textNode = avg.WordsNode(pos = (self.pos[0] + self.size[0]/2, self.pos[1]+ self.size[1]/2 - (0.30*self.size[1]/2)),
                                      fontsize = 0.5*self.size[1], 
                                      text ="Classic-Mode", 
                                      parent = self.getParent(), 
                                      color = color, 
                                      font = "arial", 
                                      alignment = "center",
                                      sensitive = False
                                      )
        while((self.textNode.size[0] >= self.size[0])):
            self.textNode.fontsize -=1
        self.textNode.text = text
        
    def getTextNode(self):
        return self.textNode
    
    def updateTextNode(self, newText):
        self.textNode.text = newText
        
    def setInactiv(self):
        self.textNode.active = False
        self.active = False
    
    def setActiv(self):
        self.textNode.active = True
        self.active = True
        
    def addTextForBackButton(self, text, color = "000000"):
        self.textNode = avg.WordsNode(pos = (self.pos[0] + self.size[0]/2, self.pos[1]+ self.size[1]/2 - (0.30*self.size[1]/2)),
                                      fontsize = 0.45*self.size[1], 
                                      text =text, 
                                      parent = self.getParent(), 
                                      color = color, font = "arial", 
                                      alignment = "center",
                                      sensitive = False)
        while((self.textNode.size[0] >= self.size[0])):
            self.textNode.fontsize -=1
        self.textNode.text = text
        
        
    def addTextForLobbyLine(self, textA, textB , color = "000000" ):
        self.textNodeA = avg.WordsNode(pos = (self.pos[0]+ self.size[0]*0.1, self.pos[1]+ self.size[1]/2 - (0.30*self.size[1]/2)),
                                      fontsize = 0.45*self.size[1], 
                                      text ="Players connected:", 
                                      parent = self.getParent(), 
                                      color = color, font = "arial", 
                                      alignment = "left",
                                      sensitive = False)
        
        self.textNodeB = avg.WordsNode(pos = (self.pos[0]+self.size[0]-self.size[0]*0.1, self.pos[1]+ self.size[1]/2 - (0.30*self.size[1]/2)),
                                      fontsize = 0.45*self.size[1], 
                                      text =textB, 
                                      parent = self.getParent(), 
                                      color = color, font = "arial", 
                                      alignment = "right",
                                      sensitive = False)
        
        while(self.textNodeA.size[0] >= self.size[0]*0.7):
            self.textNodeA.fontsize-=1
        self.textNodeA.text = textA
        self.textNodeB.fontsize = self.textNodeA.fontsize
        
    def updateTextForLobbyLine(self,textA, textB):
        self.textNodeA.text = textA
        self.textNodeB.text = textB