from Board import Board

""""
Methods that score moves
"""
# def scoreMoveForward(currentPositions, pawn, numberOfSpaces):
#     spacesScore = numberOfSpaces
#     if currentPositions[pawn.pawnSpace + numberOfSpaces] == otherPawn:
#         sorryOtherScore += 1
#     if currentPositions[pawn.pawnSpace + numberOfSpaces] == startOfSlide:
#         spacesScore += lengthOfSlide
#         sorryOtherScore += countSorrysFromSlide(currentPositions, pawn, lengthOfSlide)[0]
#         sorrySelfScore = countSorrysFromSlide(currentPositions, pawn, lengthOfSlide)[1]
#     totalScore = spacesScore + sorryOtherScore - sorrySelfScore
#     return totalScore
#
# def scoreMoveBackward(currentPositions, pawn, numberOfSpaces):
#     if currentPositions[pawn.pawnSpace - numberOfSpaces] < currentPositions[pawn.pawnSpace]:
#         spacesScore = 0 - numberOfSpaces
#     else:
#         spacesScore = currentPositions[pawn.pawnSpace - numberOfSpaces] - currentPositions[pawn.pawnSpace]
#
#     if currentPositions[pawn.pawnSpace - numberOfSpaces] == otherPawn:
#         sorryOtherScore += 1
#
#     if currentPositions[pawn.pawnSpace - numberOfSpaces] == startOfSlide:
#         spacesScore += lengthOfSlide
#         sorryOtherScore += countSorrysFromSlide(currentPositions, pawn, lengthOfSlide)[0]
#         sorrySelfScore = countSorrysFromSlide(currentPositions, pawn, lengthOfSlide)[1]
#
#     totalScore = spacesScore + sorryOtherScore - sorrySelfScore
#
#     return totalScore
#
# def scoreMoveToSpace():
#     def scoreMoveFromStart():
#
#         def countSorrysFromSlide(currentPositions, pawn, lengthOfSlide):
#             sorryOther = 0
#             sorrySelf = 0
#             for i in range(lengthOfSlide):
#                 if currentPositions[pawn.pawnSpace + i] == otherPawn:
#                     sorryOther += 1
#                 if currentPositions[pawn.pawnSpace + i] == ownPawn:
#                     sorrySelf += 1
#             return [sorryOther, sorrySelf]

#def scoreMoveFromStart():

# def countSorrysFromSlide(currentPositions, pawn, lengthOfSlide):
#     sorryOther = 0
#     sorrySelf = 0
#     for i in range(lengthOfSlide):
#         if currentPositions[pawn.pawnSpace + i] == otherPawn:
#             sorryOther += 1
#         if currentPositions[pawn.pawnSpace + i] == ownPawn:
#             sorrySelf += 1
#     return [sorryOther, sorrySelf]


"""
Methods that calculate the result of a move
"""
# def moveForward(currentPositions, pawn, numberOfSpaces):
#     if currentPositions[pawn.pawnSpace + numberOfSpaces] == otherPawn:
#         moveToSpace(currentPositions[pawn.pawnSpace + numberOfSpaces])
#         sorryOther(pawnAt.currentPositions[pawn.pawnSpace + numberOfSpaces])
#     if currentPositions[pawn.pawnSpace + numberOfSpaces] == startOfSlide:
#         moveToSpace(currentPositions[pawn.pawnSpace + numberOfSpaces + lengthOfSlide])
#         slide(currentPositions, pawn, lengthOfSlide)
#     else:
#         moveToSpace(currentPositions[pawn.pawnSpace + numberOfSpaces])
#
# def moveBackward(currentPositions, pawn, numberOfSpaces):
#     if currentPositions[pawn.pawnSpace - numberOfSpaces] == otherPawn:
#         moveToSpace(currentPositions[pawn.pawnSpace - numberOfSpaces])
#         sorryOther(pawnAt.currentPositions[pawn.pawnSpace - numberOfSpaces])
#     if currentPositions[pawn.pawnSpace - numberOfSpaces] == startOfSlide:
#         moveToSpace(currentPositions[pawn.pawnSpace - numberOfSpaces + lengthOfSlide])
#         slide(currentPositions, pawn, lengthOfSlide)
#     else:
#         moveToSpace(currentPositions[pawn.pawnSpace - numberOfSpaces])


#def moveToSpace(spaceNumber):

# def moveFromStart():
#     if pawn.pawnInStart:
#         if currentPositions[pawn.pawnSpace + 1] != ownPawn:
#             moveFromStart += 1
#             if currentPositions[pawn.pawnSpace + 1] == otherPawn:
#                 sorryOtherMove += 1


#def drawAgain():


#def sorryOtherPawn():

#def sorryOwnPawn():


"""
Card methods
"""
def getValidPossibleMoves(board, player):
    possibleMoves = board.deck.currentCard.possibleMoves
    validMoves = []
    for pawn in board.pawns:
        if pawn.player == board.currentPlayer:
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
#    print(validMoves)
main()