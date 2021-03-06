# this is starting the game
import mainTest

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
##pygame.font.init()


# Define additional button colors (beyond white, grey, black)
TRANSPARENT = (0, 0, 0, 0)
PURPLE = (255, 125, 255)
DARKPURPLE = (198, 0, 198)
GREEN = (50, 200, 20)
FORESTGREEN = (34,139,34)
DARKGREY = (127,127,127)


# setting user colors
yellow = 0
green = 90
red = 180
blue = 270

# create array to use for validation later on
behaviorChoices = ["mean","nice"]
intelligenceChoices = ["smart","dumb"]

# create dictionary that is used to orient board
colors= { "yellow": 0,
          "green": 90,
          "red": 180,
          "blue": 270
          }

#global validMoves and buttons list and activePawn - DO WE NEED TO FIX THIS?
activePawn = None
playState = 0

# this is the main function that will create a new game
def main(textObjects, numOfComps, userColor, username, mode):
    
    buttons = []
    validMoves = []

    # takes care of sliding a pawn when they land on an arrow on the board
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
        activePawn.tileName = currentTile
        
    # displays the squares that are valid moves for a pawn
    def displayValidMovesForPawn(validMoves, buttons, tileName):
        global playState
        global activePawn
        deactivateAllTileButtons(buttons)
        if (board.currentPlayer ==1 or mode ==2):
            for move in validMoves:
                pawn = move[0]
                if pawn.tileName == tileName:
                    for button in buttons:
                        if button.name == move[2]:
                            button.active = True
                            activePawn = pawn
                            break
            playState = 2
        else:
            activePawn = validMoves[0][0]
            movePawnToPosition(buttons,validMoves[0][2])
        return None

    # deactivate all tile buttons. (resets so you cant click or see them)
    def deactivateAllTileButtons(buttons):
        for button in buttons:
            if 0 < button.name < 89:
                button.active = False

    # displays pawns that can move
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
            if pawn.player == board.currentPlayer:
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
            
    # ends turn
    def endTurn(board, numPlayers):
        board.deck.discardCard()
        board.currentPlayer = board.currentPlayer%numPlayers + 1

    # moves pawn to the tileName that is specified
    def movePawnToPosition(buttons, tileName):
        global playState
        global activePawn
        deactivateAllTileButtons(buttons)
        activePawn.tileName = tileName
        for otherPawn in board.pawns:
            if otherPawn.player != board.currentPlayer:
                if otherPawn.tileName == tileName:
                    sorryPawn(board, otherPawn)
        if board.tiles[activePawn.tileName]['specialType'] == 'slide4':
            slide(board, activePawn, 4)
        elif board.tiles[activePawn.tileName]['specialType'] == 'slide5':
            slide(board, activePawn, 5)
        activePawn = None
        if board.deck.currentCard.value == '2':
            board.deck.discardCard()
        else:
            endTurn(board, numOfComps+1)
        playState = 0
        return None

    # is called when a player gets knocked off the board
    def sorryPawn(board, pawn):
        startNumbers = [61, 62, 63, 64]
        for num in startNumbers:
            if board.tiles[num]['side'] == pawn.player:
                newTile = num
        pawn.tileName = newTile

   
            
#################### END OF FUNCTIONS ###########################

    behaviorArray = []
    intelligenceArray = []
    newTxtObject = []    
    
    
    # validate computer setting input
    for txt in textObjects:
        txt = txt.getText()
        newTxtObject.append(txt.lower())

        
    # put behavior and intelligence settings into seperate arrays
    for i in range(0,len(newTxtObject)):
        if i % 2 == 0:
            
            behaviorArray.append(newTxtObject[i])

        else:
            
            intelligenceArray.append(newTxtObject[i])


    # validate behaviors the user set                                          
    for b in behaviorArray:
        if b not in behaviorChoices:
            if mode == 1:
                mode = "computer"
            elif mode == 2:
                mode = "player"
            mainMenu.newGame2(username, numOfComps, userColor, False, mode)

    # validate intelligence that user set
    for i in intelligenceArray:
        if i not in intelligenceChoices:

            mainMenu.newGame2(username, numOfComps, userColor, False)


            if mode == 1:
                mode = "computer"
            elif mode == 2:
                mode = "player"
            
            mainMenu.newGame2(username, numOfComps, userColor, False, mode)


    # when you get here I am assuming input is valid and a new game is being played so
    # I update gamesPlayed in tblStats by 1
    dbConnection.incrementGamesPlayed(dbConnection.connectDB(), username)
    

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
    for i in range(0,numOfComps):
        print(intelligenceArray[i])
        board.setComputer(i+2,intelligenceArray[i],behaviorArray[i])

    # Play state variable
    #1: choose valid pawn
    #2: choose valid move (new tile)
    #3: wait for discard

    # sets locations and names all buttons that go around board and adds to buttonsn array
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

    turnDone = Button("End Turn", (175, 575), endTurn, actionArgs=[board, numOfComps+1],
                    buttonColor=GREEN, buttonSize = (100,30), active=False)
    
    backButton = Button("Main Menu", (100,50), mainMenu.startPage, actionArgs=[username], buttonColor = FORESTGREEN, buttonSize=(200,30))

    instructionsButton = Button("Instructions", (100,100), mainMenu.instructions, actionArgs=[username], buttonSize=(200,30),buttonColor = DARKGREY)

    buttons.append(drawPile)
    buttons.append(turnDone)
    buttons.append(backButton)
    buttons.append(instructionsButton)

    # start loop to create the board
    while True:
        screen.fill((225, 225, 225))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.mouseButtonDown()
                    pygame.event.clear()
            else:
                pygame.event.clear()

        # Blit board and cards to screen
        board.displayBoard(screen,board)
        board.displayColor(screen, int(mode))


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
            


        board.displayInstructions(screen, validMoves, playState, int(mode))
        pygame.display.flip()
        clock.tick(60)


