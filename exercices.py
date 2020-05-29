"""All exercices go in this file.
"""

import datetime
import sys
from time import sleep
from collections import deque


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

    c = 3 - 5j
    print("The complex number {0} if formed of the real part {0.real} and the imaginary part {0.imag}".format(c))

    class Point:
        """
        Test class for __str__ implementation
        """

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
    # noinspection PyStringFormat
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
    # noinspection PyUnusedLocal
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

    def fib2(m):
        """Return a list containing the Fibonacci series up to n"""

        result = []
        a, b = 1, 1
        while a < m:
            result.append(a)
            a, b = b, a + b
        return result

    n = 10000
    r = fib2(n)
    print(f'fib2(n) = {r}')

    def change_param(a, b):
        """
        Modify parameter "a" which is an object.

        "b", which is an integer, cannot be changed.

        :param a:
        :param b:
        :return:
        """
        a.append('Gotcha!')
        b += 1

    arr = ['a', 'b']
    num = 42
    print(f"Before call to change_param: arr: {arr}, num: {num}")
    change_param(arr, num)
    print(f"After call to change_param: arr: {arr}, num: {num}")

    # Test default values
    # noinspection PyDefaultArgument
    def test_cache(a, _cache=[]):
        """Simulate a very basic (and WRONG) memoizing function"""
        if len(_cache) == 0:
            # Do lenghty calculation
            print("In test_cache, doing calculation…")
            sleep(1)
            _cache.append(42 + a)
        return _cache[0]

    print(f"Calling test_cache once: {test_cache(2)}")
    print(f"Calling test_cache twice: {test_cache(3)}")

    # Keyword arguments
    # noinspection PyShadowingBuiltins
    def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
        """Test keyword arguments"""

        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it.")
        print("-- Lovely plumage, the", type)
        print("-- it's", state, "!")

    parrot(1000)
    parrot(voltage=1000)
    parrot(voltage=100000, action='VOOOOM')
    parrot(action='VOOOOM', voltage=100000)
    parrot('a million', 'beref of life', 'jump')
    parrot('a thousand', state='pushing up the daisies')

    # parrot()
    # parrot(voltage=5.0, 'dead')
    # parrot(110, voltage=220)
    # parrot(actor='John Cleese')

    def cheeseshop(kind, *arguments, **keywords):
        """
        Test keyword arguments and array.

        :param kind:
        :param arguments:
        :param keywords:
        :return:
        """

        print("-- Do you have any", kind, "?")
        print("-- I'm sorry, we're all out of", kind)
        for arg in arguments:
            print(arg)
        print("-" * 40)
        for kw in keywords:
            print(kw, ":", keywords[kw])

    cheeseshop("Limburger", "It's very runny, sir",
               "It's really very, VERY runny, sir.",
               shopkeeper="Michael Palin",
               client="John Cleese",
               sketch="Cheese Shop Sketch")

    def standard_arg(arg):
        """Test positional or keyword argument"""

        print(arg)

    def pos_only_arg(arg, /):
        """Test positional only argument"""

        print(arg)

    def kwd_only_arg(*, arg):
        """Test keyword only argument"""

        print(arg)

    def combined_example(pos_only, /, standard, *, kwd_only):
        """Combine all 3 types"""

        print(pos_only, standard, kwd_only)

    standard_arg("Test standard_arg")
    standard_arg(arg="Test standard_arg")
    pos_only_arg("Test pos_only_arg")
    # pos_only_arg(arg="Test pos_only_arg")
    # kwd_only_arg("Test kwd_only_arg")
    kwd_only_arg(arg="Test kwd_only_arg")
    # combined_example("Test combined_example 1",
    #                  "Test combined_example 2",
    #                  "Test combined_example 3")
    combined_example("Test combined_example 1",
                     "Test combined_example 2",
                     kwd_only="Test combined_example 3")
    combined_example("Test combined_example 1",
                     standard="Test combined_example 2",
                     kwd_only="Test combined_example 3")

    # combined_example(post_only="Test combined_example 1",
    #                  standard="Test combined_example 2",
    #                  kwd_only="Test combined_example 3")

    # noinspection PyUnusedLocal
    def foo(name, **kwargs):
        """Test keyword arguments"""

        return 'name' in kwargs

    # noinspection PyUnusedLocal
    def foo2(name, /, **kwargs):
        """Test keyword arguments"""

        return 'name' in kwargs

    # This won't work because "name" always bind to the first argument and
    # cannot be reuse as a keyword argument
    try:
        foo('toto', **{'name': 42, 'z': 0})
    except TypeError:
        pass

    # This works because in foo2() we're forcing the first parameter to
    # be positional only
    foo2('toto', **{'name': 42, 'z': 0})

    # Unpacking argument lists
    print("Range: ", list(range(3, 6)))  # Normal call with separate arguments
    args = [3, 6]
    print("Range: ", list(range(*args)))  # Call with arguments unpacked from a list
    try:
        args = [3, 6, 42, 27]
        print("Range: ", list(range(*args)))  # Won't work: too many arguments
    except TypeError:
        pass

    # Same with dictionary
    d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
    parrot(**d)

    # Lambda
    pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
    print("Pairs before sorting: ", pairs)
    pairs.sort(key=lambda pair: pair[1])
    print("Pairs after sorting with lambda", pairs)

    # Call annotated function
    func_annotations('spam')
    # These would hint warnings in IntelliJ
    # func_annotations(42)
    # x = func_annotations('bacon') + 4


# Function Annotations
def func_annotations(ham: str, eggs: str = 'eggs') -> str:
    """
    Test Function Annotations

    :param ham: Some Ham
    :param eggs: Some eggs
    :return: Delicious breakfast
    """
    print("Annotations: ", func_annotations.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


def data_structures():
    """
    Experiment with data structures: list, tuple, array, set…

    :return:
    """

    a = []
    print("Empty list:", a)
    a.append(1)
    print("Append 1:", a)
    a.extend(range(2, 20))
    print("Extend by a range:", a)
    a.insert(10, 42)
    print("Insert 42 in position 10:", a)
    a.remove(10)
    print("Remove number 10:", a)
    n = a.pop(12)
    print("Pop", n, "at position 12:", a)
    a.clear()
    print("Clear:", n)
    a = [10, 42, -5, 0, 3, 7, 9, 42]
    print("Recreate:", a)
    n = a.index(42, 2)
    print("Found 42 from slice [2:] at position", n, ":", a)
    n = a.count(42)
    print("Found 42", n, "times in the list:", a)
    a.sort(reverse=True)
    print("Reverse sort:", a)
    a.reverse()
    print("Reverse", a)
    b = a.copy()
    print("b is a copy():", b, ". id(a) =", id(a), "but id(b) =", id(b))
    c = a
    print("But c=a IS a", ". id(a) =", id(a), "and id(c) =", id(c))

    # Queue
    queue = deque(['Eric', 'John', 'Michael'])
    print(queue)
    queue.append("Terry")
    queue.append("Graham")
    print(queue)
    print(queue.popleft())
    print(queue.popleft())
    print(queue)

    # List comprehensions

    print("List comprehensions:")
    x = 42
    squares = []
    for x in range(10):
        squares.append(x ** 2)
    print("Unnecessary variable 'x' remains and erased previous value: ", x)
    print("squares:", squares)
    squares = list(map(lambda x: x ** 2, range(10)))
    print("squares:", squares)
    squares = [x ** 2 for x in range(10)]
    print("squares:", squares)

    # The loop are embedded in the order they are written.
    # Here the "y" loops continuously between each "x" loop.
    a = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    print(a)

    # Simulate map() in better
    vec = [-4, -2, 0, 2, 4]
    print("vec:", vec)
    print("vec * 2:", [x * 2 for x in vec])

    # Implement filter()
    print("filter vec >= 0:", [x for x in vec if x >= 0])

    # apply a function
    print("abs(vec):", [abs(x) for x in vec])

    # Call a method on each element
    freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
    print("Fruits:", freshfruit)
    print("Fruits stripped:", [fruit.strip() for fruit in freshfruit])

    # Create a list of 2-tuples from a range
    print("2-tuples from a range:", [(x, x ** 3) for x in range(6)])
    # This won't work
    # [x, x**3 for x in range(6)]

    # Flatten a list using a listcomp with 2 'for'
    vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Flatten list:", [num for elem in vec for num in elem])

    # Nested list comprehensions
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    print("Matrix:", matrix)
    print("Transposed matrix", [[row[i] for row in matrix] for i in range(4)])
    print("Transposed matrix with zip:", list(zip(*matrix)))

    # Tuples
    empty = ()
    singleton = "one",
    print("empty tuple:", empty)
    print("singleton tuple:", singleton)
    t = tuple(range(5))
    print("tuple:", t)
    a, b, c, d, e = t
    print("unpacked tuple:", a, b, c, d, e)

    # Sets
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print("set:", basket)
    print("orange in basket:", 'orange' in basket)
    print("crabgrass in basket:", 'crabgrass' in basket)

    a = set('abracadabra')
    b = set('alacazam')
    print("sets a & b:", a, "&", b)
    print("a - b:", a - b)
    print("a | b", a | b)
    print("a & b", a & b)
    print("a ^ b", a ^ b)

    # Set comprehensions
    a = {x for x in 'abracadabra' if x not in 'abc'}
    print("Set comprehension result:", a)

    # Dictionnary
    tel = {'jack': 4098, 'sape': 4139}
    print("dict:", tel)
    tel['guido'] = 4127
    print("add to dict:", tel)
    del tel['sape']
    print("delete 'sape' from dict", tel)
    tel['irv'] = 4127
    print("add irv to dict", tel)
    print("dict keys in order:", list(tel))
    print("dict keys sorted:", sorted(tel))
    print("'guido' in dict:", 'guido' in tel)
    print("'sape' in dict:", 'sape' in tel)

    print("dict from tuples:", dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

    print("dict comprehension", {x: x ** 2 for x in range(6)})

    # Looping
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k, v)

    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)

    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print("What is your {0}?  It is {1}".format(q, a))

    for i in reversed(range(1, 10, 2)):
        print(i)

    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print(f)


def exceptions():
    """Experiment with exceptions"""

    class B(Exception):
        pass

    class C(B):
        pass

    class D(C):
        pass

    print("Catch exception in the correct order:")
    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print("Caught exception D.")
        except C:
            print("Caught exception C.")
        except B:
            print("Caught exception B.")

    print("\nRevert the 'except:' order:")
    for cls in [B, C, D]:
        try:
            raise cls()
        except B:
            print("Caught exception B.")
        except C:
            print("Caught exception C.")
        except D:
            print("Caught exception D.")

    print("\nRaise first exception:")
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print(f"OS error: {err}")
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info())
        raise

    print("\nRaise second exception:")
    try:
        f = open('fibo.py')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print(f"OS error: {err}")
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info())
        raise

    print("\nRaise third exception:")
    try:
        f = open('fibo.py')
        s = f.readline()
        i = 1 / 0
    except OSError as err:
        print(f"OS error: {err}")
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info())
        # raise

    print("\nArguments to Exceptions:")
    try:
        raise Exception('spam', 'eggs')
    except Exception as inst:
        print("Type:", type(inst))
        print("Args:", inst.args)
        print("Exception:", inst)
        x, y = inst.args
        print("x = ", x)
        print("y = ", y)

    class Error(Exception):
        """Base class for exceptions in this module"""
        pass

    class InputError(Error):
        """Exception raised for errors in input

        Attributes:
            expression -- input expression in which the error occurred
            message -- explanation of the error
        """

        def __init__(self, expression, message):
            self.expression = expression
            self.message = message

    class TransitionError(Error):
        """Raised when an operation attemps a state transition that's not
        allowed.

        Attributes:
            previous -- state at beginning of transition
            next -- attempted new state
            message -- explanation of why the specific transition is not allowed
        """

        def __init__(self, previous, next, message):
            self.previous = previous
            self.next = next
            self.message = message

    print("\nFinally:")
    try:
        try:
            raise KeyboardInterrupt
        finally:
            print('Goodbye, world!')
    except BaseException:
        pass

    def bool_return():
        """The "finally" return statement override the main one."""
        try:
            return True
        finally:
            return False
    assert bool_return() == False

    def divide(x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            print("Division by zero!")
        else:
            print("Result is", result)
        finally:
            print("Executing finally clause")
    divide(2, 1)
    divide(2, 0)
    try:
        divide("2", "1")
    except TypeError as e:
        print("Caught exception:", e)

def scopes():
    """Experiment with scopes"""
    def scope_test():
        def do_local():
            spam = "local spam"

        def do_nonlocal():
            nonlocal spam
            spam = "nonlocal spam"

        def do_global():
            global spam
            spam = "global spam"

        spam = "test spam"
        do_local()
        print("After local assignment:", spam)
        do_nonlocal()
        print("After nonlocal assignment:", spam)
        do_global()
        print("After global assignment:", spam)

    scope_test()
    print("In global scope:", spam)
