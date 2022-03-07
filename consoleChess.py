# [["pawn", 1]["rook", 2]["knight", 3]["bishop", 4]["queen", 5]["king", 6]["empty", 0]], COLORS: [[0, black], [1, white]]

from ast import Return
from re import A


whiteTaken = []
blackTaken = []

class Board(object):

    def __init__(self, boardState = [[[2,0], [3,0], [4,0], [5,0], [6,0], [4,0], [3,0], [2,0]],[[1,0], [1,0], [1,0], [1,0], [1,0], [1,0], [1,0], [1,0]],[[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]],[[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]],[[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]],[[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]],[[1,1], [1,1], [1,1], [1,1], [1,1], [1,1], [1,1], [1,1]],[[2,1], [3,1], [4,1], [5,1], [6,1], [4,1], [3,1], [2,1]]], boardColor = "white"):
        self.state = boardState
        self.color = boardColor

    def getBoaradState(self):
        return(self.state)

    def getPosition(self, position):
        return(self.state[position[0]][position[1]])

    def setBoardState(self, piece, posOld, newPos):
        #positions come as list [row, column]
        global whiteTaken
        global blackTaken
        self.state[posOld[0]][posOld[1]] = [0,0]
        if self.state[newPos[0]][newPos[1]][0]:
            if piece.getcolor() == 1:
                whiteTaken.append(self.state[newPos[0]][newPos[1]])
            else:
                blackTaken.append(self.state[newPos[0]][newPos[1]])
            self.state[newPos[0]][newPos[1]] = piece.getType()
        else:
            self.state[newPos[0]][newPos[1]] = piece.getType()

board = Board()

class Piece(object):

    def __init__(self, pieceType, piecePosition, pieceColor):
        self.type = pieceType
        self.position = piecePosition
        self.color = pieceColor

    def getColor(self):
        return(self.color)

    def getPos(self):
        return(self.position)

    def getType(self):
        return(self.type)

    def canTake(self, newPos):
        if board.getPosition(newPos)[0] == 0:
            return(True)
        elif self.color == board.getPosition(newPos)[1]:
            return(False)
        return(True)

class Pawn(Piece):

    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)
    
    def hasMoved(self):
        if (self.color == 0 and self.position[0] == 2) or (self.color == 1 and self.position[0] == 7):
            return(False)
        else: 
            return(True)

class Rook(Piece):

    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)

    def canMove(self, newPos):
        step = 1
        if newPos == self.position:
            return(False)
        elif newPos[0] == self.position[0]:
            if newPos[1] < self.position[1]:
                step = -1
            for i in range(self.position[1] + 1, newPos[1], step):
                if board.getPosition([newPos[0], i]):
                    return(False)
                if self.canTake(newPos):
                    return(True)
                else:
                    return(False)
            else:
                return(False)
        elif newPos[1] == self.position[1]:
            if newPos[0] < self.position[0]:
                step = -1
            for i in range(self.position[0] + 1, newPos[0], step):
                if board.getPosition([newPos[1], i]):
                    return(False)
                if self.canTake(newPos):
                    return(True)
                else:
                    return(False)
        else:
            return(False)

class Knight(Piece):

    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)

    def canMove(self, newPos):
        if self.position == newPos:
            return(False)
        if (abs(newPos[0] - self.position[0]) == 1 and abs(newPos[1] - newPos[1]) == 3) or (abs(newPos[0] - self.position[0]) == 3 and abs(newPos[1] - newPos[1]) == 1):
            if self.canTake(newPos):
                return(True)
            else:
                return(False)
        else:
            return(False)

class Bishop(Piece):
    
    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)

    def canMove(self, newPos):
        step = []
        if newPos == self.position:
            return(False)
        elif abs(newPos[0] - self.position[0]) == abs(newPos[1] - self.position[1]):
            if newPos[0] > self.position[0]:
                step.append(1)
            else:
                step.append(-1)
            if newPos[1] > self.position[1]:
                step.append(1)
            else:
                step.append(-1)
            for i in range(1, newPos[0] - self.position[0]):
                if board.getPosition([self.position[0]+step[0]*i, self.position[1]+step[1]*i]):
                    return(False)
                if self.canTake(newPos):
                    return(True)
                else:
                    return(False)
        else:
            return(False)
    
class Queen(Piece):

    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)

    def canMove(self, newPos):
        if newPos == self.position:
            return(False)
        if newPos[0] == self.position[0] or newPos[1] == self.position[1]:
            step = 1
            if newPos[0] == self.position[0]:
                if newPos[1] < self.position[1]:
                    step = -1
                for i in range(self.position[1] + 1, newPos[1], step):
                    if board.getPosition([newPos[0], i]):
                        return(False)
                    if self.canTake(newPos):
                        return(True)
                    else:
                        return(False)
            elif newPos[1] == self.position[1]:
                if newPos[0] < self.position[0]:
                    step = -1
                for i in range(self.position[0] + 1, newPos[0], step):
                    if board.getPosition([newPos[1], i]):
                        return(False)
                    if self.canTake(newPos):
                        return(True)
                    else:
                        return(False)
        if abs(newPos[0] - self.position[0]) == abs(newPos[1] - self.position[1]):
            step = []
            if newPos[0] > self.position[0]:
                step.append(1)
            else:
                step.append(-1)
            if newPos[1] > self.position[1]:
                step.append(1)
            else:
                step.append(-1)
            for i in range(1, newPos[0] - self.position[0]):
                if board.getPosition([self.position[0]+step[0]*i, self.position[1]+step[1]*i]):
                    return(False)
                if self.canTake(newPos):
                    return(True)
                else:
                    return(False)
        else:
            return(False)

class King(Piece):

    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)
    
    def isCheck(self, position):
        return(False)

    def canMove(self, newPos):
        if newPos == self.position:
            return(False)
        if self.position[0] == newPos[0]:
            if abs(self.position[1] - newPos[1]) == 1:
                if self.canTake(newPos):
                    return(True)
        if self.position[1] == newPos[1]:
            if abs(self.position[0] - newPos[0]) == 1:
                if self.canTake(newPos):
                    return(True)