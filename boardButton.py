import pygame
#Invisible buttons behind the image of our board to add functionality
TRANSPARENT = (0, 0, 0, 0)
class BoardButton():
    #Creates the object giving it a tile numberand a location from the list of pawn locations
    def __init__(self,tileNum,locationX,locationY):
        self.tileNum = str(tileNum)

        self.location = (locationX,locationY)
    #Returns the corresponding values
    def getLocation(self):
        return(self.location)
    def getTileNum(self):
        return(self.tileNum)
