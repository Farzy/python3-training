"""My training scripts

    I use this project to practice on Python 3.8.

    Author: Farzad FARID

    References:
        - Python 3.8 tutorial
        - Python 3.8 library
        - Python 3.8 reference
"""


def strings():
    """Training on strings"""
    print("{0}, {1}, {2}".format('a', 'b', 'c'))
    print("{}, {}, {}".format('a', 'b', 'c'))
    print("{1}, {0}, {2}".format('a', 'b', 'c'))
    print("{2}, {1}, {0}".format(*'abc'))
    print("{0}{1}{0}".format('abra', 'cad'))


def main():
    """The main program call the training sessions"""
    strings()


if __name__ == '__main__':
    main()
