"""My training scripts

    I use this project to practice on Python 3.8.

    Author: Farzad FARID

    References:
        - Python 3.8 tutorial
        - Python 3.8 library
        - Python 3.8 reference
"""
from sys import argv
import exercices


def main():
    """The main program calls the training sessions

    This function uses Python's introspection in order to extract the list of
    functions from the "exercises" module.
    """

    # Basic argument parsing
    if len(argv) > 1:
        functions = [argv[1]]
    else:
        # Extract functions whose name does not start with '_' from module
        functions = filter(
            lambda sym: type(getattr(exercices, sym)) == type(main) and not sym.startswith('_'),
            dir(exercices)
        )
        functions = list(functions)
        # Do the same with list comprehension
        functions2 = [
            sym for sym in dir(exercices)
            if type(getattr(exercices, sym)) == type(main) and not sym.startswith('_')
        ]
        assert functions == functions2

    print("List of exercises:")
    for func_name in functions:
        f = getattr(exercices, func_name)  # Function object
        name = f.__name__.capitalize()  # Function name
        doc = (f.__doc__ or "NO DOCUMENTATION").splitlines()[0]  # First line of function documentation
        title_length = len(name) + len(doc)
        print()
        print("+" + "-" * (title_length + 4) + "+")
        print(f"| {name}: {doc} |")
        print("+" + "-" * (title_length + 4) + "+")
        print()

        try:
            f()
        except TypeError:
            print("Ignoring error for this function. It should not be called directly.")


if __name__ == '__main__':
    main()
