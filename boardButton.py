import pygame

TRANSPARENT = (0, 0, 0, 0)
class BoardButton():
    def __init__(self,tileNum,locationX,locationY):
        self.tileNum = str(tileNum)

        self.location = (locationX,locationY)
    def getLocation(self):
        return(self.location)
    def getTileNum(self):
        return(self.tileNum)
    def testin(self):
        print(self.tileNum)
        print(self.location)