# [["pawn", 1]["rook", 2]["knight", 3]["bishop", 4]["queen", 5]["king", 6]["empty", 0]]

whiteTaken = []
blackTaken = []

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

class Board(object):

    def __init__(self, boardState = [[2, 3, 4, 5, 6, 4, 3, 2],[1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 1, 1, 1],[2, 3, 4, 5, 6, 4, 3, 2]], boardColor = "white"):
        self.state = boardState
        self.color = boardColor

    def getBoaradState(self):
        return(self.state)

    def setBoardState(self, piece, posOld, posNew):
        #positions come as list [row, column]
        global whiteTaken
        global blackTaken
        self.state[posOld[1]][posOld[2]] = 0
        if self.state[posNew[1]][posNew[2]]:
            if piece.getcolor() == "white":
                whiteTaken.append(self.state[posNew[1]][posNew[2]])
            else:
                blackTaken.append(self.state[posNew[1]][posNew[2]])
            self.state[posNew[1]][posNew[2]] = piece.getType()
        else:
            self.state[posNew[1]][posNew[2]] = piece.getType()