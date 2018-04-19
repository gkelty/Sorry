import pygame
import sys
import os
from Board import Board
from Card import Card, Deck
from Button import Button
from boardButton import BoardButton
import Image

pygame.init()

# Create screen and initialize clock
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

# Create new board and shuffled deck
board = Board(boardOrientation=0, boardLocation=(350, 0))

# Print the order of the shuffled deck (top card listed last) for testing purposes
board.deck.showCards()

# Define additional button colors (beyond white, grey, black)
TRANSPARENT = (0, 0, 0, 0)
GREEN = (50, 200, 20)

# Checks tile locations around the outside track
def moveForwardOne():
    tileName = board.pawns[0].tileName
    board.pawns[0].tileName = board.tiles[tileName]['tileAhead']
    return None

# Checks all tile locations in whole board (init only one player for this test)
# Uncomment the following and add the moveForwardAll button to buttons list:

board = Board(boardOrientation=0, playersEnabled=[True, False, False, False])

def moveForwardAll():
    tileName = board.pawns[0].tileName
    board.pawns[0].tileName = (tileName %88) +1
    return None
def movePawn():
    print("Moved")
    board.pawns[0].tileName = int(button.getBoardButton())
    return None
buttons = []
for i in range(1, 89):
    propLocX = board.tiles[i]['pos'][0]
    propLocY = board.tiles[i]['pos'][1]
    propLocX = propLocX + board.boardLocation[0]
    propLocY = propLocY + board.boardLocation[1]
    boardBut = BoardButton(i, propLocX, propLocY)
    boardButt = Button("Board", boardBut.getLocation(), movePawn, buttonColor=TRANSPARENT, buttonSize=(35, 35),boardButton=True,boardButtObj=boardBut)
    buttons.append(boardButt)
# Create buttons
drawPile = Button("Draw Card", (650, 250), board.deck.drawCard,
                    buttonColor=TRANSPARENT, backgroundColor=TRANSPARENT, buttonSize = (75,45))

discardCard = Button("Discard Card", (260, 150), board.deck.discardCard,
                    buttonColor=GREEN, buttonSize = (100,30))

moveForwardOne = Button("Move Forward", (260, 250), moveForwardOne,
                    buttonColor=GREEN, buttonSize = (100,30))

moveForwardAll = Button("MoveForward2", (260, 350), moveForwardAll,
                        buttonColor=GREEN, buttonSize=(100, 30))

# Put button in a list for simpler game loop
buttons.append(drawPile)
buttons.append(discardCard)
buttons.append(moveForwardOne)
buttons.append(moveForwardAll)

#for i in range(0,len(boardButtons)):
  #  buttons.append(boardButtons[i])
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

    # Blit board and cards to screen
    board.displayBoard(screen)

    # Blit buttons on screen
    for button in buttons:
        button.draw(screen)

    # Activate or deactivate drawPile
    if board.deck.currentCard != None:
        drawPile.active = False
    else:
        drawPile.active = True

    pygame.display.flip()
    clock.tick(60)

