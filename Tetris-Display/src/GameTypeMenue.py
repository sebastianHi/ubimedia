from libavg import avg
from TextRectNode import TextRectNode

class GameTypeMenue(object):

        def __init__(self, parent):
            self.rootNode = parent
            self.divNodeTypeMenue = avg.DivNode(parent = self.rootNode, size  = self.rootNode.size)
            self.background = avg.ImageNode(parent = self.divNodeTypeMenue, href = "DatBG.png", size = self.divNodeTypeMenue.size)
            self.header = TextRectNode(parent = self.divNodeTypeMenue, 
                                       pos = (0,0),
                                       href = "DatBG.png",
                                       size = avg.Point2D(self.divNodeTypeMenue.size[0],self.divNodeTypeMenue.size[1]*0.25)
                                       )
            
            self.header.addText("MultiTetris")
            self.header.setActivity(False)
            
            self.buttonCreateGame = TextRectNode(parent = self.divNodeTypeMenue, 
                                       pos = (self.divNodeTypeMenue.size[0]*0.3,self.divNodeTypeMenue.size[1]*0.25),
                                       href = "DatBG.png",
                                       size = avg.Point2D(self.divNodeTypeMenue.size[0]*0.25,self.divNodeTypeMenue.size[1]*0.15))
            self.buttonCreateGame.addTextGameTypeAndMain("Choose Gametype:")
            self.buttonCreateGame.setActivity(False)

            self.buttonEqualMode = TextRectNode(parent = self.divNodeTypeMenue, 
                                       pos = (self.divNodeTypeMenue.size[0]*0.40,self.divNodeTypeMenue.size[1]*0.45),
                                       href = "DatBG.png",
                                       size = avg.Point2D(self.divNodeTypeMenue.size[0]*0.15,self.divNodeTypeMenue.size[1]*0.10))
            self.buttonEqualMode.addTextGameTypeAndMain("Equal-Mode")
             
            self.buttonNormalMode = TextRectNode(parent = self.divNodeTypeMenue, 
                                       pos = (self.divNodeTypeMenue.size[0]*0.40,self.divNodeTypeMenue.size[1]*0.60),
                                       href = "DatBG.png",
                                       size = avg.Point2D(self.divNodeTypeMenue.size[0]*0.15,self.divNodeTypeMenue.size[1]*0.10))
            self.buttonNormalMode.addTextGameTypeAndMain("Classic-Mode")
            
            self.backButton = TextRectNode(parent = self.divNodeTypeMenue, 
                                       pos = (self.divNodeTypeMenue.size[0]*0.40,self.divNodeTypeMenue.size[1]*0.75),
                                       href = "DatBG.png",
                                       size = avg.Point2D(self.divNodeTypeMenue.size[0]*0.15,self.divNodeTypeMenue.size[1]*0.10))
            self.backButton.addTextGameTypeAndMain("Back")
            

        
        
