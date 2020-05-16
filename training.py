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

    functions = [
        exercices.strings,
        exercices.lists,
        exercices.fib,
    ]

    print("List of exercices:")
    for f in functions:
        name = f.__name__.capitalize()
        doc = f.__doc__.splitlines()[0]
        title_length = len(name) + len(doc)
        print()
        print("+" + "-" * (title_length + 4) + "+")
        print(f"| {name}: {doc} |")
        print("+" + "-" * (title_length + 4) + "+")
        print()

        f()


if __name__ == '__main__':
    main()
