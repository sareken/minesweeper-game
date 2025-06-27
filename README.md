# minesweeper-game
## Description

This is a command-line version of the classic **Minesweeper** game developed using Python.  
The game randomly places mines on a square grid, and the player must reveal cells without hitting a mine.

## Game Modes

- **Hidden Mode**: Mines are not shown during play.
- **Visible Mode**: Mines are shown (for debugging or learning purposes).

## Features

- Dynamic grid size (minimum 10x10)
- Random mine placement (~30% of the grid)
- Win condition when all non-mine cells are revealed
- Immediate loss when a mine is selected
- Accurate handling of corner, edge, and center cells
- Replay and exit options after game ends

## Educational Purpose

This project was created as a part of a university assignment to reinforce the following topics:

- **Loops and conditional statements**
- **2D list operations**
- **User input handling**
- **Randomized data generation**
- **Game logic development**

## How to Run

1. Make sure Python is installed on your system.
2. Save the script as `minesweeper.py`.
3. Open terminal or a Python IDE.
4. Run the script with:

```bash
python minesweeper.py
```
## Notes
Grid size must be at least 10x10.

The player wins by successfully uncovering all cells that do not contain mines.

Selecting a mine ends the game immediately with a loss.


