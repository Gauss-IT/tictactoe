import random

class TicTacToe:
    __EMPTY_SELECTION = "-"
    __X_MARK = "X"
    __O_MARK = "O"
    
    def __initializeBoard(self):
        return [self.EmptySelection for i in range(9)]
    
    def __isValidMark(self, mark):
        return mark in self.Marks

    @property
    def Board(self):
        return self.__board
    
    @property
    def Marks(self):
        return (self.__X_MARK, self.__O_MARK)

    @property
    def EmptySelection(self):
        return self.__EMPTY_SELECTION       

    def HasSelection(self, n):        
        return n in range(9) and self.Board[n] != self.EmptySelection

    def AllowedMoves(self):
        return [i for i in range(9) if self.Board[i] == self.EmptySelection]

    def Win(self, mark):
        fullRow = [mark] * 3
        b = self.__board

        return ( b[0:3] == fullRow   or b[3:6] == fullRow    or b[6:9] == fullRow
              or b[0:7:3] == fullRow or b[1:8:3] == fullRow  or b[2:9:3] == fullRow
              or b[0:9:4] == fullRow or b[2:7:2] == fullRow )

    def Draw(self):
        return self.EmptySelection not in self.Board
        
    def GetComputerMove(self):
        return int(random.choice(self.AllowedMoves()))

    def MakeMove(self, mark, position):
        if position in self.AllowedMoves() and self.__isValidMark(mark):
            self.Board[position] = mark
        else:
            Exception("Trying to play move that is not allowed")

    def __init__(self):
        self.__board = self.__initializeBoard()