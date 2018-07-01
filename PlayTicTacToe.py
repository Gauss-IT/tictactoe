from TicTacToeGame import TicTacToeGame

QUIT_GAME = "Q"

def IsQuit(input):
    if input == QUIT_GAME:
       print("Thank you from playing the game!")
       return True
    else:
        return False

def GetInput(game):
        (xMark, oMark) = game.Marks
        print("Please choose one of the options:")
        print(xMark + " or " + xMark.lower() + ", " 
            + oMark + " or " + oMark.lower() + ", " 
            + " any other input to quit the game:")

        userInput = str(input()).upper()
        return ( userInput if userInput in game.Marks
            else QUIT_GAME)             

def PlayTicTacToe():
    game = TicTacToeGame()
    while True:
       userInput = GetInput(game)       
       if IsQuit(userInput):
            return        
       game.PlayGame(userInput) 

PlayTicTacToe()