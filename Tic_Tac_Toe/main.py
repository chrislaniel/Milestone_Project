
# List that will keep track of player markers
board = [" "," "," "," "," "," "," "," "," "]
 


#draw board
def print_board():
    print(board[0] + " |" + board[1] + " |" + board[2])
    print("__|__|__")
    print(board[3] + " |" + board[4] + " |" + board[5])
    print("__|__|__")
    print(board[6] + " |" + board[7] + " |" + board[8])
    print("  |  |  ")



#Player input   
choice = ""
position = ""

def player_input():
    #X or O is playing
    while True:
        x_o = input("Are you playing X or O? :")
        XO = x_o.upper() 
        if XO in ["X","O"]:
            global choice
            choice = XO
            break
        else :
            print("Please enter X or O")
            continue
            
    #Position to put the X or O
    while True:
        position_input = input("Enter position of your move (1-9):")
        if position_input.isdigit():
            Num_Position = int(position_input) 
        else:
            print("Please enter a valid position (1-9)")
            continue
            
        if Num_Position in range(0,10):
            global position 
            position = Num_Position
            break
        else :
            print("Please enter a valid position (1-9)")
            continue



#updating the board
def update_board():
    board[position-1] = choice



#checking if there is a winner
def winner():
    #possible winner options
    opt1 = board[0] == board[1] == board[2]
    opt2 = board[3] == board[4] == board[5]
    opt3 = board[6] == board[7] == board[8]
    opt4 = board[0] == board[3] == board[6]
    opt5 = board[1] == board[4] == board[7]
    opt6 = board[2] == board[5] == board[8]
    opt7 = board[0] == board[4] == board[8]
    opt8 = board[2] == board[4] == board[6]
 
    if opt1 == True and board[0] in ["X","O"]:
        print("Winner!")
    elif opt2 == True and board[3] in ["X","O"]:
        print("Winner!")
    elif opt3 == True and board[6] in ["X","O"]:
        print("Winner!")
    elif opt4 == True and board[0] in ["X","O"]:
        print("Winner!")
    elif opt5 == True and board[1] in ["X","O"]:
        print("Winner!")
    elif opt6 == True and board[2] in ["X","O"]:
        print("Winner!")
    elif opt7 == True and board[0] in ["X","O"]:
        print("Winner!")
    elif opt8 == True and board[2] in ["X","O"]:
        print("Winner!")
    else:
        pass


#check if we have a tie game
def tie_check():
    global board
    if (" ") in board:
        #will give back function to ask new player input
        pass
    else:
        print("We have a tie game")




  
    