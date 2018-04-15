import os
import pygame

imageLibrary = {}

def getImage(path):
    global imageLibrary
    image = imageLibrary.get(path)
    if image == None:
            canonicalizedPath = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalizedPath)
            imageLibrary[path] = image
    return image

#def getPawnImage(self, color):
#    pawnImages = {'green': self.getImage('images\sorryPawnGreen.png'),
#                       'blue': self.getImage('images\sorryPawnBlue.png'),
#                       'yellow': self.getImage('images\sorryPawnYellow.png'),
#                       'red': self.getImage('images\sorryPawnRed.png')}
#    return pawnImages[color]

#def getboardImage(self):
#    boardImage = self.getImage('images\sorrysorryGameBoardCombined.png')

