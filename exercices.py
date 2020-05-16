"""All exercices go in this file.
"""

import datetime
import math

def strings():
    """Training on strings

    Reference: https://docs.python.org/3/tutorial/introduction.html#strings
    """

    print("{0}, {1}, {2}".format('a', 'b', 'c'))
    print("{}, {}, {}".format('a', 'b', 'c'))
    print("{1}, {0}, {2}".format('a', 'b', 'c'))
    print("{2}, {1}, {0}".format(*'abc'))
    print("{0}{1}{0}".format('abra', 'cad'))

    print("Coordinates: {latitude}, {longitude}".format(latitude='37.24N', longitude='-115.81W'))
    coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
    print("Coordinates: {latitude}, {longitude}".format(**coord))

    c = 3-5j
    print("The complex number {0} if formed of the real part {0.real} and the imaginary part {0.imag}".format(c))

    class Point:
        def __init__(self, x, y):
            self.x, self.y = x, y

        def __str__(self):
            return "Point({self.x}, {self.y})".format(self=self)

    p = Point(2, 3)
    print("Object {0!r} = {0}".format(p))

    coord = (3, 5)
    print('X: {0[0]};  Y: {0[1]}'.format(coord))

    print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))

    print('{:<30}'.format('left aligned'))
    print('{:>30}'.format('right aligned'))
    print('{:^30}'.format('centered'))
    print('{:*^30}'.format('centered'))  # use '*' as a fill char

    print('{:+f}, {:+f}'.format(3.14, -3.14))
    print('{: f}, {: f}'.format(3.14, -3.14))
    print('{:-f}, {:-f}'.format(3.14, -3.14))

    print('int: {0:d}, hex: {0:08x}, oct: {0:o}, bin: {0:010b}'.format(42))
    print('int: {0:#d}, hex: {0:#08x}, oct: {0:#o}, bin: {0:#010b}'.format(42))

    print('{:,}'.format(1234567890))
    print('{:_}'.format(1234567890))  # IntelliJ complains but this format is supported

    point = 19
    total = 22
    print('Correct answers: {:.2%}'.format(point / total))

    d = datetime.datetime(2010, 7, 14, 12, 15, 58)
    print('{:%Y-%m-%d %H:%M:%S}'.format(d))

    for align, text in zip('<^>', ['left', 'center', 'right']):
        print('{0:{fill}{align}16}'.format(text, fill=align, align=align))

    octets = [192, 168, 0, 1]
    print('{:02X}.{:02X}.{:02X}.{:02X}'.format(*octets))

    width = 6
    for num in range(5, 20):
        for base in 'dXob':
            print('{0:{width}{base}}'.format(num, width=width, base=base), end=' ')
        print()


def lists():
    """Traning on lists

    Reference: https://docs.python.org/3/tutorial/introduction.html#lists
    """

    squares = [1, 4, 9, 16, 25]
    # Shallow copy
    squares_copy = squares[:]

    cubes = [1, 8, 27, 65, 125]
    cubes[3] = 64
    cubes.append(216)
    cubes.append(7 ** 3)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letters)
    letters[2:5] = ['C', 'D', 'E']
    print(letters)
    letters[2:5] = []
    print(letters)
    # Clear list
    letters[:] = []
    print(letters)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(f"Len {letters} = {len(letters)}")


def fib():
    """Fibonacci numbers

    Reference: https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming
    """

    a, b = 0, 1
    while a < 100:
        a, b = b, a + b
        print(a, end=', ')
    print()


def iterators():
    """Some iterators"""

    # Get a list out of an iterator
    r = range(0, 10)
    print(f"Range as iterator = {r}")
    print(f"Range as list = {list(r)}")


def control_structures():
    """Test some features of control structures

    Reference: https://docs.python.org/3.8/tutorial/controlflow.html
    """

    # "else"
    for n in range(2, 20):
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                print(f"{i} is a divisor of {n}.")
                break
        else:
            print(f"{n} is a prime number!")
