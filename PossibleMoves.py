from Board import Board

def distanceFromHome(board, player, tile):
    homeSpaces = [88, 70, 76, 82]
    numSpaces = 0
    countingSpace = tile
    while countingSpace != homeSpaces[player-1]:
        countingSpace = board.tiles[countingSpace]['tileAhead']
        numSpaces += 1
    print("distance from home ", numSpaces)
    return numSpaces

def getValidPossibleMoves(board, player, mean):
    possibleMoves = board.deck.currentCard.possibleMoves
    validMoves = []
    for pawn in board.pawns:
        if pawn.player == board.currentPlayer:
            for move in possibleMoves:
                moveScore = 0
                meanAdd = 0
                moveInvalid = False

                if move['moveSpaces'] != 0:            ####DISTANCE FROM HOME VARIABLE GETS USED IF A TIE OR TO SELECT A SWITCH OR SORRY CARD MOVE
                    oldTile = board.tiles[pawn.tileName]
                    newTile = board.getTargetTile(pawn, move['moveSpaces'])
                    if newTile == None:
                        moveInvalid = True
                    elif board.tiles[newTile]['specialType'] == 'home':
                        if pawn.tileName <=60:
                            moveScore += 15 #combine additions for getting into safety and home because this move gets pawn off the outer track
                        else:
                            moveScore += 2  # already in safety zone, not the most important to get into home
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
                            for newPawn in board.pawns:
                                if board.tiles[newTile] == newPawn.tileName:
                                    if mean[pawn.player-1] == True:
                                        meanAdd += 15
                                    else:
                                        meanAdd += -15

                        else:
                            distFromHomeChange = distanceFromHome(board, pawn.player, newTile) - distanceFromHome(board, pawn.player, oldTile)
                            if distFromHomeChange > 0:
                                moveScore += move['moveSpaces']                  #### NEED TO ACCOUNT FOR MOVE BACK SCORE
                            else:
                                moveScore -= move['moveSpaces']
                        if board.tiles[newTile]['specialType'] == 'slide4':
                            moveScore += 3
                            for i in range(1, 4):
                                for newPawn in board.pawns:
                                    if board.tiles[newTile+i] == newPawn.tileName:
                                        if newPawn.player == board.currentPlayer:
                                            moveScore += -10
                                        else:
                                            if mean[pawn.player-1] == True:
                                                meanAdd += 15
                                            else:
                                                meanAdd += -15
                        elif board.tiles[newTile]['specialType'] == 'slide5':
                            moveScore += 4
                            for i in range(1, 4):
                                for newPawn in board.pawns:
                                    if board.tiles[newTile + i] == newPawn.tileName:
                                        if newPawn.player == board.currentPlayer:
                                            moveScore += -10
                                        else:
                                            if mean[pawn.player-1] == True:          ###"mean add" number can be added to moveScore if smart, or used alone if dumb
                                                meanAdd += 15
                                            else:
                                                meanAdd += -15

                        validMoves.append([pawn, move, newTile, moveScore, meanAdd])

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
                        for otherPawn in board.pawns:
                            if otherPawn.tileName == newTile:
                                if otherPawn.player != player:
                                            if mean[pawn.player-1] == True:
                                                meanAdd += 15
                                            else:
                                                meanAdd += -15

                        moveScore += 14
                        validMoves.append([pawn, move, newTile, moveScore, meanAdd])

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
                                    oldTile = board.tiles[pawn.tileName]
                                    newTile = otherPawn.tileName
                                    moveScore = distanceFromHome(board, pawn.player, newTile) - distanceFromHome(board,
                                        pawn.player, oldTile)
                                    if distFromHomeChange > 0:
                                        moveScore += move['moveSpaces']
                                    else:
                                        moveScore -= move['moveSpaces']
                                    validMoves.append([pawn, move, newTile, moveScore, meanAdd])
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
                                    moveScore = distanceFromHome(board, pawn.player, newTile)
                                    validMoves.append([pawn, move, newTile, moveScore, meanAdd])
                            else:
                                moveInvalid = True
    for valMove in validMoves:
        print("pawn: ", valMove[0].name, "newTile: ", valMove[2], "score: ", valMove[3], "mean add: ", meanAdd)

    return validMoves
