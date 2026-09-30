# Input validation for Tic-Tac-Toe


def is_valid_position(position):
    """Check whether the position is between 1 and 9."""
    return 1 <= position <= 9


def is_position_empty(board, position):
    """Check whether the selected position is empty."""
    if not is_valid_position(position):
        return False

    index = position - 1
    return board[index] == " "


def get_valid_position(board):
    """Ask the player for a valid empty position."""

    while True:
        try:
            position = int(input("Enter position (1-9): "))

            if not is_valid_position(position):
                print("Please enter a number between 1 and 9.")
                continue

            if not is_position_empty(board, position):
                print("That position is already occupied. Choose another.")
                continue

            return position

        except ValueError:
            print("Invalid input. Please enter a number.")