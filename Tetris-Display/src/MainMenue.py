from libavg import avg
from TextRectNode import TextRectNode

class MainMenue(object):

        def __init__(self, parent):
            
            self.rootNode = parent
            self.divNodeMainMenue = avg.DivNode(parent = self.rootNode, size  = self.rootNode.size)
            self.background = avg.RectNode(parent = self.divNodeMainMenue, pos = (0,0), fillcolor = "0040FF", fillopacity = 1, color = "0040FF", size = self.divNodeMainMenue.size )  
            self.header = TextRectNode(parent = self.divNodeMainMenue, 
                                       pos = (0,0),
                                       fillcolor ="0040FF",
                                       fillopacity=1,
                                       color = "0040FF",
                                       size = avg.Point2D(self.divNodeMainMenue.size[0],self.divNodeMainMenue.size[1]*0.25)
                                       )
            
            self.header.addText("MultiTetris")
            
            self.buttonCreateGame = TextRectNode(parent = self.divNodeMainMenue, 
                                       pos = (self.divNodeMainMenue.size[0]*0.3,self.divNodeMainMenue.size[1]*0.25),
                                       fillcolor ="0040FF",
                                       fillopacity=1,
                                       color = "0040FF",
                                       size = avg.Point2D(self.divNodeMainMenue.size[0]*0.25,self.divNodeMainMenue.size[1]*0.15))
            self.buttonCreateGame.addTextGameTypeAndMain("  Create Game:  ")
            
            self.button1vs1 = TextRectNode(parent = self.divNodeMainMenue, 
                                       pos = (self.divNodeMainMenue.size[0]*0.40,self.divNodeMainMenue.size[1]*0.40),
                                       fillcolor ="0404B4",
                                       fillopacity=1,
                                       color = "0404B4",
                                       size = avg.Point2D(self.divNodeMainMenue.size[0]*0.15,self.divNodeMainMenue.size[1]*0.10))
            self.button1vs1.addTextGameTypeAndMain("1vs1")
            
            self.button2vs2 = TextRectNode(parent = self.divNodeMainMenue, 
                                       pos = (self.divNodeMainMenue.size[0]*0.40,self.divNodeMainMenue.size[1]*0.70),
                                       fillcolor ="0404B4",
                                       fillopacity=1,
                                       color = "0404B4",
                                       size = avg.Point2D(self.divNodeMainMenue.size[0]*0.15,self.divNodeMainMenue.size[1]*0.10))
            self.button2vs2.addTextGameTypeAndMain("2vs2")
            
            self.button1vs1vs1 = TextRectNode(parent = self.divNodeMainMenue, 
                                       pos = (self.divNodeMainMenue.size[0]*0.40,self.divNodeMainMenue.size[1]*0.55),
                                       fillcolor ="0404B4",
                                       fillopacity=1,
                                       color = "0404B4",
                                       size = avg.Point2D(self.divNodeMainMenue.size[0]*0.15,self.divNodeMainMenue.size[1]*0.10))
            self.button1vs1vs1.addTextGameTypeAndMain("1vs1vs1")
            
   
