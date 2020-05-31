"""My training scripts

    I use this project to practice on Python 3.8.

    Author: Farzad FARID

    References:
        - Python 3.8 tutorial
        - Python 3.8 library
        - Python 3.8 reference
"""
import sys
import argparse
import exercices

VERSION = '1.0'


def get_modules():
    """Return the list of all exercice modules with a short description"""

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

    modules = {}
    for func_name in functions:
        f = getattr(exercices, func_name)  # Function object
        name = f.__name__  # Function name
        doc = (f.__doc__.strip() or "NO DOCUMENTATION").splitlines()[0]  # First line of function documentation
        modules[name] = doc

    return modules


def main():
    """The main program calls the training sessions

    This function uses Python's introspection in order to extract the list of
    functions from the "exercises" module.
    """

    parser = argparse.ArgumentParser(prog="python3-training",
                                     description="My Python 3 traning sessions")
    parser.add_argument('module', nargs='?', default=None,
                        help='Execute only one module by name')
    parser.add_argument('-l', '--list', action='store_true',
                        help='Display list of modules')
    parser.add_argument('--version', action='version', version=f'{parser.prog} {VERSION}')
    args = parser.parse_args()

    # Basic argument parsing
    if args.list:
        modules = get_modules()
        for name in modules:
            print(f"{name:<15} -- {modules[name]}")
        sys.exit(1)

    modules = get_modules()
    if args.module:
        try:
            modules = {args.module: modules[args.module]}  # Reduce dict to one element
        except KeyError:
            sys.stderr.write(
                f"Error: Unknown module {args.module}. Check module list with '{parser.prog} --list'.\n")
            sys.exit(1)

    print("List of exercises:")
    for name in modules:
        f = getattr(exercices, name)  # Function object
        title = name.capitalize()  # Function name
        doc = modules[name]
        title_length = len(title) + len(doc)
        print()
        print("+" + "-" * (title_length + 4) + "+")
        print(f"| {title}: {doc} |")
        print("+" + "-" * (title_length + 4) + "+")
        print()

        try:
            f()
        except TypeError:
            print("Ignoring error for this function. It should not be called directly.")


if __name__ == '__main__':
    main()
