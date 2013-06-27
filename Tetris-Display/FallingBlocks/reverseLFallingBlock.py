from libavg import avg
from src import FallingBlock,GameMenue

class reverseLFallingBlock(FallingBlock):



    def __init__(self):
        
        self.part1 = avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (self.linksFeld1X+ (8 * self.blocksize), self.yOben + self.Blocksize), 
                                  fillcolor = "00FFFF", fillopacity = 1, color = "00FFFF", 
                                  size = avg.Point2D(self.blocksize ,self.blocksize)
                                  )
        self.part2 = avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (self.linksFeld1X+ (6 * self.blocksize), self.yOben), 
                                  fillcolor = "00FFFF", fillopacity = 1, color = "00FFFF", 
                                  size = avg.Point2D(self.blocksize ,self.blocksize)
                                  )
        self.part3 = avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (self.linksFeld1X+ (7 * self.blocksize), self.yOben), 
                                  fillcolor = "00FFFF", fillopacity = 1, color = "00FFFF", 
                                  size = avg.Point2D(self.blocksize ,self.blocksize)
                                  )
        self.part4 = avg.RectNode(parent = self.divNodeGameMenue, 
                                  pos = (self.linksFeld1X+ (8 * self.blocksize), self.yOben), 
                                  fillcolor = "00FFFF", fillopacity = 1, color = "00FFFF", 
                                  size = avg.Point2D(self.blocksize ,self.blocksize)
                                  )