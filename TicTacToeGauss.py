import random

EMPTY_SELECTION = "-"
X_MARK = "X"
O_MARK = "O"
QUIT_GAME = "Q"

def InitializeBoard():
    board = [EMPTY_SELECTION for i in range(0, 9)]
    possible_places = [i for i in range(0, 9)]
    return (board, possible_places)

def OutputBoardState(board):
    print(*board[0:3])
    print(*board[3:6])
    print(*board[6:9])
    print()

def CheckIfWinner(mark, board):
    if board[0:3] == [mark, mark, mark] or board[3:6] == [mark, mark, mark]:
        return True
    if board[6:9] == [mark, mark, mark] or board[0:7:3] == [mark, mark, mark]:
        return True
    if board[1:8:3] == [mark, mark, mark] or board[2:9:3] == [mark, mark, mark]:
        return True
    if board[0:9:4] == [mark, mark, mark] or board[2:7:2] == [mark, mark, mark]:
        return True
    else:
        return False

def GetComputerMove(possible_places):
    return int(random.choice(possible_places))

def GetInputMove():
    spot = input("Where you want to place it ?")
    return int(spot)

def AskUserForSelection():
    print("Please choose one of the options:")
    print(X_MARK + " or " + X_MARK.lower() + ", " 
    + O_MARK + " or " + O_MARK.lower() + ", " 
    + QUIT_GAME + " or " + QUIT_GAME.lower() + " to quit the game: \n")

    userInput = str(input())
    if userInput.upper() == X_MARK:
        return X_MARK
    elif userInput.upper() == O_MARK:
        return O_MARK
    else:
        return QUIT_GAME

def PlayMove(currentMark, humanMark, board, possible_places):
    if currentMark == humanMark:
        position = GetInputMove()  
    else:
        position = GetComputerMove(possible_places)

    possible_places.remove(position)
    board[position] = currentMark

def MoveForPlayer(currentMark,humanMark, board, possible_places):
    PlayMove(currentMark, humanMark, board, possible_places)
    OutputBoardState(board)
    return CheckIfWinner(currentMark, board)

def PlayGame(humanMark):
    (board, possible_places) = InitializeBoard()
    
    while True:
        if MoveForPlayer(X_MARK, humanMark, board, possible_places):
            print("Player " + X_MARK + " wins the game")
            break

        if MoveForPlayer(O_MARK, humanMark, board, possible_places):
            print("Player " + O_MARK + " wins the game")
            break
        
def PlayGames():
    while True:
       humanMark = AskUserForSelection()
       
       if humanMark == QUIT_GAME:
            print("Thank you from playing the game!")
            return
        
       PlayGame(humanMark)   

PlayGames()
