# Main file for Tic-Tac-Toe

from game_board import create_board, display_board
from game_logic import make_move, check_winner, check_draw
from player import get_player_names
from validation import get_valid_position


def main():
    print("================================")
    print("        TIC-TAC-TOE GAME")
    print("================================")

    # Get player names
    player1, player2 = get_player_names()

    # Create empty board
    board = create_board()

    current_player = player1
    current_symbol = "X"

    while True:
        display_board(board)

        print(f"{current_player}'s turn ({current_symbol})")

        # Get a valid position from validation module
        position = get_valid_position(board)

        # Make the move
        make_move(board, position, current_symbol)

        # Check winner
        if check_winner(board, current_symbol):
            display_board(board)
            print(f"Congratulations! {current_player} wins!")
            break

        # Check draw
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch player
        if current_symbol == "X":
            current_player = player2
            current_symbol = "O"
        else:
            current_player = player1
            current_symbol = "X"


if __name__ == "__main__":
    main()