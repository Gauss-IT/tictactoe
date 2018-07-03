from TicTacToe import TicTacToe
import SimpleStategy

class TicTacToeGame:    
    @property
    def Marks(self):
        return self.__game.Marks
    
    @property
    def EmptySelection(self):
        return self.__game.EmptySelection

    def OutputBoardState(self, board = None):
        if board == None:
            board = self.__game.Board            
        
        print(*board[0:3])
        print(*board[3:6])
        print(*board[6:9])
        print()
                
    def OutputPossibleMoves(self):
        movesBoard = [self.EmptySelection if self.__game.HasSelection(i) 
                      else i + 1 
                      for i in range(len(self.__game.Board))]        
        self.OutputBoardState(movesBoard)
    
    def Validate(self, move):
        if move not in [x + 1 for x in self.__game.AllowedMoves()]:
            print("Your input does not specify a valid move")
            return False
        else:
             return True
    def GetComputerMove(self, humanMark):
        return (SimpleStategy
        .getBestMove(self.__game.OtherMark(humanMark), self.__game))

    def GetInputMove(self):
        move = int(input("Where do you want to place it?"))
        while not self.Validate(move):
            print("Please enter one of the following inputs ")
            self.OutputPossibleMoves()
            move = int(input("Where do you want to place it?"))
        return move - 1    
        
    def MakeMove(self, currentMark, humanMark):
        position = (self.GetInputMove() if currentMark == humanMark 
               else self.GetComputerMove(humanMark) )       
        self.__game.MakeMove(currentMark, position)

    def PlayGame(self, humanMark):       
        self.__game.Reset()
        while True:
            for mark in self.__game.Marks:
                self.MakeMove(mark, humanMark)
                if self.__game.Win(mark):
                    self.OutputBoardState()
                    print("Player " + mark + " wins the game \n")
                    return
                elif self.__game.Draw():
                    self.OutputBoardState()
                    print("The game is a draw \n")
                    return
            self.OutputBoardState()
    
    def __init__(self):
        self.__game = TicTacToe()




