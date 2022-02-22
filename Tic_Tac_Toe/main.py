from algos.game import player_input, is_winner, tie_check
from viz.board import print_board


def main():
    # List that will keep track of player markers
    # TO DO: Create board dynamically to support different size 
    board = [" "," "," "," "," "," "," "," "," "]

    winner = False
    tie = False
    while not winner and not tie:
        print_board(board)
        board, player = player_input(board)
        winner = is_winner(board)
        tie = tie_check(board)
    print_board(board)
    print(f"CONGRATS TO THE {player}")


if __name__ == "__main__":
    main()
