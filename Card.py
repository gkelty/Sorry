import pygame
import os
import random

"""
This class contains information to create cards. 
"""
class Card:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(self.value)

"""
This class contains information to create and manipulate a deck of cards and display a card from the deck.
"""
class Deck:
    def __init__(self):
        self.cards = []
        values = ["1", "2", "3", "4", "5", "7", "8", "10", "11", "12", "S"]
        for i in range(4):
            for value in values:
                self.cards.append(Card(value))
        self.cards.append(Card("1"))

    def showCards(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()

    def getImage(self, path):
        global imageLibrary
        imageLibrary = {}
        image = imageLibrary.get(path)
        if image == None:
            canonicalizedPath = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalizedPath)
            imageLibrary[path] = image
        return image

    def displayCard(self, card):
        cardImagePaths = {'1': self.getImage('images\sorryCardBig1.png'), '2': self.getImage('images\sorryCardBig2.png'),
                          '3': self.getImage('images\sorryCardBig3.png'), '4': self.getImage('images\sorryCardBig4.png'),
                          '5': self.getImage('images\sorryCardBig5.png'), '7': self.getImage('images\sorryCardBig7.png'),
                          '8': self.getImage('images\sorryCardBig8.png'), '10': self.getImage('images\sorryCardBig10.png'),
                          '11': self.getImage('images\sorryCardBig11.png'), '12': self.getImage('images\sorryCardBig12.png'),
                          'S': self.getImage('images\sorryCardBigSorry.png')}
        cardImage = cardImagePaths[card]
        return cardImage
