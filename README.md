# Game of Life

**Object-oriented implementation of Conway's cellular automaton with configurable rules and a Tkinter GUI.**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational)

![Game of Life GUI](https://user-images.githubusercontent.com/107262375/190929856-eb3c5009-7ae3-42ef-a14e-ef3c0d705fe4.png)

The board is a finite grid of user-defined size. Each cell has 8 neighbours and is either alive or dead, and the board evolves in discrete steps. The rules are **not hard-coded to B3/S23**: the user chooses how many live neighbours keep a cell alive and how many bring a dead cell to life. This makes it possible to explore other "Life-like" automata.

## Features

- Configurable board size and **birth/survival rules**
- Click cells to toggle them, or fill the board at random
- Start, pause and reset the simulation, with a live count of alive cells and the share of the board that is alive
- Simulation engine **separated from the GUI**: the automaton can be run and tested headless

## Design

| Class | Responsibility |
|---|---|
| `Cell` | a single cell and its state |
| `Space` | the grid of cells (composition of `Cell` objects) |
| `GameMaster` | the "physics": counts neighbours and applies birth/survival rules to produce the next generation |
| `GameOfLife` | Tkinter front end; translates between the button grid and the `Space` |
| `Stats` | simple statistics about the running game |

## How to run

```bash
python -m pip install -e .
python -m scripts.run_gui
```

Tkinter has to be available in your Python installation; it ships with most Python distributions. The GUI asks for the board size and rule parameters.

Tests include a headless check of the classic **blinker** oscillator: `python -m unittest discover -s tests`.
