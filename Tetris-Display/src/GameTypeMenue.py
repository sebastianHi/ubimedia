from libavg import avg
from TextRectNode import TextRectNode

class GameTypeMenue(object):

        def __init__(self, parent):
            self.rootNode = parent
            self.divNodeTypeMenue = avg.DivNode(parent = self.rootNode, size  = self.rootNode.size)
            self.background = avg.RectNode(parent = self.divNodeTypeMenue, pos = (0,0), fillcolor = "0040FF", fillopacity = 1, color = "0040FF", size = self.divNodeTypeMenue.size )  
            self.header = TextRectNode(parent = self.divNodeTypeMenue, 
                                       pos = (0,0),
                                       fillcolor ="0040FF",
                                       fillopacity=1,
                                       color = "0040FF",
                                       size = avg.Point2D(self.divNodeTypeMenue.size[0],self.divNodeTypeMenue.size[1]*0.25)
                                       )
            
            self.header.addText("MultiTetris")
            
            self.buttonCreateGame = TextRectNode(parent = self.divNodeTypeMenue, 
                                       pos = (self.divNodeTypeMenue.size[0]*0.3,self.divNodeTypeMenue.size[1]*0.25),
                                       fillcolor ="0040FF",
                                       fillopacity=1,
                                       color = "0040FF",
                                       size = avg.Point2D(self.divNodeTypeMenue.size[0]*0.25,self.divNodeTypeMenue.size[1]*0.15))
            self.buttonCreateGame.addText("Choose Gametype:")
            
            self.buttonEqualMode = TextRectNode(parent = self.divNodeTypeMenue, 
                                       pos = (self.divNodeTypeMenue.size[0]*0.40,self.divNodeTypeMenue.size[1]*0.40),
                                       fillcolor ="0404B4",
                                       fillopacity=1,
                                       color = "0404B4",
                                       size = avg.Point2D(self.divNodeTypeMenue.size[0]*0.15,self.divNodeTypeMenue.size[1]*0.10))
            self.buttonEqualMode.addText("Equal-Mode")
             
            self.buttonNormalMode = TextRectNode(parent = self.divNodeTypeMenue, 
                                       pos = (self.divNodeTypeMenue.size[0]*0.40,self.divNodeTypeMenue.size[1]*0.55),
                                       fillcolor ="0404B4",
                                       fillopacity=1,
                                       color = "0404B4",
                                       size = avg.Point2D(self.divNodeTypeMenue.size[0]*0.15,self.divNodeTypeMenue.size[1]*0.10))
            self.buttonNormalMode.addText("Classic-Mode")
            
            self.backButton = TextRectNode(parent = self.divNodeTypeMenue, 
                                       pos = (self.divNodeTypeMenue.size[0]*0.40,self.divNodeTypeMenue.size[1]*0.70),
                                       fillcolor ="0404B4",
                                       fillopacity=1,
                                       color = "0404B4",
                                       size = avg.Point2D(self.divNodeTypeMenue.size[0]*0.15,self.divNodeTypeMenue.size[1]*0.10))
            self.backButton.addText("Back")
            
            
        
        
