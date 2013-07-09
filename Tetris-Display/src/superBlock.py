from libavg import avg


class superBlock(object):



    def __init__(self, GameMenue, Field):
        
        self.part1 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (6 * GameMenue.blocksize), Field.yWertOben), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part2 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (5 * GameMenue.blocksize), Field.yWertOben + GameMenue.blocksize), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part3 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (6 * GameMenue.blocksize), Field.yWertOben + GameMenue.blocksize), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part4 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (4 * GameMenue.blocksize), Field.yWertOben + (2 * GameMenue.blocksize)), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part5 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (5 * GameMenue.blocksize), Field.yWertOben + (2 * GameMenue.blocksize)), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part6 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (7 * GameMenue.blocksize), Field.yWertOben + (2 * GameMenue.blocksize)), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part7 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (8 * GameMenue.blocksize), Field.yWertOben + (2 * GameMenue.blocksize)), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part8 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (6 * GameMenue.blocksize), Field.yWertOben + (3 * GameMenue.blocksize)), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part9 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (7 * GameMenue.blocksize), Field.yWertOben + (3 * GameMenue.blocksize)), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )
        self.part10 = avg.RectNode(parent = GameMenue.divNodeGameMenue, 
                                  pos = (Field.xWertLinksOben+ (6 * GameMenue.blocksize), Field.yWertOben + (4 * GameMenue.blocksize)), 
                                  fillcolor = "FF0000", fillopacity = 1, color = "000000", 
                                  size = avg.Point2D(GameMenue.blocksize ,GameMenue.blocksize)
                                  )

        
        self.GameMenue = GameMenue
        self.Field = Field
        self.currPos1 = (6,0)
        self.currPos2 = (5,1)
        self.currPos3 = (6,1)
        self.currPos4 = (4,2)
        self.currPos5 = (5,2)
        self.currPos6 = (7,2)
        self.currPos7 = (8,2)
        self.currPos8 = (6,3)
        self.currPos9 = (7,3)
        self.currPos10 = (6,4)
        self.blockType = "super"
        self.rotatingPosition = 0 
        
    
    def moveBlockLeft(self):
        if(self.checkLeftBound()):
            self.currPos1 = (self.currPos1[0] - 1,self.currPos1[1])
            self.currPos2 = (self.currPos2[0] - 1,self.currPos2[1])
            self.currPos3 = (self.currPos3[0] - 1,self.currPos3[1])
            self.currPos4 = (self.currPos4[0] - 1,self.currPos4[1])
            self.currPos5 = (self.currPos5[0] - 1,self.currPos5[1])
            self.currPos6 = (self.currPos6[0] - 1,self.currPos6[1])
            self.currPos7 = (self.currPos7[0] - 1,self.currPos7[1])
            self.currPos8 = (self.currPos8[0] - 1,self.currPos8[1])
            self.currPos9 = (self.currPos9[0] - 1,self.currPos9[1])
            self.currPos10 = (self.currPos10[0] - 1,self.currPos10[1])

            self.part1.pos = ((self.part1.pos[0] - self.GameMenue.blocksize),self.part1.pos[1])
            self.part2.pos = ((self.part2.pos[0] - self.GameMenue.blocksize),self.part2.pos[1])
            self.part3.pos = ((self.part3.pos[0] - self.GameMenue.blocksize),self.part3.pos[1])
            self.part4.pos = ((self.part4.pos[0] - self.GameMenue.blocksize),self.part4.pos[1])
            self.part5.pos = ((self.part5.pos[0] - self.GameMenue.blocksize),self.part5.pos[1])
            self.part6.pos = ((self.part6.pos[0] - self.GameMenue.blocksize),self.part6.pos[1])
            self.part7.pos = ((self.part7.pos[0] - self.GameMenue.blocksize),self.part7.pos[1])
            self.part8.pos = ((self.part8.pos[0] - self.GameMenue.blocksize),self.part8.pos[1])
            self.part9.pos = ((self.part9.pos[0] - self.GameMenue.blocksize),self.part9.pos[1])
            self.part10.pos = ((self.part10.pos[0] - self.GameMenue.blocksize),self.part10.pos[1])

        else:
            pass  # dont move dat shit
        
    def moveBlockRight(self):
        
        if(self.checkRightBound()):
            self.currPos1 = (self.currPos1[0] + 1,self.currPos1[1])
            self.currPos2 = (self.currPos2[0] + 1,self.currPos2[1])
            self.currPos3 = (self.currPos3[0] + 1,self.currPos3[1])
            self.currPos4 = (self.currPos4[0] + 1,self.currPos4[1])
            self.currPos5 = (self.currPos5[0] + 1,self.currPos5[1])
            self.currPos6 = (self.currPos6[0] + 1,self.currPos6[1])
            self.currPos7 = (self.currPos7[0] + 1,self.currPos7[1])
            self.currPos8 = (self.currPos8[0] + 1,self.currPos8[1])
            self.currPos9 = (self.currPos9[0] + 1,self.currPos9[1])
            self.currPos10 = (self.currPos10[0] + 1,self.currPos10[1])

            self.part1.pos = ((self.part1.pos[0] + self.GameMenue.blocksize),self.part1.pos[1])
            self.part2.pos = ((self.part2.pos[0] + self.GameMenue.blocksize),self.part2.pos[1])
            self.part3.pos = ((self.part3.pos[0] + self.GameMenue.blocksize),self.part3.pos[1])
            self.part4.pos = ((self.part4.pos[0] + self.GameMenue.blocksize),self.part4.pos[1])
            self.part5.pos = ((self.part5.pos[0] + self.GameMenue.blocksize),self.part5.pos[1])
            self.part6.pos = ((self.part6.pos[0] + self.GameMenue.blocksize),self.part6.pos[1])
            self.part7.pos = ((self.part7.pos[0] + self.GameMenue.blocksize),self.part7.pos[1])
            self.part8.pos = ((self.part8.pos[0] + self.GameMenue.blocksize),self.part8.pos[1])
            self.part9.pos = ((self.part9.pos[0] + self.GameMenue.blocksize),self.part9.pos[1])
            self.part10.pos = ((self.part10.pos[0] + self.GameMenue.blocksize),self.part10.pos[1])
        else:
            pass  # dont move dat shit
        
    def rotateLeft(self):
        self.rotateRight()
    
    def rotateRight(self):
        if (self.rotatingPosition == 0):
            if (self.checkCollisionAtRotation(0)):
                pass
            else:
                self.currPos2 = (self.currPos2[0] + 2,self.currPos2[1])
                self.currPos9 = (self.currPos9[0] - 2,self.currPos9[1])
                self.part2.pos = ((self.part2.pos[0] + (2 * self.GameMenue.blocksize)),self.part2.pos[1])
                self.part9.pos = ((self.part9.pos[0] - (2 * self.GameMenue.blocksize)),self.part9.pos[1])
                self.rotatingPosition = 1
        else:
            if (self.checkCollisionAtRotation(1)):
                pass
            else:
                self.currPos2 = (self.currPos2[0] - 2,self.currPos2[1])
                self.currPos9 = (self.currPos9[0] + 2,self.currPos9[1])
                self.part2.pos = ((self.part2.pos[0] - (2 * self.GameMenue.blocksize)),self.part2.pos[1])
                self.part9.pos = ((self.part9.pos[0] + (2 * self.GameMenue.blocksize)),self.part9.pos[1])
                self.rotatingPosition = 0
                
    def hitGround(self): # gibt True zurueck, wenn es den "Boden" bzw ein Hindernis beruehrt, sonst False
        if((self.currPos1[1] + 1 > 18) | (self.currPos2[1] + 1 > 18) | (self.currPos3[1] + 1> 18) 
           |(self.currPos4[1] + 1> 18) | (self.currPos5[1] + 1 > 18) | (self.currPos6[1] + 1> 18)
           | (self.currPos7[1] + 1 > 18) | (self.currPos8[1] + 1> 18) | (self.currPos9[1] + 1 > 18)
            | (self.currPos10[1] + 1> 18)):
            return True
        a = self.Field.matrix[self.currPos2[0]][self.currPos2[1] + 1]
        b = self.Field.matrix[self.currPos3[0]][self.currPos3[1] + 1]
        c = self.Field.matrix[self.currPos4[0]][self.currPos4[1] + 1]
        d = self.Field.matrix[self.currPos1[0]][self.currPos1[1] + 1]
        e = self.Field.matrix[self.currPos5[0]][self.currPos5[1] + 1]
        f = self.Field.matrix[self.currPos6[0]][self.currPos6[1] + 1]
        g = self.Field.matrix[self.currPos7[0]][self.currPos7[1] + 1]
        h = self.Field.matrix[self.currPos8[0]][self.currPos8[1] + 1]
        i = self.Field.matrix[self.currPos9[0]][self.currPos9[1] + 1]
        j = self.Field.matrix[self.currPos10[0]][self.currPos10[1] + 1]

        
        if (a or b or c or d or e or f or g or h or i or j):
            return True
        else:
            return False

    def checkLeftBound(self): #return true wenn bewegung moeglich
        if (self.rotatingPosition == 0):
            
            # pruefe part 1,2,4,8,10
            if((self.currPos1[0]-1 < 0)  | (self.currPos2[0]-1 < 0) | (self.currPos4[0]-1 < 0) 
               | (self.currPos8[0]-1 < 0) | (self.currPos10[0]-1 < 0)):
                return False
            else:
                a = self.Field.matrix[self.currPos1[0] - 1][self.currPos1[1]]
                b = self.Field.matrix[self.currPos2[0] - 1][self.currPos2[1]]
                c = self.Field.matrix[self.currPos4[0] - 1][self.currPos4[1]]
                d = self.Field.matrix[self.currPos8[0] - 1][self.currPos8[1]]
                e = self.Field.matrix[self.currPos10[0] - 1][self.currPos10[1]]
                if (a or b or c or d or e):
                    return False
                else:
                    return True
        else:
            # pruefe part 4,5,7,9,10
            if((self.currPos4[0]-1 < 0)  | (self.currPos5[0]-1 < 0) | (self.currPos7[0]-1 < 0) 
               | (self.currPos9[0]-1 < 0) | (self.currPos10[0]-1 < 0)):
                return False
            else:
                a = self.Field.matrix[self.currPos4[0] - 1][self.currPos4[1]]
                b = self.Field.matrix[self.currPos5[0] - 1][self.currPos5[1]]
                c = self.Field.matrix[self.currPos7[0] - 1][self.currPos7[1]]
                d = self.Field.matrix[self.currPos9[0] - 1][self.currPos9[1]]
                e = self.Field.matrix[self.currPos10[0] - 1][self.currPos10[1]]
                if (a or b or c or d or e):
                    return False
                else:
                    return True
 
            
    
    def checkRightBound(self):#return true wenn bewegung moeglich, prueft nur rechten unteren Block
        if (self.rotatingPosition == 0):
            
            # pruefe part 1,3,7,9,10
            if((self.currPos1[0]+1 > 13) | (self.currPos3[0]+1 > 13) | (self.currPos7[0]+1 > 13)
               | (self.currPos9[0]+1 > 13) | (self.currPos10[0]+1 > 13)):
                return False
            else:
                a = self.Field.matrix[self.currPos1[0] + 1][self.currPos1[1]]
                b = self.Field.matrix[self.currPos3[0] + 1][self.currPos3[1]]
                c = self.Field.matrix[self.currPos7[0] + 1][self.currPos7[1]]
                d = self.Field.matrix[self.currPos9[0] + 1][self.currPos9[1]]
                e = self.Field.matrix[self.currPos10[0] + 1][self.currPos10[1]]
                if (a or b or c or d or e):
                    return False
                else:
                    return True
        else:
            # pruefe part 1,2,4,6,7
            if((self.currPos1[0]+1 > 13) | (self.currPos2[0]+1 > 13) | (self.currPos4[0]+1 > 13)
               | (self.currPos6[0]+1 > 13) | (self.currPos7[0]+1 > 13)):
                return False
            else:
                a = self.Field.matrix[self.currPos1[0] + 1][self.currPos1[1]]
                b = self.Field.matrix[self.currPos2[0] + 1][self.currPos2[1]]
                c = self.Field.matrix[self.currPos4[0] + 1][self.currPos4[1]]
                d = self.Field.matrix[self.currPos6[0] + 1][self.currPos6[1]]
                e = self.Field.matrix[self.currPos7[0] + 1][self.currPos7[1]]
                if (a or b or c or d or e):
                    return False
                else:
                    return True
                
    def checkCollisionAtRotation(self, RotatingNumber): # True = Collison, False = No Collision
    
        if (RotatingNumber == 0):
            a = self.Field.matrix[self.currPos2[0] + 2][self.currPos2[1]]
            b = self.Field.matrix[self.currPos9[0] - 2][self.currPos9[1]]
            if  (b or a):
                return True
            else:
                return False
                
        else:

            a = self.Field.matrix[self.currPos2[0] - 2][self.currPos2[1]]
            b = self.Field.matrix[self.currPos9[0] + 2][self.currPos9[1]]
            if  (b or a):
                return True
            else:
                return False
            
    def steadyBlockSuper(self):
        self.Field.matrixSteadyRectNodes[self.currPos1[0]][self.currPos1[1]] = self.part1
        self.Field.matrixSteadyRectNodes[self.currPos2[0]][self.currPos2[1]] = self.part2
        self.Field.matrixSteadyRectNodes[self.currPos3[0]][self.currPos3[1]] = self.part3
        self.Field.matrixSteadyRectNodes[self.currPos4[0]][self.currPos4[1]] = self.part4
        self.Field.matrixSteadyRectNodes[self.currPos5[0]][self.currPos5[1]] = self.part5
        self.Field.matrixSteadyRectNodes[self.currPos6[0]][self.currPos6[1]] = self.part6
        self.Field.matrixSteadyRectNodes[self.currPos7[0]][self.currPos7[1]] = self.part7
        self.Field.matrixSteadyRectNodes[self.currPos8[0]][self.currPos8[1]] = self.part8
        self.Field.matrixSteadyRectNodes[self.currPos9[0]][self.currPos9[1]] = self.part9
        self.Field.matrixSteadyRectNodes[self.currPos10[0]][self.currPos10[1]] = self.part10

        self.Field.matrix[self.currPos1[0]][self.currPos1[1]] = True
        self.Field.matrix[self.currPos2[0]][self.currPos2[1]] = True
        self.Field.matrix[self.currPos3[0]][self.currPos3[1]] = True
        self.Field.matrix[self.currPos4[0]][self.currPos4[1]] = True
        self.Field.matrix[self.currPos5[0]][self.currPos5[1]] = True
        self.Field.matrix[self.currPos6[0]][self.currPos6[1]] = True
        self.Field.matrix[self.currPos7[0]][self.currPos7[1]] = True
        self.Field.matrix[self.currPos8[0]][self.currPos8[1]] = True
        self.Field.matrix[self.currPos9[0]][self.currPos9[1]] = True
        self.Field.matrix[self.currPos10[0]][self.currPos10[1]] = True

        self.Field.player.clearInterval(self.Field.timer)
        
    def setBlock(self):
        self.currPos1 = (self.currPos1[0] ,self.currPos1[1] +1)
        self.currPos2 = (self.currPos2[0] ,self.currPos2[1] +1)
        self.currPos3 = (self.currPos3[0] ,self.currPos3[1] +1)
        self.currPos4 = (self.currPos4[0] ,self.currPos4[1] +1)
        self.currPos5 = (self.currPos5[0] ,self.currPos5[1] +1)
        self.currPos6 = (self.currPos6[0] ,self.currPos6[1] +1)
        self.currPos7 = (self.currPos7[0] ,self.currPos7[1] +1)
        self.currPos8 = (self.currPos8[0] ,self.currPos8[1] +1)
        self.currPos9 = (self.currPos9[0] ,self.currPos9[1] +1)
        self.currPos10 = (self.currPos10[0] ,self.currPos10[1] +1)

        self.part1.pos = (self.part1.pos[0],self.part1.pos[1] + self.gameMenue.blocksize)
        self.part2.pos = (self.part2.pos[0],self.part2.pos[1] + self.gameMenue.blocksize)
        self.part3.pos = (self.part3.pos[0],self.part3.pos[1] + self.gameMenue.blocksize)
        self.part4.pos = (self.part4.pos[0],self.part4.pos[1] + self.gameMenue.blocksize)
        self.part5.pos = (self.part5.pos[0],self.part5.pos[1] + self.gameMenue.blocksize)
        self.part6.pos = (self.part6.pos[0],self.part6.pos[1] + self.gameMenue.blocksize)
        self.part7.pos = (self.part7.pos[0],self.part7.pos[1] + self.gameMenue.blocksize)
        self.part8.pos = (self.part8.pos[0],self.part8.pos[1] + self.gameMenue.blocksize)
        self.part9.pos = (self.part9.pos[0],self.part9.pos[1] + self.gameMenue.blocksize)
        self.part10.pos = (self.part10.pos[0],self.part10.pos[1] + self.gameMenue.blocksize)
        