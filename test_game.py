# Test cases for Tic-Tac-Toe

from game_board import create_board
from game_logic import make_move, check_winner, check_draw


def test_create_board():
    board = create_board()

    assert len(board) == 9
    assert all(position == " " for position in board)


def test_make_move():
    board = create_board()

    result = make_move(board, 1, "X")

    assert result is True
    assert board[0] == "X"


def test_invalid_move():
    board = create_board()

    make_move(board, 1, "X")
    result = make_move(board, 1, "O")

    assert result is False


def test_winner():
    board = create_board()

    make_move(board, 1, "X")
    make_move(board, 2, "X")
    make_move(board, 3, "X")

    assert check_winner(board, "X") is True


def test_draw():
    board = [
        "X", "O", "X",
        "X", "O", "O",
        "O", "X", "X"
    ]

    assert check_draw(board) is True


print("All test cases passed!")