import pygame
import sys
import os
from Board import Board
from Card import Card, Deck
from Button import Button
from boardButton import BoardButton
import PossibleMoves
import Image

pygame.init()

# Create screen and initialize clock
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

# Create new board and shuffled deck
board = Board(boardOrientation=0, boardLocation=(350, 0))
mean = [True, False, True]                                      ###WILL NEED TO PASS IN FROM GAME INIT
smart = [True, True, False]
playMode = 1                                                        ### mode 1: play against computer, mode 2: play with friends

# Print the order of the shuffled deck (top card listed last) for testing purposes
board.deck.showCards()

# Define additional button colors (beyond white, grey, black)
TRANSPARENT = (0, 0, 0, 0)
PURPLE = (255, 125, 255)
DARKPURPLE = (198, 0, 198)
GREEN = (50, 200, 20)

# Play state variable
#1: choose valid pawn
#2: choose valid move (new tile)
#3: wait for discard
playState = 0

#global validMoves and buttons list and activePawn - DO WE NEED TO FIX THIS?
validMoves = []
activePawn = None


# Button handler
def tileButtonHandler(tileName):
    if playState == 1:
        #send to function that does logic for displaying moves
        displayValidMovesForPawn(validMoves, buttons, tileName)
    elif playState == 2:
        #send to function that moves pawn to new space (including handling slides), discard card, increment player, next player's turn
        movePawnToPosition(activePawn, tileName)


def deactivateAllTileButtons(buttons):
#    print("deactivate")
    for button in buttons:
        if 0 < button.name < 89:
            button.active = False

def displayPawnsWithValidMoves(validMoves, buttons):
    global playState
    deactivateAllTileButtons(buttons)
    print("player: ", board.currentPlayer)
    print(validMoves)
    for move in validMoves:
        pawn = move[0]
        if pawn.player == board.currentPlayer:
            currentPosition = pawn.tileName
            for button in buttons:
                if button.name == currentPosition:
                    button.active = True
                    break
    playState = 1
    return None

def displayValidMovesForPawn(validMoves, buttons, tileName):
    global playState
    global activePawn
    deactivateAllTileButtons(buttons)
    for move in validMoves:
        pawn = move[0]
        if pawn.tileName == tileName:
            for button in buttons:
                if button.name == move[2]:
                    button.active = True
                    activePawn = pawn
                    break
    playState = 2
    return None

def movePawnToPosition(pawn, tileName):
    global playState
    global activePawn
    if board.currentPlayer == 1:
        pawn = activePawn
    deactivateAllTileButtons(buttons)
    oldTile = pawn.tileName
    pawn.tileName = tileName
    for otherPawn in board.pawns:
        if otherPawn.player != board.currentPlayer:
            if otherPawn.tileName == tileName:
                if board.deck.currentCard.value == '11':
                    otherPawn.tileName = oldTile
                else:
                    sorryPawn(board, otherPawn)
    if board.tiles[pawn.tileName]['side'] != board.currentPlayer:
        if board.tiles[pawn.tileName]['specialType'] == 'slide4':
            slide(board, pawn, 4)
        elif board.tiles[pawn.tileName]['specialType'] == 'slide5':
            slide(board, pawn, 5)
    activePawn = None
    if board.deck.currentCard.value == '2':
        board.deck.discardCard()
    else:
        endTurn()
    playState = 0
    return None

def slide(board, pawn, lengthOfSlide):
    currentTile = pawn.tileName
    for i in range(lengthOfSlide-1):
        newTile = board.tiles[currentTile]['tileAhead']
        for otherPawn in board.pawns:
            if otherPawn.tileName == newTile:
                if otherPawn.player == board.currentPlayer:
                    sorryPawn(board, otherPawn)
                elif otherPawn.player != board.currentPlayer:
                    sorryPawn(board, otherPawn)
        currentTile = newTile
    deactivateAllTileButtons(buttons)
    pawn.tileName = currentTile

def sorryPawn(board, pawn):
    startNumbers = [61, 62, 63, 64]
    for num in startNumbers:
        if board.tiles[num]['side'] == pawn.player:
            newTile = num
    pawn.tileName = newTile

def endTurn():
#    print("end turn")
    board.deck.discardCard()
    board.currentPlayer = board.currentPlayer%4 + 1 ###THIS SHOULD BE NUMBER OF PLAYERS

def playerTurn():
        if playState == 0:
            validMoves = PossibleMoves.getValidPossibleMoves(board, board.currentPlayer, mean)
            board.displayInstructions(screen, validMoves, playState, playMode)

            if validMoves != []:
                displayPawnsWithValidMoves(validMoves, buttons)
            else:
                turnDone.active = True
        elif playState == 1 or playState == 2:
            turnDone.active = False

def computerTurn():
    board.deck.drawCard()
    board.displayCards(screen, board)
    validMoves = PossibleMoves.getValidPossibleMoves(board, board.currentPlayer, mean)
    board.displayInstructions(screen, validMoves, playState, playMode)
#    pygame.time.wait(1000)

    if validMoves != []:
        pawnToMove = board.computerMove(validMoves, smart[board.currentPlayer-2])[0]
        bestMove = board.computerMove(validMoves, smart[board.currentPlayer-2])[1]
        print(pawnToMove.tileName, "----", bestMove)
        movePawnToPosition(pawnToMove, validMoves[bestMove-1][2])
        board.displayInstructions(screen, validMoves, playState, playMode)
    else:
        endTurn()


####### from here down, make main loop ###########
buttons = []
for i in range(1, 89):
    propLocX = board.tiles[i]['pos'][0]
    propLocY = board.tiles[i]['pos'][1]
    propLocX = propLocX + board.boardLocation[0]
    propLocY = propLocY + board.boardLocation[1]
    boardBut = BoardButton(i, propLocX, propLocY)
    boardButt = Button("", boardBut.getLocation(), tileButtonHandler, actionArgs=[i], name=i, buttonColor=PURPLE, backgroundColor=DARKPURPLE,
                       buttonSize=(35, 35), active=False, boardButton=True, boardButtObj=boardBut)
    buttons.append(boardButt)

# Create buttons
drawPile = Button("Draw Card", (650, 250), board.deck.drawCard,
                    buttonColor=TRANSPARENT, backgroundColor=TRANSPARENT, buttonSize = (75,45))

turnDone = Button("End Turn", (175, 575), endTurn,
                    buttonColor=GREEN, buttonSize = (100,30), active=False)

#moveForwardOne = Button("Move Forward", (260, 250), moveForwardOne,
#                    buttonColor=GREEN, buttonSize = (100,30))

#moveForwardAll = Button("MoveForward2", (260, 350), moveForwardAll,
#                        buttonColor=GREEN, buttonSize=(100, 30))

# Put button in a list for simpler game loop
buttons.append(drawPile)
buttons.append(turnDone)
#buttons.append(moveForwardOne)
#buttons.append(moveForwardAll)

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
        else:
            None

    # Blit board and cards to screen
    board.displayBoard(screen)
    board.displayCards(screen, board)

    board.displayColor(screen)
    board.displayInstructions(screen, validMoves, playState, playMode)


    # Blit buttons on screen
    for button in buttons:
        button.draw(screen)

    # Blit pawns on screen
    board.displayPawns(screen)

#########################MODE 1 = see old git for mode 2 and add it in##############################
    if board.currentPlayer == 1:
        # Activate or deactivate drawPile
        if board.deck.currentCard != None:
            drawPile.active = False
            playerTurn()
        else:
            drawPile.active = True
            turnDone.active = False

    else:
        turnDone.active = False
        pygame.time.wait(500)
        computerTurn()

#For mode 1:
    if board.currentPlayer != 1:
            pygame.time.wait(1000)
    else:
        if board.deck.currentCard == None:
            pygame.time.wait(1000)

    pygame.display.flip()
    clock.tick(60)

