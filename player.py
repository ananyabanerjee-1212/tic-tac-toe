# Player management for Tic-Tac-Toe


def get_player_names():
    """Get and return the names of the two players."""

    player1 = input("Enter name of Player 1 (X): ").strip()
    player2 = input("Enter name of Player 2 (O): ").strip()

    # Default names if the user leaves the input empty
    if not player1:
        player1 = "Player 1"

    if not player2:
        player2 = "Player 2"

    return player1, player2