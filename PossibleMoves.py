from Board import Board

""""
Methods that score moves
"""

"""
Card methods
"""
#Method to return valid moves of a play
def getValidPossibleMoves(board, player):
    #Checks the current card and creates an array of valid moves
    possibleMoves = board.deck.currentCard.possibleMoves
    validMoves = []
    #Tests every pawn
    for pawn in board.pawns:
        #Tests the current users pawn
        if pawn.player == board.currentPlayer:
            #For every move in the array
            for move in possibleMoves:
                moveScore = 0
                moveInvalid = False

                if move['moveSpaces'] != 0:            ####MAYBE ADD A DISTANCE FROM HOME VARIABLE THAT GETS USED IF A TIE OR TO SELECT A SWITCH OR SORRY CARD MOVE
                    newTile = board.getTargetTile(pawn, move['moveSpaces'])
                    if newTile == None:
                        moveInvalid = True
                    elif board.tiles[newTile]['specialType'] == 'home':
                        if pawn.tileName <=60:
                            moveScore += 15 #combine additions for getting into safety and home
                                                                # because this move gets pawn off the outer track
                        else:
                            moveScore += 2  # already in safety zone, not the most important to
                                                                # get into home
                    else:
                        for otherPawn in board.pawns:
                            if otherPawn.tileName == newTile:
                                if otherPawn.player == player:
                                    moveInvalid = True
                    if not moveInvalid:
                        if move['moveSpaces'] > 0:
                            if board.tiles[newTile]['specialType'] == 'safety':
                                moveScore += 13
                            elif board.tiles[newTile]['specialType'] == 'home':
                                moveScore += 15
                            moveScore += move['moveSpaces']
#                            for newPawn in board.pawns:
#                                if board.tiles[newTile] == newPawn.tileName:
#                                        else:                              ####NEED TO ACCOUNT FOR MEAN/NICE SORRY OTHER SCORE
#                                            if pawn.mean == True:
#                                                moveScore += 15
#                                            else:
#                                                moveScore += -15

                        else:
                            moveScore += move['moveSpaces']                  #### NEED TO ACCOUNT FOR MOVE BACK SCORE
                        if board.tiles[newTile]['specialType'] == 'slide4':
                            moveScore += 3
                            for i in range(1, 4):
                                for newPawn in board.pawns:
                                    if board.tiles[newTile+i] == newPawn.tileName:
                                        if newPawn.player == board.currentPlayer:
                                            moveScore += -10
#                                        else:                              ####NEED TO ACCOUNT FOR MEAN/NICE SORRY OTHER SCORE
                                                                            ####ALSO MAYBE SORRY SELF FOR SLIDE? IF SORRY OTHER THIS OVERRIDES
#                                            if pawn.mean == True:
#                                                moveScore += 15
#                                            else:
#                                                moveScore += -15
                        elif board.tiles[newTile]['specialType'] == 'slide5':
                            moveScore += 4
                            for i in range(1, 4):
                                for newPawn in board.pawns:
                                    if board.tiles[newTile + i] == newPawn.tileName:
                                        if newPawn.player == board.currentPlayer:
                                            moveScore += -10
#                                        else:                              ####NEED TO ACCOUNT FOR MEAN/NICE SORRY OTHER SCORE
                                                                            ####ALSO MAYBE SORRY SELF FOR SLIDE? IF SORRY OTHER THIS OVERRIDES
#                                            if pawn.mean == True:          ###maybe make this a "mean add" number that can be added if smart, or used alone if dumb
#                                                moveScore += 15
#                                            else:
#                                                moveScore += -15

                        validMoves.append([pawn, move, newTile, moveScore])

                if move['moveFromStart']:
                    if not board.checkInStart(pawn):
                        moveInvalid = True
                    else:
                        newTile = Board.tiles[pawn.tileName]['tileAhead']
                        for otherPawn in board.pawns:
                            if otherPawn.tileName == newTile:
                                if otherPawn.player == player:
                                    moveInvalid = True
                    if not moveInvalid:
#                        for otherPawn in board.pawns:
#                            if otherPawn.tileName == newTile:
#                                if otherPawn.player != player:
#                                            if pawn.mean == True:          ####NEED TO ACCOUNT FOR MEAN/NICE SORRY OTHER SCORE
#                                                moveScore += 15
#                                            else:
#                                                moveScore += -15

                        moveScore += 14
                        validMoves.append([pawn, move, newTile, moveScore])

                if move['switchSpace']:
                    if not board.checkOnBoard(pawn):
                        if not board.checkInSafety(pawn):
                            moveInvalid = True
                    else:
                        for otherPawn in board.pawns:
                            if board.checkOnBoard(otherPawn):
                                if otherPawn.player == player:
                                    moveInvalid = True
                                else:
                                    newTile = otherPawn.tileName
                                    validMoves.append([pawn, move, newTile, moveScore])
                            else:
                                moveInvalid = True

                if move['sorryCard']:
                    if not board.checkInStart(pawn):
                        moveInvalid = True
                    else:
                        for otherPawn in board.pawns:
                            if board.checkOnBoard(otherPawn):
                                if otherPawn.player == player:
                                    moveInvalid = True
                                else:
                                    newTile = otherPawn.tileName
                                    validMoves.append([pawn, move, newTile, moveScore])
                            else:
                                moveInvalid = True
    for valMove in validMoves:
        print("pawn: ", valMove[0].name, "newTile: ", valMove[2], "score: ", valMove[3])

    return validMoves


def main():
#    card = 1
    board = Board(boardOrientation=0, boardLocation=(350, 0))
#    for pawn in board.pawns:
#        print("id:", pawn.name)
#        print("color", pawn.color)
#    getValidPossibleMoves(card, board.pawns)
#    pawn = Pawn(1, "red", 1, 84)
#    newTile = board.getTargetTile(pawn, 5)
#    print(newTile)
    pawnLocations = [61, 1, 3, 12, 4, 5, 6, 7, 8, 9, 10, 63, 64, 64, 64, 64]
    for pawn in board.pawns:
        pawn.tileName = pawnLocations[pawn.name-1]

#    board.deck.showCards()
    board.deck.drawCard()
    player = 1
    validMoves = getValidPossibleMoves(board, player)

    print(validMoves)
#main()

#    print(validMoves)
main()

