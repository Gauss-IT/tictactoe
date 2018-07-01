from TicTacToeGame import TicTacToeGame

QUIT_GAME = "Q"

def GetInput(marks):
        (xMark, oMark) = marks
        print("Please choose one of the options:")
        print(xMark + " or " + xMark.lower() + ", " 
            + oMark + " or " + oMark.lower() + ", " 
            + " any other input to quit the game:")

        userInput = str(input()).upper()
        return userInput if userInput in marks else QUIT_GAME             

def PlayTicTacToe():
    game = TicTacToeGame()
    while True:
       humanMark = GetInput(game.Marks)       
       if humanMark == QUIT_GAME:
            print("Thank you from playing the game!")
            return
        
       game.PlayGame(humanMark)   

PlayTicTacToe()