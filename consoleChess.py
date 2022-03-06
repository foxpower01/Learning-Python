# [["pawn", 1]["rook", 2]["knight", 3]["bishop", 4]["queen", 5]["king", 6]["empty", 0]], COLORS: [[0, black], [1, white]]

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

    def setBoardState(self, piece, posOld, posNew):
        #positions come as list [row, column]
        global whiteTaken
        global blackTaken
        self.state[posOld[0]][posOld[1]] = [0,0]
        if self.state[posNew[0]][posNew[1]][0]:
            if piece.getcolor() == 1:
                whiteTaken.append(self.state[posNew[0]][posNew[1]])
            else:
                blackTaken.append(self.state[posNew[0]][posNew[1]])
            self.state[posNew[0]][posNew[1]] = piece.getType()
        else:
            self.state[posNew[0]][posNew[1]] = piece.getType()

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

    def canTake(self, posNew):
        if self.color == board.getPosition(posNew)[1]:
            return(False)
        return(True)

class Pawn(Piece):

    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)

class Rook(Piece):

    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)

class Knight(Piece):

    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)

class Bishop(Piece):
    
    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)
    
class Queen(Piece):

    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)

class King(Piece):

    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)
    
    def isCheck(self, position):
        return(False)

    def canMove(self, posNew):
        if self.position[0] == posNew[0]:
            if abs(self.position[1] - posNew[1]) == 1:
                if self.canTake:
                    return(True)
        if self.position[1] == posNew[1]:
            if abs(self.position[0] - posNew[0]) == 1:
                if self.canTake:
                    return(True)

