import pygame
from Pawn import Pawn
from Card import Card, Deck
from boardButton import BoardButton
import Image

class Board:
    boardImage = Image.getImage('images\sorryGameBoardNoCenter.png')
    boardCenterImage = Image.getImage('images\sorryGameBoardCenterOnly.png')
    bigCardOffset = (225, 180)
    drawPileOffset = (262, 225)
    discardPileOffset = (262,330)
    pawnTileOffset = (-17, -22)
    pawnStartHomeOffsets = [(-35, -40), (-35, -5), (0, -40), (0, -5)]
    startLocations = [61, 62, 63, 64]
    homeLocations = [70, 76, 82, 88]

    # tiles attributes in dictionary below (access tile attribute as follows (e.g., tiles[1]['type'])
        # side: 1=bottom, 2=left, 3=top, 4=right
        # specialType: None (no special type), start, home, safety, slide, startTile
        # pos: center pixel location of tile (relative to the board - need to offset position by board offset)
        # tileAhead: key of next tile
        # tileBehind: key of previous tile
        # tileRight: key of tile to the right
    tiles = {1: {'side': 1, 'specialType': 'startTile', 'pos': (422, 562), 'tileAhead': 2, 'tileBehind': 60, 'tileRight': None},
           2: {'side': 1, 'specialType': None, 'pos': (387, 562), 'tileAhead': 3, 'tileBehind': 1, 'tileRight': None},
           3: {'side': 1, 'specialType': None, 'pos': (352, 562), 'tileAhead': 4, 'tileBehind': 2, 'tileRight': None},
           4: {'side': 1, 'specialType': None, 'pos': (317, 562), 'tileAhead': 5, 'tileBehind': 3, 'tileRight': None},
           5: {'side': 1, 'specialType': None, 'pos': (282, 562), 'tileAhead': 6, 'tileBehind': 4, 'tileRight': None},
           6: {'side': 1, 'specialType': 'slide5', 'pos': (247, 562), 'tileAhead': 7, 'tileBehind': 5, 'tileRight': None},
           7: {'side': 1, 'specialType': None, 'pos': (212, 562), 'tileAhead': 8, 'tileBehind': 6, 'tileRight': None},
           8: {'side': 1, 'specialType': None, 'pos': (177, 562), 'tileAhead': 9, 'tileBehind': 7, 'tileRight': None},
           9: {'side': 1, 'specialType': None, 'pos': (142, 562), 'tileAhead': 10, 'tileBehind': 8, 'tileRight': None},
           10: {'side': 1, 'specialType': None, 'pos': (107, 562), 'tileAhead': 11, 'tileBehind': 9, 'tileRight': None},
           11: {'side': 1, 'specialType': None, 'pos': (72, 562), 'tileAhead': 12, 'tileBehind': 10, 'tileRight': None},
           12: {'side': 2, 'specialType': None, 'pos': (37, 562), 'tileAhead': 13, 'tileBehind': 11, 'tileRight': None},
           13: {'side': 2, 'specialType': 'slide4', 'pos': (37, 527), 'tileAhead': 14, 'tileBehind': 12, 'tileRight': None},
           14: {'side': 2, 'specialType': None, 'pos': (37, 492), 'tileAhead': 15, 'tileBehind': 13, 'tileRight': 65},
           15: {'side': 2, 'specialType': None, 'pos': (37, 457), 'tileAhead': 16, 'tileBehind': 14, 'tileRight': None},
           16: {'side': 2, 'specialType': 'startTile', 'pos': (37, 422), 'tileAhead': 17, 'tileBehind': 15, 'tileRight': None},
           17: {'side': 2, 'specialType': None, 'pos': (37, 387), 'tileAhead': 18, 'tileBehind': 16, 'tileRight': None},
           18: {'side': 2, 'specialType': None, 'pos': (37, 352), 'tileAhead': 19, 'tileBehind': 17, 'tileRight': None},
           19: {'side': 2, 'specialType': None, 'pos': (37, 317), 'tileAhead': 20, 'tileBehind': 18, 'tileRight': None},
           20: {'side': 2, 'specialType': None, 'pos': (37, 282), 'tileAhead': 21, 'tileBehind': 19, 'tileRight': None},
           21: {'side': 2, 'specialType': 'slide5', 'pos': (37, 247), 'tileAhead': 22, 'tileBehind': 20, 'tileRight': None},
           22: {'side': 2, 'specialType': None, 'pos': (37, 212), 'tileAhead': 23, 'tileBehind': 21, 'tileRight': None},
           23: {'side': 2, 'specialType': None, 'pos': (37, 177), 'tileAhead': 24, 'tileBehind': 22, 'tileRight': None},
           24: {'side': 2, 'specialType': None, 'pos': (37, 142), 'tileAhead': 25, 'tileBehind': 23, 'tileRight': None},
           25: {'side': 2, 'specialType': None, 'pos': (37, 107), 'tileAhead': 26, 'tileBehind': 24, 'tileRight': None},
           26: {'side': 2, 'specialType': None, 'pos': (37, 72), 'tileAhead': 27, 'tileBehind': 25, 'tileRight': None},
           27: {'side': 3, 'specialType': None, 'pos': (37, 37), 'tileAhead': 28, 'tileBehind': 26, 'tileRight': None},
           28: {'side': 3, 'specialType': 'slide4', 'pos': (72, 37), 'tileAhead': 29, 'tileBehind': 27, 'tileRight': None},
           29: {'side': 3, 'specialType': None, 'pos': (107, 37), 'tileAhead': 30, 'tileBehind': 28, 'tileRight': 71},
           30: {'side': 3, 'specialType': None, 'pos': (142, 37), 'tileAhead': 31, 'tileBehind': 29, 'tileRight': None},
           31: {'side': 3, 'specialType': 'startTile', 'pos': (177, 37), 'tileAhead': 32, 'tileBehind': 30, 'tileRight': None},
           32: {'side': 3, 'specialType': None, 'pos': (212, 37), 'tileAhead': 33, 'tileBehind': 31, 'tileRight': None},
           33: {'side': 3, 'specialType': None, 'pos': (247, 37), 'tileAhead': 34, 'tileBehind': 32, 'tileRight': None},
           34: {'side': 3, 'specialType': None, 'pos': (282, 37), 'tileAhead': 35, 'tileBehind': 33, 'tileRight': None},
           35: {'side': 3, 'specialType': None, 'pos': (317, 37), 'tileAhead': 36, 'tileBehind': 34, 'tileRight': None},
           36: {'side': 3, 'specialType': 'slide5', 'pos': (352, 37), 'tileAhead': 37, 'tileBehind': 35, 'tileRight': None},
           37: {'side': 3, 'specialType': None, 'pos': (387, 37), 'tileAhead': 38, 'tileBehind': 36, 'tileRight': None},
           38: {'side': 3, 'specialType': None, 'pos': (422, 37), 'tileAhead': 39, 'tileBehind': 37, 'tileRight': None},
           39: {'side': 3, 'specialType': None, 'pos': (457, 37), 'tileAhead': 40, 'tileBehind': 38, 'tileRight': None},
           40: {'side': 3, 'specialType': None, 'pos': (492, 37), 'tileAhead': 41, 'tileBehind': 39, 'tileRight': None},
           41: {'side': 3, 'specialType': None, 'pos': (527, 37), 'tileAhead': 42, 'tileBehind': 40, 'tileRight': None},
           42: {'side': 4, 'specialType': None, 'pos': (562, 37), 'tileAhead': 43, 'tileBehind': 41, 'tileRight': None},
           43: {'side': 4, 'specialType': 'slide4', 'pos': (562, 72), 'tileAhead': 44, 'tileBehind': 42, 'tileRight': None},
           44: {'side': 4, 'specialType': None, 'pos': (562, 107), 'tileAhead': 45, 'tileBehind': 43, 'tileRight': 77},
           45: {'side': 4, 'specialType': None, 'pos': (562, 142), 'tileAhead': 46, 'tileBehind': 44, 'tileRight': None},
           46: {'side': 4, 'specialType': 'startTile', 'pos': (562, 177), 'tileAhead': 47, 'tileBehind': 45, 'tileRight': None},
           47: {'side': 4, 'specialType': None, 'pos': (562, 212), 'tileAhead': 48, 'tileBehind': 46, 'tileRight': None},
           48: {'side': 4, 'specialType': None, 'pos': (562, 247), 'tileAhead': 49, 'tileBehind': 47, 'tileRight': None},
           49: {'side': 4, 'specialType': None, 'pos': (562, 282), 'tileAhead': 50, 'tileBehind': 48, 'tileRight': None},
           50: {'side': 4, 'specialType': None, 'pos': (562, 317), 'tileAhead': 51, 'tileBehind': 49, 'tileRight': None},
           51: {'side': 4, 'specialType': 'slide5', 'pos': (562, 352), 'tileAhead': 52, 'tileBehind': 50, 'tileRight': None},
           52: {'side': 4, 'specialType': None, 'pos': (562, 387), 'tileAhead': 53, 'tileBehind': 51, 'tileRight': None},
           53: {'side': 4, 'specialType': None, 'pos': (562, 422), 'tileAhead': 54, 'tileBehind': 52, 'tileRight': None},
           54: {'side': 4, 'specialType': None, 'pos': (562, 457), 'tileAhead': 55, 'tileBehind': 53, 'tileRight': None},
           55: {'side': 4, 'specialType': None, 'pos': (562, 492), 'tileAhead': 56, 'tileBehind': 54, 'tileRight': None},
           56: {'side': 4, 'specialType': None, 'pos': (562, 527), 'tileAhead': 57, 'tileBehind': 55, 'tileRight': None},
           57: {'side': 1, 'specialType': None, 'pos': (562, 562), 'tileAhead': 58, 'tileBehind': 56, 'tileRight': None},
           58: {'side': 1, 'specialType': 'slide4', 'pos': (527, 562), 'tileAhead': 59, 'tileBehind': 57, 'tileRight': None},
           59: {'side': 1, 'specialType': None, 'pos': (492, 562), 'tileAhead': 60, 'tileBehind': 58, 'tileRight': 83},
           60: {'side': 1, 'specialType': None, 'pos': (457, 562), 'tileAhead': 1, 'tileBehind': 59, 'tileRight': None},
           61: {'side': 1, 'specialType': 'start', 'pos': (422, 505), 'tileAhead': 1, 'tileBehind': None, 'tileRight': None},
           62: {'side': 2, 'specialType': 'start', 'pos': (94, 422), 'tileAhead': 16, 'tileBehind': None, 'tileRight': None},
           63: {'side': 3, 'specialType': 'start', 'pos': (177, 94), 'tileAhead': 31, 'tileBehind': None, 'tileRight': None},
           64: {'side': 4, 'specialType': 'start', 'pos': (505, 177), 'tileAhead': 46, 'tileBehind': None, 'tileRight': None},
           65: {'side': 2, 'specialType': 'safety', 'pos': (72, 492), 'tileAhead': 66, 'tileBehind': 14, 'tileRight': None},
           66: {'side': 2, 'specialType': 'safety', 'pos': (107, 492), 'tileAhead': 67, 'tileBehind': 65, 'tileRight': None},
           67: {'side': 2, 'specialType': 'safety', 'pos': (142, 492), 'tileAhead': 68, 'tileBehind': 66, 'tileRight': None},
           68: {'side': 2, 'specialType': 'safety', 'pos': (177, 492), 'tileAhead': 69, 'tileBehind': 67, 'tileRight': None},
           69: {'side': 2, 'specialType': 'safety', 'pos': (212, 492), 'tileAhead': 70, 'tileBehind': 68, 'tileRight': None},
           70: {'side': 2, 'specialType': 'home', 'pos': (270, 492), 'tileAhead': None, 'tileBehind': None, 'tileRight': None},
           71: {'side': 3, 'specialType': 'safety', 'pos': (107, 72), 'tileAhead': 72, 'tileBehind': 29, 'tileRight': None},
           72: {'side': 3, 'specialType': 'safety', 'pos': (107, 107), 'tileAhead': 73, 'tileBehind': 71, 'tileRight': None},
           73: {'side': 3, 'specialType': 'safety', 'pos': (107, 142), 'tileAhead': 74, 'tileBehind': 72, 'tileRight': None},
           74: {'side': 3, 'specialType': 'safety', 'pos': (107, 177), 'tileAhead': 75, 'tileBehind': 73, 'tileRight': None},
           75: {'side': 3, 'specialType': 'safety', 'pos': (107, 212), 'tileAhead': 76, 'tileBehind': 74, 'tileRight': None},
           76: {'side': 3, 'specialType': 'home', 'pos': (108, 270), 'tileAhead': None, 'tileBehind': None, 'tileRight': None},
           77: {'side': 4, 'specialType': 'safety', 'pos': (527, 107), 'tileAhead': 78, 'tileBehind': 44, 'tileRight': None},
           78: {'side': 4, 'specialType': 'safety', 'pos': (492, 107), 'tileAhead': 79, 'tileBehind': 77, 'tileRight': None},
           79: {'side': 4, 'specialType': 'safety', 'pos': (457, 107), 'tileAhead': 80, 'tileBehind': 78, 'tileRight': None},
           80: {'side': 4, 'specialType': 'safety', 'pos': (422, 107), 'tileAhead': 81, 'tileBehind': 79, 'tileRight': None},
           81: {'side': 4, 'specialType': 'safety', 'pos': (387, 107), 'tileAhead': 82, 'tileBehind': 80, 'tileRight': None},
           82: {'side': 4, 'specialType': 'home', 'pos': (331, 107), 'tileAhead': None, 'tileBehind': None, 'tileRight': None},
           83: {'side': 1, 'specialType': 'safety', 'pos': (492, 527), 'tileAhead': 84, 'tileBehind': 59, 'tileRight': None},
           84: {'side': 1, 'specialType': 'safety', 'pos': (492, 492), 'tileAhead': 85, 'tileBehind': 83, 'tileRight': None},
           85: {'side': 1, 'specialType': 'safety', 'pos': (492, 457), 'tileAhead': 86, 'tileBehind': 84, 'tileRight': None},
           86: {'side': 1, 'specialType': 'safety', 'pos': (492, 422), 'tileAhead': 87, 'tileBehind': 85, 'tileRight': None},
           87: {'side': 1, 'specialType': 'safety', 'pos': (492, 387), 'tileAhead': 88, 'tileBehind': 86, 'tileRight': None},
           88: {'side': 1, 'specialType': 'home', 'pos': (493, 331), 'tileAhead': None, 'tileBehind': None, 'tileRight': None}}

    def __init__(self, boardOrientation, boardLocation=(350, 0), playersEnabled=[True, True, True, True]):
        self.orientation = boardOrientation # degrees of orientation off of yellow on bottom
                                            # (if player is yellow: 0 green: 90 red: 180 blue: 270)
        self.image = pygame.transform.rotate(Board.boardImage, self.orientation)
        self.boardLocation = boardLocation # top left of image, not center like with buttons and pawns
        self.drawPileLocation = (boardLocation[0] + Board.drawPileOffset[0],  boardLocation[1] + Board.drawPileOffset[1])
        self.discardPileLocation = (boardLocation[0] + Board.discardPileOffset[0],  boardLocation[1] + Board.discardPileOffset[1])
        self.bigCardLocation = (boardLocation[0] + Board.bigCardOffset[0],  boardLocation[1] + Board.bigCardOffset[1])
        self.pawns = []
        self.players = playersEnabled
        self.currentPlayer = 1
        id = 0
        indexOffset = int(self.orientation / 90)
        for i in range(4):
            index = (i + indexOffset) % 4
            if playersEnabled[i]:
                for j in range(4):
                    id += 1
                    self.pawns.append(Pawn(id, Pawn.colors[index], i+1, Board.startLocations[i]))
                                            #only rotate init colors to match board rotation, not startLocations
        #self.currentPositions = []
        self.deck = Deck()
        self.deck.shuffle() 
        # self.boardButtons = []
        # for i in range(1,89):
        #     propLocX = self.tiles[i]['pos'][0]
        #     propLocY = self.tiles[i]['pos'][1]
        #     propLocX = propLocX+self.boardLocation[0]
        #     propLocY = propLocY+self.boardLocation[1]
        #     boardBut = BoardButton(i,propLocX,propLocY)
        #     self.boardButtons.append(boardBut.createBoard())

    def getPlayerColor(self):
        for pawn in self.pawns:
            if pawn.player == self.currentPlayer:
                return pawn.color

    def checkInStart(self, pawn):
        inStart = False
        if Board.tiles[pawn.tileName]['specialType'] == 'start':
            inStart = True
        return inStart

    def checkOnStartTile(self, pawn):
        onStartTile = False
        if Board.tiles[pawn.tileName]['specialType'] == 'startTile':
            onStartTile = True
        return onStartTile

    #This is only the outer track
    def checkOnBoard(self, pawn):
        onBoard = False
        if Board.tiles[pawn.tileName]['specialType'] == None or Board.tiles[pawn.tileName]['specialType'] == 'startTile' \
                or Board.tiles[pawn.tileName]['specialType'] == 'slide4' or Board.tiles[pawn.tileName]['specialType'] == 'slide5':
            onBoard = True
        return onBoard

    def checkInSafety(self, pawn):
        inSafety = False
        if Board.tiles[pawn.tileName]['specialType'] == 'safety':
            inSafety = True
        return inSafety

    def checkInHome(self, pawn):
        inHome = False
        if Board.tiles[pawn.tileName]['specialType'] == 'home':
            inHome = True
        return inHome

    def getTargetTile(self, pawn, numberOfSpaces):
        assert numberOfSpaces != 0
        currentTile = pawn.tileName
        newTile = None
        direction = 1
        if numberOfSpaces < 0:
            value = abs(numberOfSpaces)
            direction = -1
        else:
            value = numberOfSpaces
        if self.checkOnBoard(pawn) or self.checkInSafety(pawn):
            for i in range(value):
                if direction == -1:
                    newTile = Board.tiles[currentTile]['tileBehind']
                elif Board.tiles[currentTile]['side'] != pawn.player:
                    newTile = Board.tiles[currentTile]['tileAhead']
                elif Board.tiles[currentTile]['tileRight'] == None:
                    newTile = Board.tiles[currentTile]['tileAhead']
                else:
                    newTile = Board.tiles[currentTile]['tileRight']
                if newTile == None:
                    break
                else:
                    currentTile = newTile
        return newTile


    #def returnBoard(self):
       # return(self.boardButtons)

    def displayBoard(self, screen, board):
        screen.blit(self.image, self.boardLocation)
        screen.blit(Board.boardCenterImage, self.boardLocation)

        #Blit current card on screen
        self.deck.displayDeck(screen, board, self.drawPileLocation, self.discardPileLocation, self.bigCardLocation)

    def displayPawns(self, screen):
        #Blit pawns on screen
        pawnsStartHome = {}
        for pawn in self.pawns:
            locationX = (self.boardLocation[0] + Board.tiles[pawn.tileName]['pos'][0])
            locationY = (self.boardLocation[1] + Board.tiles[pawn.tileName]['pos'][1])
            if Board.tiles[pawn.tileName]['specialType'] == 'start' or Board.tiles[pawn.tileName]['specialType'] == 'home':
                if not pawn.tileName in pawnsStartHome:
                    pawnsStartHome[pawn.tileName] = 0
                pawn.displayPawn(screen, ((locationX + Board.pawnStartHomeOffsets[pawnsStartHome[pawn.tileName]][0]),
                                          (locationY + Board.pawnStartHomeOffsets[pawnsStartHome[pawn.tileName]][1])))
                pawnsStartHome[pawn.tileName] += 1
            else:
                pawn.displayPawn(screen, (locationX + Board.pawnTileOffset[0], locationY + Board.pawnTileOffset[1]))

    def displayColor(self, screen):
        myfont = pygame.font.SysFont('freesans.ttf', 30)
        mode = 1  # mode 1: play against computer, mode 2: play with friends -- pass this value in to this function
        if mode == 1:
            if self.currentPlayer == 1:
                turnMessage = "It's your turn!"
            else:
                turnMessage = "It's " + self.getPlayerColor() + "'s turn"
        if mode == 2:
            turnMessage = "It's " + self.getPlayerColor() + "'s turn"
        textsurface = myfont.render(turnMessage, False, (0, 0, 0))
        screen.blit(textsurface, (100, 300))

    def getInstructions(self, validMoves, playState):
        mode = 1        # mode 1: play against computer, mode 2: play with friends -- pass this value in to this function
        instructions = []
        if mode == 1:
            if self.currentPlayer != 1:
                instructions = ["Please wait..."]
            else:
                if self.deck.currentCard == None:
                    if validMoves == []:
                        instructions = ["Click on the draw pile to select a card."]
                    else:
                        for move in validMoves:
                            if move[1]['drawAgain']:
                                instructions = ["You get to draw again.", "Click on the draw pile to select a card."]
                            else:
                                instructions = ["Click on the draw pile to select a card."]

                elif validMoves == []:
                    instructions = ["You cannot move.", "Click the End Turn button."]
                elif validMoves != []:
                    if playState == 1:
                        instructions = ["Click on a highlighted pawn", "to see its possible moves."]
                    elif playState == 2:
                        instructions = ["Click on a highlighted space", "to move the pawn there."]
        if mode == 2:
            if self.deck.currentCard == None:
                if validMoves == []:
                    instructions = ["Click on the draw pile to select a card."]
                else:
                    for move in validMoves:
                        if move[1]['drawAgain']:
                            instructions = ["You get to draw again.", "Click on the draw pile to select a card."]
                        else:
                            instructions = ["Click on the draw pile to select a card."]

            elif validMoves == []:
                instructions = ["You cannot move.", "Click the End Turn button."]
            elif validMoves != []:
                if playState == 1:
                    instructions = ["Click on a highlighted pawn",  "to see its possible moves."]
                elif playState == 2:
                    instructions = ["Click on a highlighted space", "to move the pawn there."]
        return instructions

    def displayInstructions(self, screen, validMoves, playState):
        yLoc = 400
        myfont = pygame.font.SysFont('segoe UI', 15)
        instructions = self.getInstructions(validMoves, playState)
        for line in instructions:
            textsurface = myfont.render(line, False, (0, 0, 0))
            screen.blit(textsurface, (50, yLoc))
            yLoc += 25

