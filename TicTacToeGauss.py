import random

EMPTY_SELECTION = "-"
X_MARK = "X"
O_MARK = "O"
QUIT_GAME = "Q"

def InitializeBoard():
    return [EMPTY_SELECTION for i in range(0, 9)]

def OutputBoardState(board):
    print(*board[0:3])
    print(*board[3:6])
    print(*board[6:9])
    print()

def AllowedMoves(board):
    return [i for i in range(9) if board[i] == EMPTY_SELECTION]
            
def OutputPossibleMoves(board):
    movesBoard = [EMPTY_SELECTION] * 9
    for i in range(9):
        if board[i] == EMPTY_SELECTION:
            movesBoard[i] = i + 1
    OutputBoardState(movesBoard)

def Win(mark, board):
    fullRow = [mark]*3
    win = (board[0:3] == fullRow or board[3:6] == fullRow or board[6:9] == fullRow
    or board[0:7:3] == fullRow or board[1:8:3] == fullRow or board[2:9:3] == fullRow
    or board[0:9:4] == fullRow or board[2:7:2] == fullRow)
    
    if win:
        print("Player " + mark + " wins the game \n")
    return win

def Draw(board):
    draw = EMPTY_SELECTION not in board
    if draw:
        print("The game is a draw \n")

    return draw

def GetInputMove(board):
    allowedUserInputs = [x + 1 for x in AllowedMoves(board)]
    move = int(input("Where do you want to place it (please select an empty field) ?"))
    while move not in allowedUserInputs:
        print("Your input does not specify a valid move")
        print("Please enter one of the following inputs ")
        OutputPossibleMoves(board)
        move = int(input("Where do you want to place it?"))
    return move - 1

def GetInput():
    print("Please choose one of the options:")
    print(X_MARK + " or " + X_MARK.lower() + ", " 
        + O_MARK + " or " + O_MARK.lower() + ", " 
        + " any other input to quit the game:")

    userInput = str(input()).upper()
    if userInput == X_MARK or userInput == O_MARK:
        return userInput
    else:
        return QUIT_GAME

def GetComputerMove(board):
    return int(random.choice(AllowedMoves(board)))

def MakeMove(currentMark, humanMark, board):
    if currentMark == humanMark:
        position = GetInputMove(board)
    else:
        position = GetComputerMove(board)
    
    board[position] = currentMark

def PlayGame(humanMark):
    board = InitializeBoard()
    
    while True:
        for mark in [X_MARK,O_MARK]:
            MakeMove(mark, humanMark, board)
            if Win(mark, board) or Draw(board):
                OutputBoardState(board)
                return
            OutputBoardState(board)
        
def PlayGames():
    while True:
       humanMark = GetInput()
       
       if humanMark == QUIT_GAME:
            print("Thank you from playing the game!")
            return
        
       PlayGame(humanMark)   

PlayGames()
