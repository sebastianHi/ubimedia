from TextRectNode import TextRectNode
from libavg import avg

class OptionMenue(object):

# Resume
# Sound
# Grafik
# Exit

    def __init__(self, parent):
        self.rootNode = parent
        self.divNodeOptionMenue = avg.DivNode(parent = self.rootNode, size  = self.rootNode.size, active = False)
        self.background = avg.ImageNode(parent = self.divNodeGameMenue, href = "DatBG.png", size = self.divNodeGameMenue.size)
        self.header = TextRectNode(parent = self.divNodeOptionMenue, 
                                   href = "DatBG.png",
                                   pos = (0,0),
                                   size = avg.Point2D(self.divNodeOptionMenue.size[0],self.divNodeOptionMenue.size[1]*0.25)
                                   )
        
        self.header.addText("MultiTetris")
        self.header.setActivity(False)
        
        self.buttonPause = TextRectNode(parent = self.divNodeOptionMenue, 
                                   pos = (self.divNodeOptionMenue.size[0]*0.3,self.divNodeOptionMenue.size[1]*0.25),
                                   href = "Overlay1.png",
                                   size = avg.Point2D(self.divNodeOptionMenue.size[0]*0.25,self.divNodeOptionMenue.size[1]*0.15))
        self.buttonPause.addTextGameTypeAndMain("Pause")
        self.buttonPause.setActivity(False)

        self.buttonResume = TextRectNode(parent = self.divNodeOptionMenue, 
                                   pos = (self.divNodeOptionMenue.size[0]*0.40,self.divNodeOptionMenue.size[1]*0.42),
                                   href = "Overlay1.png",
                                   size = avg.Point2D(self.divNodeOptionMenue.size[0]*0.15,self.divNodeOptionMenue.size[1]*0.10))
        self.buttonResume.addTextGameTypeAndMain("Resume")
        
        self.buttonSound = TextRectNode(parent = self.divNodeOptionMenue, 
                                   pos = (self.divNodeOptionMenue.size[0]*0.40,self.divNodeOptionMenue.size[1]*0.57),
                                   href = "Overlay1.png",
                                   size = avg.Point2D(self.divNodeOptionMenue.size[0]*0.15,self.divNodeOptionMenue.size[1]*0.10))
        self.buttonSound.addTextGameTypeAndMain("Sound:  ON")
        
        self.buttonFinish = TextRectNode(parent = self.divNodeOptionMenue, 
                                   pos = (self.divNodeOptionMenue.size[0]*0.40,self.divNodeOptionMenue.size[1]*0.72),
                                   href = "Overlay1.png",
                                   size = avg.Point2D(self.divNodeOptionMenue.size[0]*0.15,self.divNodeOptionMenue.size[1]*0.10))
        self.buttonFinish.addTextGameTypeAndMain("Quit")
    
    

