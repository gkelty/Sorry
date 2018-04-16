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
    drawPileImage = Image.getImage('images\sorryCardBackSmall.png')
    values = ["1", "2", "3", "4", "5", "7", "8", "10", "11", "12", "S"]
    def __init__(self):
        self.cards = []
        self.drawPileActive = True
        self.currentCard = None
        self.discard = None
        for i in range(4):
            for value in Deck.values:
                self.cards.append(Card(value))
        self.cards.append(Card("1"))

    def showCards(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        self.currentCard = self.cards.pop()
        if len(self.cards) == 0:
            self.drawPileActive = False
        return self.drawPileActive

    def discardCard(self):
        if self.currentCard != None:
            self.discard = pygame.transform.rotozoom(self.currentCard.getCardImage(), 90, 0.3)
        self.currentCard = None


    def displayDeck(self, screen, drawPileLocation, discardPileLocation, bigCardLocation):
        if self.drawPileActive:
            if self.currentCard == None:
                screen.blit(Deck.drawPileImage, (drawPileLocation))
                if self.discard != None:
                    screen.blit(self.discard, (discardPileLocation))
            else:
                screen.blit(self.currentCard.getCardImage(), (bigCardLocation))
