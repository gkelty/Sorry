import pygame
from Button import Button
GREEN = (50, 200, 20)
class BoardButton():
    def __init__(self,tileNum,location):
        self.tileNum = str(tileNum)
        self.location = location
    def createBoard(self):
        boardButton = Button(self.tileNum, self.location, self.testin(),
                             buttonColor=GREEN, buttonSize=(35,35))
        return(boardButton)

    def testin(self):
        print(self.tileNum)
        print(self.location)