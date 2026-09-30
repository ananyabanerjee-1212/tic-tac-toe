# Game logic for Tic-Tac-Toe


def make_move(board, position, symbol):
    """Place a symbol on the selected position."""
    if position < 1 or position > 9:
        return False

    index = position - 1

    if board[index] != " ":
        return False

    board[index] = symbol
    return True


def check_winner(board, symbol):
    """Check whether the given symbol has won."""
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == symbol and board[b] == symbol and board[c] == symbol:
            return True

    return False


def check_draw(board):
    """Check whether the game is a draw."""
    return all(position != " " for position in board)