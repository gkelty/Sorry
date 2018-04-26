import pygame
import random
import Image

pygame.font.init()
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

    possibleMoves = {'1': [{'moveSpaces': 1, 'moveFromStart': False, 'switchSpace': False, 'sorryCard': False, 'drawAgain': False},
                         {'moveSpaces': 0, 'moveFromStart': True, 'switchSpace': False, 'sorryCard': False, 'drawAgain': False}],
                     '2': [{'moveSpaces': 2, 'moveFromStart': False, 'switchSpace': False, 'sorryCard': False, 'drawAgain': True},
                         {'moveSpaces': 0, 'moveFromStart': True, 'switchSpace': False, 'sorryCard': False, 'drawAgain': True}],
                     '3': [{'moveSpaces': 3, 'moveFromStart': False, 'switchSpace': False, 'sorryCard': False, 'drawAgain': False}],
                     '4': [{'moveSpaces': -4, 'moveFromStart': False, 'switchSpace': False, 'sorryCard': False, 'drawAgain': False}],
                     '5': [{'moveSpaces': 5, 'moveFromStart': False, 'switchSpace': False, 'sorryCard': False, 'drawAgain': False}],
                     '7': [{'moveSpaces': 7, 'moveFromStart': False, 'switchSpace': False, 'sorryCard': False, 'drawAgain': False}],
                                # Need to implement split move condition
                     '8': [{'moveSpaces': 8, 'moveFromStart': False, 'switchSpace': False, 'sorryCard': False, 'drawAgain': False}],
                     '10': [{'moveSpaces': 10, 'moveFromStart': False, 'switchSpace': False, 'sorryCard': False, 'drawAgain': False},
                         {'moveSpaces': -1, 'moveFromStart': False, 'switchSpace': False, 'sorryCard': False, 'drawAgain': False}],
                     '11': [{'moveSpaces': 11, 'moveFromStart': False, 'switchSpace': False, 'sorryCard': False, 'drawAgain': False},
                          {'moveSpaces': 0, 'moveFromStart': False, 'switchSpace': True, 'sorryCard': False, 'drawAgain': False}],
                     '12': [{'moveSpaces': 12, 'moveFromStart': False, 'switchSpace': False, 'sorryCard': False, 'drawAgain': False}],
                     'S': [{'moveSpaces': 0, 'moveFromStart': False, 'switchSpace': False, 'sorryCard': True, 'drawAgain': False}]}

    def __init__(self, value):
        self.value = value
        self.possibleMoves = Card.possibleMoves[value]
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
        self.discards = []
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
        self.discards.append(self.currentCard)
        if len(self.cards) == 0:
            self.shuffleDiscards()
            self.drawCard()
        return self.drawPileActive
    def shuffleDiscards(self):
        print(self.discards)
        random.shuffle(self.discards)
        self.cards = self.discards

    def discardCard(self):
        if self.currentCard != None:
            self.discard = pygame.transform.rotozoom(self.currentCard.getCardImage(), 90, 0.3)
        self.currentCard = None

    def displayDeck(self, screen, board, drawPileLocation, discardPileLocation, bigCardLocation):
        if self.drawPileActive:
            if self.currentCard == None:
                screen.blit(Deck.drawPileImage, (drawPileLocation))
                if self.discard != None:
                    screen.blit(self.discard, (discardPileLocation))
            else:
                screen.blit(self.currentCard.getCardImage(), (bigCardLocation))