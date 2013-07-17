from libavg import avg
from TextRectNode import TextRectNode

class WinLooseMenue(object):

        def __init__(self, parent):
            
            self.rootNode = parent
            self.divNodeWinLooseMenue = avg.DivNode(parent = self.rootNode, size  = self.rootNode.size, active = False)
            self.background = avg.ImageNode(parent = self.divNodeWinLooseMenue, href = "DatBG.png", size = self.divNodeWinLooseMenue.size) 
            self.header = TextRectNode(parent = self.divNodeWinLooseMenue, 
                                       pos = (0,0),
                                       href = "Overlay1.png",
                                       size = avg.Point2D(self.divNodeWinLooseMenue.size[0],self.divNodeWinLooseMenue.size[1]*0.25)
                                       )
            
            self.header.addText("MultiTetris")
            self.header.setActivity(False)
            
            self.buttonSomeOneWon = TextRectNode(parent = self.divNodeWinLooseMenue, 
                                       pos = (self.divNodeWinLooseMenue.size[0]*0.3,self.divNodeWinLooseMenue.size[1]*0.25),
                                       href = "Overlay1.png",
                                       size = avg.Point2D(self.divNodeWinLooseMenue.size[0]*0.25,self.divNodeWinLooseMenue.size[1]*0.15))
            self.buttonSomeOneWon.addTextGameTypeAndMain("  SomeOneWon  ")
            
            self.buttonSomeOneWon.setActivity(False)
            
            self.buttonNextGame = TextRectNode(parent = self.divNodeWinLooseMenue, 
                                       pos = (self.divNodeWinLooseMenue.size[0]*0.40,self.divNodeWinLooseMenue.size[1]*0.45),
                                       sensitive = False,
                                       href = "Overlay1.png",
                                       size = avg.Point2D(self.divNodeWinLooseMenue.size[0]*0.15,self.divNodeWinLooseMenue.size[1]*0.10))
            self.buttonNextGame.addTextGameTypeAndMain("Mainmenue")
            
           
