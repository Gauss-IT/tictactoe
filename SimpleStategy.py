from TicTacToe import TicTacToe
from copy import deepcopy

def intersect(list1, list2):
    return [value for value in list1 if value in list2]

def getBestMove(mark : int, inputGame : TicTacToe):
    game = deepcopy(inputGame)
    allowedMoves = game.AllowedMoves()
    # Try to play a move that wins
    for move in allowedMoves:
        game.MakeMove(mark, move)
        if game.Win(mark):
            return move
        game.RevertMove(move)
    
    # Try to play a move that stops the opponent from winning
    opponent = game.OtherMark(mark)
    for move in allowedMoves:
        game.MakeMove(opponent, move)
        if game.Win(opponent):
            return move
        game.RevertMove(move)
    
    # Try to place on the center
    if game.Center in allowedMoves:
        return game.Center
    
    # Try to place on corner
    corners = intersect(game.Corners, allowedMoves)
    if len(corners) > 0:
        return corners[0]
    
    # Try to place on center squares of sides
    sideCenters = intersect(game.SideCenters, allowedMoves)
    if len(sideCenters) > 0:
        return sideCenters[0]
    
    if allowedMoves.count() > 0:
        return allowedMoves[0]
    else:
        Exception("No legal moves to play")

    