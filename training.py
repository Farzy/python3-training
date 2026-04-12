"""My training scripts

    I use this project to practice on Python 3.8.

    Author: Farzad FARID

    References:
        - Python 3.8 tutorial
        - Python 3.8 library
        - Python 3.8 reference

Copyright 2020 Farzad FARID

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys
import click
import types
import exercices

VERSION = "1.0"


def get_modules():
    """Return the list of all exercice modules with a short description"""

    # Extract functions whose name does not start with '_' from module
    functions = filter(
        lambda sym: isinstance(getattr(exercices, sym), types.FunctionType)
        and not sym.startswith("_"),
        dir(exercices),
    )
    functions = list(functions)
    # Do the same with list comprehension
    functions2 = [
        sym
        for sym in dir(exercices)
        if isinstance(getattr(exercices, sym), types.FunctionType)
        and not sym.startswith("_")
    ]
    assert functions == functions2

    modules = {}
    for func_name in functions:
        f = getattr(exercices, func_name)  # Function object
        name = f.__name__  # Function name
        doc = (f.__doc__.strip() or "NO DOCUMENTATION").splitlines()[
            0
        ]  # First line of function documentation
        modules[name] = doc

    return modules


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.argument("module", required=False)
@click.option(
    "--list", "-l", "list_modules", is_flag=True, help="Display list of modules"
)
@click.version_option(VERSION, "--version", prog_name="python3-training")
def main(module, list_modules):
    """The main program calls the training sessions

    This function uses Python's introspection in order to extract the list of
    functions from the "exercises" module.
    """

    # Basic argument parsing
    if list_modules:
        modules = get_modules()
        for name in modules:
            print(f"{name:<15} -- {modules[name]}")
        sys.exit(1)

    modules = get_modules()
    if module:
        try:
            modules = {module: modules[module]}  # Reduce dict to one element
        except KeyError:
            click.echo(
                f"Error: Unknown module {module}. Check module list with 'python3-training --list'.",
                err=True,
            )
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

        f()  # Let exceptions happen


if __name__ == "__main__":
    main()
