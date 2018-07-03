import random
from enum import Enum

class TicTacToe:
    __EMPTY_SELECTION = "-"
    __X_MARK = "X"
    __O_MARK = "O"

    FullRows = [# Rows
                (0,1,2), (3,4,5), (6,7,8),
                # Columns
                (0,3,6), (1,4,7), (2,5,8),
                # Diagonals
                (0,4,8), (2,4,6)]
    
    Center = 4
    Corners = [0,2,6,8]
    SideCenters = [2,3,5,7]
        
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

    def OtherMark(self, mark):
        if mark == self.__X_MARK:
            return self.__O_MARK
        elif mark == self.__O_MARK:
            return self.__X_MARK
        else:
             Exception("Mark is not recognized")

    def HasSelection(self, n):        
        return n in range(9) and self.Board[n] != self.EmptySelection

    def AllowedMoves(self):
        return [i for i in range(9) if self.Board[i] == self.EmptySelection]

    def Win(self, mark):
        b = self.__board
        for (n1, n2, n3) in self.FullRows:
            if b[n1] == mark and b[n2] == mark and b[n3] == mark:
                return True
        return False

    def Draw(self):
        return self.EmptySelection not in self.Board
        
    def GetComputerMove(self):
        return int(random.choice(self.AllowedMoves()))

    def MakeMove(self, mark, position):
        if position in self.AllowedMoves() and self.__isValidMark(mark):
            self.Board[position] = mark
        else:
            Exception("Trying to play move that is not allowed")
    
    def RevertMove(self, position):
        self.Board[position] = self.__EMPTY_SELECTION

    def Reset(self):
        self.__board = self.__initializeBoard()

    def __init__(self):
        self.__board = self.__initializeBoard()
        