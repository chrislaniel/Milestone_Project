from algos.utils import update_board

# TO DO:  build win conditions dynamically
WIN_CONDITIONS = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def is_winner(board, win_conditions=WIN_CONDITIONS):
    is_winner = False
    #possible winner options
    for x,y,z in win_conditions:
        if board[x] in ["X","O"] and \
            board[x] == board[y] == board[z]:
            is_winner = True
            break
    return is_winner


def pick_player(board):
    num_x = board.count("X")
    num_o = board.count("O")
    total = num_x - num_o

    if total == 0:
        return "X"
    else:
        return "O"

def player_input(board):
    # Determine if X or O playing
    player = pick_player(board)
    query_text = "Enter position of your move (1-9):"

    invalid_input = True
    while invalid_input:
        # Ask for input
        position_input = input(query_text)
        # Check if input is a valid number
        if position_input.isdigit():
            # Making sure it's an int
            position_input = int(position_input)
            if position_input in range(1,10):
                if board[position_input - 1] == " ":
                    invalid_input = False
                else:
                    print("Already a marker at this location.")
            else:
                print("Index outside of the board range.")
    # Update board with the value
    board = update_board(board, player, position_input)
    return board, player

# Check if we have a tie game
def tie_check(board):
    if (" ") in board:
        return False
    else:
        return True
