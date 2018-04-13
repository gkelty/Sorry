import pygame
import sys
import os
from Card import Card, Deck
from Button import Button


pygame.init()

# Create screen and initialize clock
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

# Create deck, shuffle it, and print the order (top card listed last), and draw first card
deck = Deck()
shuffledDeck = deck.shuffle()
deck.showCards()
currentCard = deck.drawCard()

# Define additional button colors (beyond white, grey, black)
GREEN = (50, 200, 20)

# Create button
nextButton = Button("Show Next Card", (260, 150), deck.displayCard, actionArgs=[currentCard.value],
                    buttonColor=GREEN, buttonSize = (100,30))

# Put button in a list for simpler game loop
buttons = [nextButton]

# Example game loop
while True:
    screen.fill((225, 225, 225))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Button.mouseButtonDown(buttons)
            currentCard = deck.drawCard()

    # Blit board on screen
    screen.blit(deck.getImage('images\sorryGameBoardCombined.png'), (350, 20))

    # Blit buttons on screen
    for button in buttons:
        button.draw(screen)

    #Blid current card on screen
    screen.blit(deck.displayCard(currentCard.value), (575, 200))

    pygame.display.flip()
    clock.tick(60)

