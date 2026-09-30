# Project Statement

## Project Title

Tic-Tac-Toe Game

## Problem Statement

Traditional Tic-Tac-Toe is a simple two-player game where players take turns placing their symbols on a 3 × 3 grid. When played without a structured system, players need to manually track the board, validate moves, and determine the winner.

This project develops a Python-based console Tic-Tac-Toe game that manages the game board, validates player input, processes moves, checks winning conditions, and identifies draws.

## Project Scope

The project focuses on developing a simple two-player console-based Tic-Tac-Toe game using Python.

The system includes:

- Player name input
- 3 × 3 game board
- Player turn management
- Position validation
- Move processing
- Winner detection
- Draw detection
- Basic software testing

The project is designed for local execution through the Python command line.

## Target Users

The target users are:

- Students learning Python programming
- Beginners learning modular programming
- Users who want to play a simple console-based Tic-Tac-Toe game

## High-Level Features

1. **Player Management**
   - Accepts names of two players.
   - Assigns `X` to Player 1 and `O` to Player 2.

2. **Game Board Management**
   - Creates a 3 × 3 board.
   - Displays the current board after each turn.

3. **Move Validation**
   - Accepts positions from 1 to 9.
   - Prevents invalid or already occupied positions.

4. **Game Logic**
   - Processes player moves.
   - Checks all possible winning combinations.
   - Detects when the game ends in a draw.

5. **Testing**
   - Tests board creation.
   - Tests valid and invalid moves.
   - Tests winner and draw detection.

## Technologies Used

- Python
- VS Code
- Git
- GitHub

## Project Modules

- `main.py` – Controls the complete game flow.
- `game_board.py` – Creates and displays the board.
- `game_logic.py` – Handles moves, winner detection, and draw detection.
- `player.py` – Handles player names.
- `validation.py` – Validates player input and positions.
- `test_game.py` – Contains basic test cases.

## Expected Outcome

The expected outcome is a functional, modular, and easy-to-understand Python Tic-Tac-Toe game that allows two players to play through the console while providing input validation and automatic winner or draw detection.