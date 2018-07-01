import random
from TicTacToe import TicTacToe

class TicTacToeGame:    
    @property
    def Marks(self):
        return self.Game.Marks
    
    @property
    def EmptySelection(self):
        return self.Game.EmptySelection

    @property
    def Game(self):
        return self.__game

    def OutputBoardState(self, board = None):
        if board == None:
            board = self.Game.Board            
        
        print(*board[0:3])
        print(*board[3:6])
        print(*board[6:9])
        print()
                
    def OutputPossibleMoves(self):
        movesBoard = [self.EmptySelection if self.Game.HasSelection(i) 
                      else i + 1 
                      for i in range(len(self.Game.Board))]        
        self.OutputBoardState(movesBoard)
    
    def Validate(self, move):
        if move not in [x + 1 for x in self.Game.AllowedMoves()]:
            print("Your input does not specify a valid move")
            return False
        else:
             return True

    def GetInputMove(self):
        move = int(input("Where do you want to place it?"))
        while not self.Validate(move):
            print("Please enter one of the following inputs ")
            self.OutputPossibleMoves()
            move = int(input("Where do you want to place it?"))
        return move - 1    
        
    def MakeMove(self, currentMark, humanMark):
        position = self.GetInputMove() if currentMark == humanMark else self.Game.GetComputerMove()        
        self.Game.MakeMove(currentMark, position)

    def PlayGame(self, humanMark):       
        while True:
            for mark in self.Game.Marks:
                self.MakeMove(mark, humanMark)
                if self.Game.Win(mark):
                    self.OutputBoardState()
                    print("Player " + mark + " wins the game \n")
                    return
                elif self.Game.Draw():
                    self.OutputBoardState()
                    print("The game is a draw \n")
                    return
            self.OutputBoardState()
    
    def __init__(self):
        self.__game = TicTacToe()




