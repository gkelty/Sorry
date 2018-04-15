import pygame
import sys
import os
from Card import Card, Deck
from Button import Button
import Image

pygame.init()

# Create screen and initialize clock
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

# Create deck, shuffle it, and print the order (top card listed last), and draw first card
deck = Deck()
shuffledDeck = deck.shuffle()
deck.showCards()
#currentCard = deck.drawCard()
#currentCard = None

# Define additional button colors (beyond white, grey, black)
GREEN = (50, 200, 20)

# Create button
drawPile = Button("Draw Card", (650, 270), deck.drawCard,
                    buttonColor=GREEN, buttonSize = (60,30))

discardCard = Button("Discard Card", (260, 150), deck.discardCard,
                    buttonColor=GREEN, buttonSize = (100,30))

# Put button in a list for simpler game loop
buttons = [drawPile, discardCard]

# Example game loop
while True:
    screen.fill((225, 225, 225))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                button.mouseButtonDown()

    # Blit board on screen
    screen.blit(Image.getImage('images\sorryGameBoardCombined.png'), (350, 20))

    # Blit buttons on screen
    for button in buttons:
        button.draw(screen)

    #Blit current card on screen
    if deck.currentCard != None:
        deck.displayCard(screen, (575, 200))
        drawPile.active = False
    else:
        drawPile.active = True

    pygame.display.flip()
    clock.tick(60)

