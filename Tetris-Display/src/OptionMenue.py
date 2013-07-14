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
        self.background = avg.RectNode(parent = self.divNodeOptionMenue, pos = (0,0), sensitive = True, fillcolor = "0040FF", fillopacity = 1, color = "0040FF", size = self.divNodeOptionMenue.size )  
        self.header = TextRectNode(parent = self.divNodeOptionMenue, 
                                   pos = (0,0),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodeOptionMenue.size[0],self.divNodeOptionMenue.size[1]*0.25)
                                   )
        
        self.header.addText("MultiTetris")
        
        self.buttonPause = TextRectNode(parent = self.divNodeOptionMenue, 
                                   pos = (self.divNodeOptionMenue.size[0]*0.3,self.divNodeOptionMenue.size[1]*0.25),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodeOptionMenue.size[0]*0.25,self.divNodeOptionMenue.size[1]*0.15))
        self.buttonPause.addTextGameTypeAndMain("Pause")

        self.buttonResume = TextRectNode(parent = self.divNodeOptionMenue, 
                                   pos = (self.divNodeOptionMenue.size[0]*0.40,self.divNodeOptionMenue.size[1]*0.42),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeOptionMenue.size[0]*0.15,self.divNodeOptionMenue.size[1]*0.10))
        self.buttonResume.addTextGameTypeAndMain("Resume")
         
        self.buttonGrafik = TextRectNode(parent = self.divNodeOptionMenue, 
                                   pos = (self.divNodeOptionMenue.size[0]*0.40,self.divNodeOptionMenue.size[1]*0.57),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeOptionMenue.size[0]*0.15,self.divNodeOptionMenue.size[1]*0.10))
        self.buttonGrafik.addTextGameTypeAndMain("Grafik")
   
        
        self.buttonSound = TextRectNode(parent = self.divNodeOptionMenue, 
                                   pos = (self.divNodeOptionMenue.size[0]*0.40,self.divNodeOptionMenue.size[1]*0.72),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeOptionMenue.size[0]*0.15,self.divNodeOptionMenue.size[1]*0.10))
        self.buttonSound.addTextGameTypeAndMain("Sound:  An")
        
        self.buttonFinish = TextRectNode(parent = self.divNodeOptionMenue, 
                                   pos = (self.divNodeOptionMenue.size[0]*0.40,self.divNodeOptionMenue.size[1]*0.87),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeOptionMenue.size[0]*0.15,self.divNodeOptionMenue.size[1]*0.10))
        self.buttonFinish.addTextGameTypeAndMain("Beenden")
    
    

