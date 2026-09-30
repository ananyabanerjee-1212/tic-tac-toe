# Tic-Tac-Toe (Python)

A simple two-player, command-line Tic-Tac-Toe game written in Python. The code is split into separate modules to keep it easy to read and extend.

## Features

- Two-player game (Player 1 = `X`, Player 2 = `O`)
- Custom player names (defaults to "Player 1" / "Player 2" if left blank)
- Empty cells are shown with their position numbers (1-9)
- Input validation: rejects non-numeric input, out-of-range numbers, and already-taken cells
- Automatic win and draw detection

## Requirements

- Python 3.6 or newer
- No external libraries needed

## How to Run

Keep all files in the same folder, then run:

```bash
python main.py
```

## How to Play

1. Both players enter their names.
2. On each turn, choose a number from 1 to 9. The positions map to the board like this:

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

3. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins.
4. If the board fills up with no winner, the game is a draw.

## Project Structure

```
.
├── main.py          # Game loop and entry point
├── game_board.py    # Board creation and display
├── game_logic.py    # Moves, win check, draw check
├── player.py        # Player name input
└── validation.py    # Valid position input
```

| File | Purpose |
|------|---------|
| `main.py` | Runs the overall game flow and switches turns |
| `game_board.py` | `create_board()`, `display_board()` |
| `game_logic.py` | `make_move()`, `check_winner()`, `check_draw()` |
| `player.py` | `get_player_names()` |
| `validation.py` | `get_valid_position()` |

## Example Output

```
================================
        TIC-TAC-TOE GAME
================================
Enter name for Player 1 (X): Rahul
Enter name for Player 2 (O): Aman

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Rahul's turn (X)
Choose a position (1-9): 5
```

## Future Improvements

- Computer (AI) opponent
- Score tracking and multiple rounds
- GUI version (Tkinter or Pygame)
