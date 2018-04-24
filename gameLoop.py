from Button import Button
from TextInputBox import TextInputBox
from dbConnection import dbConnection
from Board import Board
from boardButton import BoardButton
import mainMenu
import PossibleMoves
import pygame
import pygame.locals as pl
import sys
import os.path
pygame.init()
pygame.font.init()



# Define additional button colors (beyond white, grey, black)
TRANSPARENT = (0, 0, 0, 0)
PURPLE = (255, 125, 255)
DARKPURPLE = (198, 0, 198)
GREEN = (50, 200, 20)

# setting user colors
yellow = 0
green = 90
red = 180
blue = 270
 
behaviorChoices = ["mean","nice"]
intelligenceChoices = ["smart","dumb"]

colors= { "yellow": 0,
          "green": 90,
          "red": 180,
          "blue": 270
          }



#global validMoves and buttons list and activePawn - DO WE NEED TO FIX THIS?
validMoves = []
activePawn = None
playState = 0

def main(textObjects, numOfComps, userColor, username):
    
    buttons = []

    def slide(board, pawn, lengthOfSlide):
        currentTile = pawn.tileName
        for i in range(lengthOfSlide-1):
            newTile = board.tiles[currentTile]['tileAhead']
            print("new tile", newTile)
            for otherPawn in board.pawns:
                print("other pawn", otherPawn.tileName)
                if otherPawn.tileName == newTile:
                    if otherPawn.player == board.currentPlayer:
                        sorryPawn(board, otherPawn)
                    elif otherPawn.player != board.currentPlayer:
                        sorryPawn(board, otherPawn)
            currentTile = newTile
        deactivateAllTileButtons(buttons)
        activePawn.tileName = currentTile
    
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

    def deactivateAllTileButtons(buttons):
##        print("deactivate")
        for button in buttons:
            if 0 < button.name < 89:
                button.active = False

    def displayPawnsWithValidMoves(validMoves, buttons):
        global playState
        deactivateAllTileButtons(buttons)
        for move in validMoves:
            pawn = move[0]
            currentPosition = pawn.tileName
            for button in buttons:
                if button.name == currentPosition:
                    button.active = True
                    break
        playState = 1
        return None

    # Button handler
    def tileButtonHandler(tileName):
        if playState == 1:
            #send to function that does logic for displaying moves
            displayValidMovesForPawn(validMoves, buttons, tileName)
        elif playState == 2:
            #send to function that moves pawn to new space (including handling slides), discard card, increment player, next player's turn
            movePawnToPosition(buttons, tileName)
    def endTurn(board):
        board.deck.discardCard()
        board.currentPlayer = board.currentPlayer%4 + 1

    
    def movePawnToPosition(buttons, tileName):
        global playState
        global activePawn
        deactivateAllTileButtons(buttons)
        activePawn.tileName = tileName
        for otherPawn in board.pawns:
            if otherPawn.player != board.currentPlayer:
##                print("other pawn", otherPawn.tileName)
                if otherPawn.tileName == tileName:
                    sorryPawn(board, otherPawn)
##        print(board.tiles[activePawn.tileName]['specialType'])
        if board.tiles[activePawn.tileName]['specialType'] == 'slide4':
            slide(board, activePawn, 4)
        elif board.tiles[activePawn.tileName]['specialType'] == 'slide5':
            slide(board, activePawn, 5)
        activePawn = None
##        print(board.deck.currentCard.value)
        if board.deck.currentCard.value == '2':
            board.deck.discardCard()
        else:
            endTurn(board)
        playState = 0
        return None

   
            
#################### END OF FUNCTIONS ###########################

    behaviorArray = []
    intelligenceArray = []
    newTxtObject = []
    
    # validate computer setting input
    for txt in textObjects:
        txt = txt.getText()
        newTxtObject.append(txt)

    #print(newTxtObject)

    for i in range(0,len(newTxtObject)):
        if i % 2 == 0:
            
            behaviorArray.append(newTxtObject[i])

        else:
            
            intelligenceArray.append(newTxtObject[i])
        
##    print(behaviorArray)
##    print(intelligenceArray)
                        
                    
    for b in behaviorArray:
##        print(b)
        if b not in behaviorChoices:
            mainMenu.newGame2(username, numOfComps, userColor)
            
    for i in intelligenceArray:
##        print(i)
        if i not in intelligenceChoices:
            mainMenu.newGame2(username, numOfComps, userColor)
        

    
    # Create screen and initialize clock
    screen = pygame.display.set_mode((1000, 600))
    clock = pygame.time.Clock()


    # Create new board and shuffled deck
    if numOfComps == 3:
        for c in colors:
            color =  colors[userColor]
            board = Board(boardOrientation=color, boardLocation=(350, 0))

    if numOfComps == 2:
        for c in colors:
            color =  colors[userColor]
            board = Board(boardOrientation=color, boardLocation=(350, 0), playersEnabled=[True, True, True, False] )
    if numOfComps == 1:
        for c in colors:
            color =  colors[userColor]
            board = Board(boardOrientation=color, boardLocation=(350, 0), playersEnabled=[True, True, False, False] )

    # Print the order of the shuffled deck (top card listed last) for testing purposes
    board.deck.showCards()


    # Play state variable
    #1: choose valid pawn
    #2: choose valid move (new tile)
    #3: wait for discard
    
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

    turnDone = Button("End Turn", (260, 150), endTurn, actionArgs=[board],
                    buttonColor=GREEN, buttonSize = (100,30), active=False)

    buttons.append(drawPile)
    buttons.append(turnDone)

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

        # Blit pawns on screen
        board.displayPawns(screen)

        # Activate or deactivate drawPile
        if board.deck.currentCard != None:
            drawPile.active = False
            if playState == 0:
                validMoves = PossibleMoves.getValidPossibleMoves(board, board.currentPlayer)
                if validMoves != []:
                    displayPawnsWithValidMoves(validMoves, buttons)
                else:
                    turnDone.active = True
            elif playState == 1 or playState == 2:
                turnDone.active = False

        else:
            drawPile.active = True
            turnDone.active = False

        pygame.display.flip()
        clock.tick(60)


