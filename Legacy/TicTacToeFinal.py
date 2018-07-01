import random
def Start():
    board=["-" for i in range(0,9)]
    possible_places = [i for i in range(0,9)]
    def pr_board():
        print(*board[0:3])
        print(*board[3:6])
        print(*board[6:9])
        if "-" not in board:
            if check_winner("X"):
                print("X has Won")
                Start()
            if check_winner("O"):
                print("O has Won")
                Start()
            print("tie")
            Start()
    def check_winner(c):
        if board[0:3] == [c,c,c] or board[3:6] == [c,c,c] or board[6:9]== [c,c,c] or board[0:7:3] == [c,c,c]:
            return True
        if board[1:8:3] == [c,c,c] or board[2:9:3]==[c,c,c]:
            return True
        if board[0:9:4]==[c,c,c] or board[2:7:2]==[c,c,c]:
            return True    
        else:
            return False
    while True:
        
        selector = input("X or O: ")
        possible_places = [i for i in range(0,9)]
        board=["-" for i in range(0,9)]
        while selector == "X" or selector=="x":
            spot = input("Where you want to place it ?")
            spot = int(spot)
            if spot-1 in possible_places:
                spot = spot-1
                
                possible_places.remove(spot)
                board[spot]="X"
                if check_winner("X"):
                    print("X has Won")
                    pr_board()
                    Start()
                try:
                    bot = int(random.choice(possible_places))+1
                    possible_places.remove(bot-1)
                    board[bot-1]="O"
                    if check_winner("O"):
                        print("O has Won")
                        pr_board()
                        Start()
                    pr_board()
                except IndexError:
                    pr_board()
            else:
                pass

        while selector =="O" or selector=="o":  
            bot = random.choice(possible_places)
            possible_places.remove(bot)
            board[bot]="X"
            pr_board()
            if check_winner("X"):
                    print("X has Won")
                    pr_board()
                    Start()
            spot = input("Where you want to place it ?")
            spot = int(spot)
            if spot-1 in possible_places:
                spot = spot-1
                possible_places.remove(spot)
                board[spot]="O"
                if check_winner("O"):
                    print("O has Won")
                    pr_board()
                    Start()

Start()