
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

  
    