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
