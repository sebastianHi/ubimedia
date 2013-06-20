'''
Created on 20.06.2013

@author: sebastian
'''
from libavg import avg

class TextRectNode(avg.RectNode):
    
    def addText(self, text , color = "000000" ):
        self.textNode = avg.WordsNode(pos = (self.pos[0] + self.size[0]/2, self.pos[1]+ self.size[1]/2 - (0.30*self.size[1]/2)),fontsize = 0.30*self.size[1], text =text, parent = self.getParent(), color = color, font = "arial", alignment = "center")
    
    def getTextNode(self):
        return self.textNode
    
    def updateTextNode(self, newText):
        self.textNode.text = newText