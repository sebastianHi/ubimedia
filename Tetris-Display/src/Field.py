from FallingBlock import FallingBlock

class Field(object):

    def __init__(self, xWertLinksOben, xWertRechtsOben, yWertOben, yWertUnten, blocksize):
        self.xWertLinksOben = xWertLinksOben
        self.xWertRechtsOben = xWertRechtsOben
        self.yWertOben = yWertOben
        self.yWertUnten = yWertUnten
        
        self.gravity = 1
        #queue die gefuellt wird durch phone, new falling stone danach mit dem naechsten rufen
        pass
        
        
    
    
    def hitGround(self, node):#return true wenn bewegung moeglich
        pass
    
   
    def newFallingStone(self, node):#  <-- rufe stein, der macht den rest. gebe das feld mit.
        ##if queue leer dann random sonst erstes element der queue
        pass
    
    