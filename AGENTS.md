# Python 3 Training

## Project Overview

This is a personal project for practicing Python 3. It contains a collection of Python scripts with examples and exercises covering various features of the language. The project is structured to allow for easy execution of individual or all exercises.

**Main technologies:**

*   Python 3
*   Dependencies:
    *   `bs4` (Beautiful Soup)
    *   `requests`
    *   `matplotlib`

**Architecture:**

*   `training.py`: The main script to run the exercises.
*   `exercices.py`: Contains all the exercise functions.
*   `codewars/`: Contains solutions to Codewars katas.
*   `brilliant/`: Contains exercises from Brilliant.org.

## Building and Running

No build is needed. The main program can be run directly.

**Running all exercises:**

```bash
python3 training.py
```

**Running a specific exercise:**

To see the list of available exercises, run:

```bash
python3 training.py --list
```

To run a specific exercise, for example, `strings`:

```bash
python3 training.py strings
```

## Testing

The project includes some tests in `exercices.py`. To run them:

```bash
python3 exercices.py -v
```

## Development Conventions

*   The code follows the standard Python conventions (PEP 8).
*   The project uses `uv` for package and dependency management, with configuration in `pyproject.toml`.
