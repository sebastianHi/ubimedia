from libavg import avg
from TextRectNode import TextRectNode

class WinLooseMenue(object):

        def __init__(self, parent):
            
            self.rootNode = parent
            self.divNodeWinLooseMenue = avg.DivNode(parent = self.rootNode, size  = self.rootNode.size, active = False)
            self.background = avg.RectNode(parent = self.divNodeWinLooseMenue, pos = (0,0), fillcolor = "0040FF", fillopacity = 1, color = "0040FF", size = self.divNodeWinLooseMenue.size )  
            self.header = TextRectNode(parent = self.divNodeWinLooseMenue, 
                                       pos = (0,0),
                                       fillcolor ="0040FF",
                                       fillopacity=1,
                                       color = "0040FF",
                                       size = avg.Point2D(self.divNodeWinLooseMenue.size[0],self.divNodeWinLooseMenue.size[1]*0.25)
                                       )
            
            self.header.addText("MultiTetris")
            
            self.buttonSomeOneWon = TextRectNode(parent = self.divNodeWinLooseMenue, 
                                       pos = (self.divNodeWinLooseMenue.size[0]*0.3,self.divNodeWinLooseMenue.size[1]*0.25),
                                       fillcolor ="0040FF",
                                       fillopacity=1,
                                       color = "0040FF",
                                       size = avg.Point2D(self.divNodeWinLooseMenue.size[0]*0.25,self.divNodeWinLooseMenue.size[1]*0.15))
            self.buttonSomeOneWon.addTextGameTypeAndMain("  SomeOneWon  ")
            
            self.buttonNextGame = TextRectNode(parent = self.divNodeWinLooseMenue, 
                                       pos = (self.divNodeWinLooseMenue.size[0]*0.40,self.divNodeWinLooseMenue.size[1]*0.45),
                                       fillcolor ="0404B4",
                                       fillopacity=1,
                                       sensitive = False,
                                       color = "0404B4",
                                       size = avg.Point2D(self.divNodeWinLooseMenue.size[0]*0.15,self.divNodeWinLooseMenue.size[1]*0.10))
            self.buttonNextGame.addTextGameTypeAndMain("Mainmenue")
            
           
