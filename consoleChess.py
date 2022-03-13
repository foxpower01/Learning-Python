# [["pawn", 1]["rook", 2]["knight", 3]["bishop", 4]["queen", 5]["king", 6]["empty", 0]], COLORS: [[0, black], [1, white]] ⬛♙♘♗♖♕♔♚♛♜♝♞♟

whiteTaken = []
blackTaken = []
symbols = [["□", "♙", "♖", "♘", "♗", "♕", "♔"], ["□", "♟", "♜", "♞", "♝", "♛", "♚"]]

class Board(object):

    def __init__(self, boardState = [[[2,0], [3,0], [4,0], [5,0], [6,0], [4,0], [3,0], [2,0]],[[0,0], [1,0], [1,0], [1,0], [1,0], [1,0], [1,0], [1,0]],[[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]],[[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]],[[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]],[[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]],[[1,1], [1,1], [1,1], [1,1], [1,1], [1,1], [1,1], [1,1]],[[2,1], [3,1], [4,1], [5,1], [6,1], [4,1], [3,1], [2,1]]], boardColor = 1):
        self.state = boardState
        self.color = boardColor

    def getBoaradState(self):
        return(self.state)

    def getPosition(self, position):
        print(position)
        return(self.state[position[0]][position[1]])

    def setBoardState(self, posOld, newPos):
        #positions come as list [row, column]
        global whiteTaken
        global blackTaken
        global piece
        self.state[posOld[0]][posOld[1]] = [0,0]
        if self.state[newPos[0]][newPos[1]][0]:
            if piece.getColor == 1:
                whiteTaken.append(self.state[newPos[0]][newPos[1]])
            else:
                blackTaken.append(self.state[newPos[0]][newPos[1]])
            self.state[newPos[0]][newPos[1]] = [piece.getType(), piece.getColor()]
        else:
            self.state[newPos[0]][newPos[1]] = [piece.getType(), piece.getColor()]
            print(self.state[newPos[0]][newPos[1]])
    
    def display(self, color):
        global board
        displayBoard = Board([], color)
        if color == 1:
            for row in board.state:
                tempRow = []
                for piece in row:
                    tempRow.append(symbols[piece[1]][piece[0]])
                displayBoard.state.append(tempRow)
        if color == 0:
            for row in reversed(board.state):
                tempRow = []
                for piece in reversed(row):
                    tempRow.append(symbols[piece[1]][piece[0]])
                displayBoard.state.append(tempRow)
        for row in displayBoard.state:
            print(row)

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

piece = Piece(2, [0,0], 0)

class Pawn(Piece):

    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)
    
    def hasMoved(self):
        if (self.color == 0 and self.position[0] == 2) or (self.color == 1 and self.position[0] == 7):
            return(False)
        else: 
            return(True)

    def canMove(self, newPos):
        if newPos == self.position:
            return(False)
        if newPos[1] == self.position[1]:
            if newPos[0] == self.position[0] + (-1) ** (self.color):
                if self.canTake(newPos):
                    return(True)
                else:
                    return(False)
            if newPos[0] == self.position[0] + 2 * (-1) ** (self.color) and self.hasMoved() == False:
                if self.canTake(newPos):
                    return(True)
                else:
                    return(False)
        if newPos[0] == self.position[0] + (-1) ** (self.color) and abs(newPos[1] - self.position[1]) == 1 and board.getPosition(newPos):
            if board.getPosition(newPos):
                if self.canTake(newPos):
                    return(True)
                else:
                    return(False)
            else:
                return(False)
        else:
            return(False)

class Rook(Piece):

    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)

    def canMove(self, newPos):
        step = 1
        if newPos == self.position:
            return(False)
        elif newPos[0] == self.position[0]:
            print("correct 1")
            if (newPos[1] < self.position[1] and self.color) == 1 or (newPos[1] > self.position[1] and self.color == 0):
                print("correct 2")
                step = -1
                for i in range(self.position[1] + step, newPos[1], step):
                    if board.getPosition([newPos[0], i]):
                        print("piece found")
                        return(False)
                if self.canTake(newPos):
                    print("correct 3")
                    return(True)
                else:
                    return(False)
            else:
                return(False)
        elif newPos[1] == self.position[1]:
            print("correct 1")
            if (newPos[0] < self.position[0] and self.color == 1) or (newPos[0] > self.position[0] and self.color == 0):
                print("correct 2")
                step = -1
                for i in range(self.position[0] + step, newPos[0], step):
                    if board.getPosition([i, newPos[1]]):
                        print("piece found")
                        return(False)
                if self.canTake(newPos):
                    print("correct 3")
                    return(True)
                else:
                    return(False)
        else:
            return(False)

class Knight(Piece):

    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)

    def canMove(self, newPos):
        print(newPos)
        print(self.position)
        if self.position == newPos:
            return(False)
        if (abs(newPos[0] - self.position[0]) == 1 and abs(newPos[1] - self.position[1]) == 2) or (abs(newPos[0] - self.position[0]) == 2 and abs(newPos[1] - self.position[1]) == 1):
            print("correct")
            if self.canTake(newPos):
                return(True)
            else:
                return(False)
        else:
            print("incorrect")
            return(False)

class Bishop(Piece):
    
    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)

    def canMove(self, newPos):
        step = []
        if newPos == self.position:
            return(False)
        elif abs(newPos[0] - self.position[0]) == abs(newPos[1] - self.position[1]):
            print("correct")
            if newPos[0] > self.position[0]:
                step.append(1)
            else:
                step.append(-1)
            if newPos[1] > self.position[1]:
                step.append(1)
            else:
                step.append(-1)
            print(step)
            for i in range(1, newPos[0] - self.position[0]):
                if board.getPosition([self.position[0]+step[0]*i, self.position[1]+step[1]*i]):
                    print("found piece")
                    return(False)
            if self.canTake(newPos):
                print("this works")
                return(True)
            else:
                print("cant take")
                return(False)
        else:
            return(False)
    
class Queen(Piece):

    def __init__(self, pieceType, piecePosition, pieceColor):
        super().__init__(pieceType, piecePosition, pieceColor)

    def canMove(self, newPos):
        if newPos == self.position:
            return(False)
        print("newpos", newPos)
        print("self", self.position)
        if newPos[0] == self.position[0] or newPos[1] == self.position[1]:
            step = 1
            if newPos[0] == self.position[0]:
                if newPos[1] < self.position[1]:
                    step = -1
                for i in range(self.position[1] + step, newPos[1], step):
                    if board.getPosition([newPos[0], i]):
                        return(False)
                if self.canTake(newPos):
                    return(True)
                else:
                    return(False)
            elif newPos[1] == self.position[1]:
                if newPos[0] < self.position[0]:
                    step = -1
                for i in range(self.position[0] + step, newPos[0], step):
                    if board.getPosition([i, newPos[1]]):
                        print("piece found")
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
        if abs(self.position[0] - newPos[0]) == 1 and abs(newPos[1] - self.position[1]) == 1:
            if board.getPosition(newPos):
                if self.canTake(newPos):
                    return(True)
                else:
                    return(False)
            else:
                return(False)

def parseInput(input):
    temp = input.split(", ")
    parse = []
    for item in temp:
        parse.append(int(item))
    return(parse)

def setPiece(piece):
    match piece.getType():
        case 1:
            piece = Pawn(1, piece.getPos(), piece.getColor())
        case 2:
            piece = Rook(2, piece.getPos(), piece.getColor())
        case 3:
            piece = Knight(3, piece.getPos(), piece.getColor())
        case 4:
            piece = Bishop(4, piece.getPos(), piece.getColor())
        case 5:
            piece = Queen(5, piece.getPos(), piece.getColor())
        case 6:
            piece = King(6, piece.getPos(), piece.getColor())
    return(piece)
    
    # if int(piece.getType()) == 1:
    #     piece = Pawn(1, piece.getPos(), piece.getColor())
    # elif int(piece.getType()) == 2:
    #     piece = Rook(2, piece.getPos(), piece.getColor())
    # elif int(piece.getType()) == 3:
    #     piece = Knight(3, piece.getPos(), piece.getColor())
    # elif int(piece.getType()) == 4:
    #     piece = Bishop(4, piece.getPos(), piece.getColor())
    # elif int(piece.getType()) == 5:
    #     piece = Queen(5, piece.getPos(), piece.getColor())
    # elif int(piece.getType()) == 6:
    #     piece = King(6, piece.getPos(), piece.getColor())
    # return(piece)

def turnW(): #atm only works with white, probably need to maake seperate black turn function
    global piece
    board.display(1)
    confirm = "n"
    while confirm != "y":
        piecePosition = parseInput(input("Player 1, chose a piece to move using its position: 'row, column'"))
        print(piecePosition)
        if board.getPosition(piecePosition)[1]:
            print(symbols[board.getPosition(piecePosition)[1]][board.getPosition(piecePosition)[0]])
            print(piecePosition)
            confirm = input("is this the piece you wanted to move? y/n")
            print(confirm)
        else:
            print("invalid piece.")
    piece = Piece(board.getPosition(piecePosition)[0], piecePosition, board.getPosition(piecePosition)[1])
    confirm = "n"
    while confirm != "y":
        newPos = parseInput(input("what position would you like to move this piece to? Input the position as 'row, column' "))
        if setPiece(piece).canMove(newPos):
            print(newPos)
            confirm = input("is this where you would like to move? y/n ")
        else:
            print("you can't move there!")
    board.setBoardState(piecePosition, newPos)
    board.display(1)

def turnB():
    global piece
    board.display(0)
    confirm = "n"
    while confirm != "y":
        piecePosition = parseInput(input("Player 2, chose a piece to move using its position: 'row, column' "))
        print(piecePosition)
        if board.getPosition(piecePosition)[1] == 0:
            print(symbols[board.getPosition(piecePosition)[1]][board.getPosition(piecePosition)[0]])
            confirm = input("is this the piece you wanted to move? y/n ")
        else:
            print("invalid piece.")
    piece = Piece(board.getPosition(piecePosition)[0], piecePosition, board.getPosition(piecePosition)[1])
    print(piece.getPos())
    confirm = "n"
    while confirm != "y":
        newPos = parseInput(input("what position would you like to move this piece to? Input the position as 'row, column' "))
        if setPiece(piece).canMove(newPos):
            print(newPos)
            confirm = input("is this where you would like to move? y/n ")
        else:
            print("you can't move there!")
    board.setBoardState(piecePosition, newPos)
    board.display(0)

def main():
    # global piece
    # board.display(1)
    # confirm = "n"
    # while confirm != "y":
    #     piecePosition = parseInput(input("Player one, chose a piece to move using its position: 'row, column'"))
    #     print(piecePosition)
    #     if board.getPosition(piecePosition)[1]:
    #         print(symbols[board.getPosition(piecePosition)[1]][board.getPosition(piecePosition)[0]])
    #         print(piecePosition)
    #         confirm = input("is this the piece you wanted to move? y/n")
    #         print(confirm)
    #     else:
    #         print("invalid piece.")
    # newPos = parseInput(input("what position would you like to move this piece to? Input the position as 'row, column'"))
    # piece = Piece(board.getPosition(piecePosition)[0], piecePosition, board.getPosition(piecePosition)[1])
    # if setPiece(piece).canMove(newPos):
    #     board.setBoardState(piecePosition, newPos)
    # board.display(0)
    for i in range(5):
        if i % 2:
            turnB()
        else:
            turnW()

if __name__ == "__main__":
    main()