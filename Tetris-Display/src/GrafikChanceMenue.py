'''
Created on 14.07.2013

@author: SebastianS
'''
from TextRectNode import TextRectNode
from libavg import avg

class GrafikChanceMenue(object):

    def __init__(self, parent, player):
        self.rootNode = parent
        self.divNodeGrafikMenue = avg.DivNode(parent = self.rootNode, size  = self.rootNode.size, active = False)
        self.background = avg.RectNode(parent = self.divNodeGrafikMenue, pos = (0,0), sensitive = True, fillcolor = "0040FF", fillopacity = 1, color = "0040FF", size = self.divNodeGrafikMenue.size )  
        self.header = TextRectNode(parent = self.divNodeGrafikMenue, 
                                   pos = (0,0),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodeGrafikMenue.size[0],self.divNodeGrafikMenue.size[1]*0.25)
                                   )
        
        self.header.addText("MultiTetris")
        
        self.buttonAufloesung = TextRectNode(parent = self.divNodeGrafikMenue, 
                                   pos = (self.divNodeGrafikMenue.size[0]*0.3,self.divNodeGrafikMenue.size[1]*0.25),
                                   fillcolor ="0040FF",
                                   fillopacity=1,
                                   color = "0040FF",
                                   size = avg.Point2D(self.divNodeGrafikMenue.size[0]*0.25,self.divNodeGrafikMenue.size[1]*0.15))
        self.buttonAufloesung.addTextGameTypeAndMain("Aufloesung")

        self.buttonLaenge = TextRectNode(parent = self.divNodeGrafikMenue, 
                                   pos = (self.divNodeGrafikMenue.size[0]*0.40,self.divNodeGrafikMenue.size[1]*0.45),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeGrafikMenue.size[0]*0.15,self.divNodeGrafikMenue.size[1]*0.10))
        self.buttonLaenge.addTextGameTypeAndMain("Laenge")
         
        self.buttonBreite = TextRectNode(parent = self.divNodeGrafikMenue, 
                                   pos = (self.divNodeGrafikMenue.size[0]*0.40,self.divNodeGrafikMenue.size[1]*0.60),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeGrafikMenue.size[0]*0.15,self.divNodeGrafikMenue.size[1]*0.10))
        self.buttonBreite.addTextGameTypeAndMain("Breite")
        
        
        
        self.buttonBack = TextRectNode(parent = self.divNodeGrafikMenue, 
                                   pos = (self.divNodeGrafikMenue.size[0]*0.40,self.divNodeGrafikMenue.size[1]*0.75),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeGrafikMenue.size[0]*0.15,self.divNodeGrafikMenue.size[1]*0.10))
        self.buttonBack.addTextGameTypeAndMain("Back")
    
    
#-----------------------------------------------------------------------------------------------------------------------------
        self.buttonLaengeM = TextRectNode(parent = self.divNodeGrafikMenue, 
                                   pos = (self.divNodeGrafikMenue.size[0]*0.275,self.divNodeGrafikMenue.size[1]*0.45),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeGrafikMenue.size[0]*0.1,self.divNodeGrafikMenue.size[1]*0.1))
        self.buttonLaengeM.addTextGameTypeAndMain("-")
        
        self.buttonLaengeMM = TextRectNode(parent = self.divNodeGrafikMenue, 
                                   pos = (self.divNodeGrafikMenue.size[0]*0.15,self.divNodeGrafikMenue.size[1]*0.45),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeGrafikMenue.size[0]*0.1,self.divNodeGrafikMenue.size[1]*0.1))
        self.buttonLaengeMM.addTextGameTypeAndMain("- -")
        
        self.buttonLaengeP = TextRectNode(parent = self.divNodeGrafikMenue, 
                                   pos = (self.divNodeGrafikMenue.size[0]*0.575,self.divNodeGrafikMenue.size[1]*0.45),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeGrafikMenue.size[0]*0.1,self.divNodeGrafikMenue.size[1]*0.1))
        self.buttonLaengeP.addTextGameTypeAndMain("+")
        
        self.buttonLaengePP = TextRectNode(parent = self.divNodeGrafikMenue, 
                                   pos = (self.divNodeGrafikMenue.size[0]*0.70,self.divNodeGrafikMenue.size[1]*0.45),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeGrafikMenue.size[0]*0.1,self.divNodeGrafikMenue.size[1]*0.1))
        self.buttonLaengePP.addTextGameTypeAndMain("+ +")
    
    
#-----------------------------------------------------------------------------------------------------------------------------
        self.buttonBreiteM = TextRectNode(parent = self.divNodeGrafikMenue, 
                                   pos = (self.divNodeGrafikMenue.size[0]*0.275,self.divNodeGrafikMenue.size[1]*0.60),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeGrafikMenue.size[0]*0.1,self.divNodeGrafikMenue.size[1]*0.1))
        self.buttonBreiteM.addTextGameTypeAndMain("-")
        
        self.buttonBreiteMM = TextRectNode(parent = self.divNodeGrafikMenue, 
                                   pos = (self.divNodeGrafikMenue.size[0]*0.15,self.divNodeGrafikMenue.size[1]*0.60),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeGrafikMenue.size[0]*0.1,self.divNodeGrafikMenue.size[1]*0.1))
        self.buttonBreiteMM.addTextGameTypeAndMain("- -")
        
        self.buttonBreiteP = TextRectNode(parent = self.divNodeGrafikMenue, 
                                   pos = (self.divNodeGrafikMenue.size[0]*0.575,self.divNodeGrafikMenue.size[1]*0.60),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeGrafikMenue.size[0]*0.1,self.divNodeGrafikMenue.size[1]*0.1))
        self.buttonBreiteP.addTextGameTypeAndMain("+")
        
        self.buttonBreitePP = TextRectNode(parent = self.divNodeGrafikMenue, 
                                   pos = (self.divNodeGrafikMenue.size[0]*0.70,self.divNodeGrafikMenue.size[1]*0.60),
                                   fillcolor ="0404B4",
                                   fillopacity=1,
                                   color = "0404B4",
                                   size = avg.Point2D(self.divNodeGrafikMenue.size[0]*0.1,self.divNodeGrafikMenue.size[1]*0.1))
        self.buttonBreitePP.addTextGameTypeAndMain("+ +")


