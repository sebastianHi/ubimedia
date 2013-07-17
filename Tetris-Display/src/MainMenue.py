from libavg import avg
from TextRectNode import TextRectNode

class MainMenue(object):

        def __init__(self, parent):
            
            self.rootNode = parent
            self.divNodeMainMenue = avg.DivNode(parent = self.rootNode, size  = self.rootNode.size)
            
            self.background = avg.ImageNode(parent = self.divNodeMainMenue, href = "DatBG.png", size = self.divNodeMainMenue.size)
            self.header = TextRectNode(parent = self.divNodeMainMenue, 
                                       pos = (0,0),href = "DatBG.png",
                                       size = avg.Point2D(self.divNodeMainMenue.size[0],self.divNodeMainMenue.size[1]*0.25)
                                       )
            
            self.header.addText("MultiTetris")
            self.header.setActivity(False)
            
            self.buttonCreateGame = TextRectNode(parent = self.divNodeMainMenue, 
                                       pos = (self.divNodeMainMenue.size[0]*0.3,self.divNodeMainMenue.size[1]*0.25),
                                       href = "DatBG.png",
                                       size = avg.Point2D(self.divNodeMainMenue.size[0]*0.25,self.divNodeMainMenue.size[1]*0.15))
            self.buttonCreateGame.addTextGameTypeAndMain("  Create Game:  ")
            self.buttonCreateGame.setActivity(False)
            
            self.button1vs1 = TextRectNode(parent = self.divNodeMainMenue, 
                                       pos = (self.divNodeMainMenue.size[0]*0.40,self.divNodeMainMenue.size[1]*0.45),
                                       href = "DatBG.png",
                                       size = avg.Point2D(self.divNodeMainMenue.size[0]*0.15,self.divNodeMainMenue.size[1]*0.10))
            self.button1vs1.addTextGameTypeAndMain("1vs1")
            
            self.button2vs2 = TextRectNode(parent = self.divNodeMainMenue, 
                                       pos = (self.divNodeMainMenue.size[0]*0.40,self.divNodeMainMenue.size[1]*0.75),
                                       href = "DatBG.png",
                                       size = avg.Point2D(self.divNodeMainMenue.size[0]*0.15,self.divNodeMainMenue.size[1]*0.10))
            self.button2vs2.addTextGameTypeAndMain("2vs2")
            
            self.button1vs1vs1 = TextRectNode(parent = self.divNodeMainMenue, 
                                       pos = (self.divNodeMainMenue.size[0]*0.40,self.divNodeMainMenue.size[1]*0.60),
                                       href = "DatBG.png",
                                       size = avg.Point2D(self.divNodeMainMenue.size[0]*0.15,self.divNodeMainMenue.size[1]*0.10))
            self.button1vs1vs1.addTextGameTypeAndMain("1vs1vs1")
            
   
