import random
import itertools
def Win(c):
    if board[0:3] == [c,c,c] or board[3:6] == [c,c,c] or board[6:9]== [c,c,c] or board[0:7:3] == [c,c,c]:
        return True
    if board[1:8:3] == [c,c,c] or board[2:9:3]==[c,c,c]:
        return True
    if board[0:9:4]==[c,c,c] or board[2:7:2]==[c,c,c]:
        return True    
    else:
        return False
def res(c):
    print(c+" Has Won")
def update():
    board[0][0] = all[0] 
    board[0][1] = all[1] 
    board[0][2] = all[2]
    board[1][0] = all[3]
    board[1][1] = all[4] 
    board[1][2] = all[5] 
    board[2][0] = all[6] 
    board[2][1] = all[7] 
    board[2][2] = all[8]   
def Layout():
    print(*board[0])
    print(*board[1])
    print(*board[2])
def uplay():
    update()
    Layout()
Play=True
while Play==True:
    board = [["1","2","3"],["4","5","6"],["7","8","9"]]
    all=board[0]+board[1]+board[2]
    win_combo =[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,8],[3,5,7]]
    
    print(all[0:7:3])
    Layout()
    balance = [i for i in range(1,10)]
    Get_Sy = input("Select First player (X) or Second player (O):  ")
    def bot_move(o):
        if len(balance)>7:
            Good=[1,3,7,9]
            for x in Good:
                if x in balance:
                    good_move = random.choice(Good)
                    return good_move
                else:
                    Good.remove(x)
        else:
            comb= []
            for sl in itertools.combinations(win_combo, 3):
                comb.append(sl)
            for x,y,z in comb[0]:
                if all[x] == o and all[y] ==o :
                    return int(z)
                if all[x] == o :
                    ra = [y,z]
                    return int(random.choice(ra))

            
            
    if Get_Sy == "X" or Get_Sy =="x":
        while balance !=[]:
            get_pos = input("Where you want to place your X form " + "".join(str(balance))[1:-1]+" : ")
            if int(get_pos) not in balance:
                    get_pos = input("Make sure you want to place your O form " + "".join(str(balance))[1:-1]+" : ")
            try:
                while int(get_pos) not in balance:
                    print("Number is not avaliabe!")
                    get_pos = input("Where you want to place your X form " + "".join(str(balance))[1:-1]+" : ")
                else:
                    
                    all[int(get_pos)-1] = "X"
                    balance.remove(int(get_pos))
                    Win("X")
                    if balance != []:
                        rand= int(random.choice(balance))
                        all[bot_move("O")-1] = "O"
                        balance.remove(bot_move("O"))
                        if Win("O"):
                            print("WON The O")
                            balance=[]
                            check = input("If you want to play Again type 'yes' :")
                            if check == "yes":
                                Play = True
                            else:
                                Play = False
                        
                            
                        
                        uplay()
                    else:
                        uplay()
                        print("Tie")
                        check = input("If you want to play Again type 'yes' :")
                        if check == "yes":
                            Play = True
                        else:
                            Play = False
                        
            except ValueError:
                print("You typed a wrong Character")        
    if Get_Sy == "O" or Get_Sy =="o" or Get_Sy=="0":
        while balance !=[]:
            rand= int(random.choice(balance))
            all[rand-1] = "X"
            balance.remove(rand)
            print("Computer Move Was: "+str(rand))
            uplay() 
            if balance != []:
                get_pos = input("Where you want to place your O form " + "".join(str(balance))[1:-1]+" : ")
                
                if int(get_pos) not in balance:
                    get_pos = input("Make sure you want to place your O form " + "".join(str(balance))[1:-1]+" : ")
                all[int(get_pos)-1] = "O"
                balance.remove(int(get_pos))
            else:
                print("tie")
                check = input("If you want to play Again type 'yes'  :")
                if check == "yes":
                            Play = True
                else:
                    Play = False
                    uplay()
               
