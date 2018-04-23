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
#    print(possibleMoves)

    validMoves = []
    for pawn in board.pawns:
        if pawn.player == player:
            for move in possibleMoves:
                moveInvalid = False
                if move['moveSpaces'] != 0:
                    newTile = board.getTargetTile(pawn, move['moveSpaces'])
#                    print(newTile)
                    if newTile == None:
                        moveInvalid = True
                    elif board.tiles[newTile]['specialType'] == 'home':
                        pass
                    else:
                        for otherPawn in board.pawns:
                            if otherPawn.tileName == newTile:
                                if otherPawn.player == player:
                                    moveInvalid = True
                    if not moveInvalid:
                        validMoves.append([pawn, move, newTile])

                if move['moveFromStart'] == True:
                    if board.checkInStart(pawn) == False:
                        moveInvalid = True
                    else:
                        newTile = Board.tiles[pawn.tileName]['tileAhead']
                        for otherPawn in board.pawns:
                            if otherPawn.tileName == newTile:
                                if otherPawn.player == player:
                                    moveInvalid = True
                    if not moveInvalid:
                        validMoves.append([pawn, move, newTile])

                if move['switchSpace'] == True:
                    if board.checkOnBoard(pawn) == False and board.checkInSafety(pawn) == False:
                        moveInvalid = True
                    else:
                        for otherPawn in board.pawns:
                            if board.checkOnBoard(otherPawn):
                                if otherPawn.player == player:
                                    moveInvalid = True
                                else:
                                    newTile = otherPawn.tileName
                            else:
                                moveInvalid = True
                            if not moveInvalid:
                                validMoves.append([pawn, move, newTile])

                if move['sorryCard'] == True:
                    if board.checkInStart(pawn) == False:
                        moveInvalid = True
                    else:
                        for otherPawn in board.pawns:
                            if board.checkOnBoard(otherPawn):
                                if otherPawn.player == player:
                                    moveInvalid = True
                                else:
                                    newTile = otherPawn.tileName
                            else:
                                moveInvalid = True
                            if not moveInvalid:
                                validMoves.append([pawn, move, newTile])
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
        print(pawn.name, pawn.tileName)

    board.deck.showCards()
    board.deck.drawCard()
    player = 1
    validMoves = getValidPossibleMoves(board, player)
    print(validMoves)
main()