# Game-Of-Life

Install Python 3.11+ and `python -m pip install -e .`. From the repository root run `python -m scripts.run_gui`. Commands execute experiments or launch the application; importing the model package is separate.

See [layout](docs/layout.md) and [file migration](docs/file-migration.json). Source implementations, author attribution in supplied reports and distinct historical variants are retained. New figure/table outputs are routed to results/generated. Dependency declarations describe imports, not a reconstruction of the original historical environment. No new licence is assigned.

## Current limitations

Tkinter must be available in your Python installation; it is not installed through a tkinter PyPI dependency. GUI asks for board size and rule parameters. Core rules can be imported and tested without opening windows.

## Checks

`python -m unittest discover -s tests -v` runs migration checks. Full financial experiments, agent tournaments and GUI sessions were not rerun.
