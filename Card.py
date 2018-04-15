import pygame
import random
import Image

"""
This class contains information to create cards. 
"""
class Card:
    cardImages = {'1': Image.getImage('images\sorryCardBig1.png'),
                  '2': Image.getImage('images\sorryCardBig2.png'),
                  '3': Image.getImage('images\sorryCardBig3.png'),
                  '4': Image.getImage('images\sorryCardBig4.png'),
                  '5': Image.getImage('images\sorryCardBig5.png'),
                  '7': Image.getImage('images\sorryCardBig7.png'),
                  '8': Image.getImage('images\sorryCardBig8.png'),
                  '10': Image.getImage('images\sorryCardBig10.png'),
                  '11': Image.getImage('images\sorryCardBig11.png'),
                  '12': Image.getImage('images\sorryCardBig12.png'),
                  'S': Image.getImage('images\sorryCardBigSorry.png')}

    def __init__(self, value):
        self.value = value
        self.image = Card.cardImages[value]

    def show(self):
        print(self.value)

    def getCardImage(self):
        return self.image

"""
This class contains information to create and manipulate a deck of cards and display a card from the deck.
"""
class Deck:
    def __init__(self):
        self.cards = []
        self.values = ["1", "2", "3", "4", "5", "7", "8", "10", "11", "12", "S"]
        self.currentCard = None
        for i in range(4):
            for value in self.values:
                self.cards.append(Card(value))
        self.cards.append(Card("1"))

    def showCards(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        self.currentCard = self.cards.pop()
        #return self.currentCard

    def discardCard(self):
        self.currentCard = None

    def displayCard(self, screen, location):
        screen.blit(self.currentCard.getCardImage(), location)
