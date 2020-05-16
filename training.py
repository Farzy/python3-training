"""My training scripts

    I use this project to practice on Python 3.8.

    Author: Farzad FARID

    References:
        - Python 3.8 tutorial
        - Python 3.8 library
        - Python 3.8 reference
"""

import exercices


def main():
    """The main program calls the training sessions"""

    # Extract functions whose name does not start with '_' from module
    functions = filter(
        lambda s: type(getattr(exercices, s)) == type(main) and not s.startswith('_'),
        dir(exercices)
    )

    print("List of exercises:")
    for func_name in functions:
        f = getattr(exercices, func_name)   # Function object
        name = f.__name__.capitalize()      # Function name
        doc = f.__doc__.splitlines()[0]     # First line of function documentation
        title_length = len(name) + len(doc)
        print()
        print("+" + "-" * (title_length + 4) + "+")
        print(f"| {name}: {doc} |")
        print("+" + "-" * (title_length + 4) + "+")
        print()

        f()


if __name__ == '__main__':
    main()
