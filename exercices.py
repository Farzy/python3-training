"""All exercices go in this file.

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
    """Training on lists

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
            # Do lengthy calculation
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
    _func_annotations('spam')
    # These would hint warnings in IntelliJ
    # func_annotations(42)
    # x = func_annotations('bacon') + 4


# Function Annotations
def _func_annotations(ham: str, eggs: str = 'eggs') -> str:
    """
    Test Function Annotations

    :param ham: Some Ham
    :param eggs: Some eggs
    :return: Delicious breakfast
    """
    print("Annotations: ", _func_annotations.__annotations__)
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
    squares = list(map(lambda xx: xx ** 2, range(10)))  # If x was used here, it would shadow the main x
    print("squares:", squares)
    squares = [yy ** 2 for yy in range(10)]  # If x was used here, it would shadow the main x
    print("squares:", squares)
    assert x == 9

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

    # Dictionary
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
        """B derives from Exception"""
        pass

    class C(B):
        """C derives from C"""
        pass

    class D(C):
        """D derives from C"""
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
    # noinspection PyBroadException
    try:
        f = open('myfile.txt')
        s = f.readline()
        _i = int(s.strip())
    except OSError as err:
        print(f"OS error: {err}")
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info())
        raise

    print("\nRaise second exception:")
    # noinspection PyBroadException
    try:
        f = open('fibo.py')
        s = f.readline()
        _i = int(s.strip())
    except OSError as err:
        print(f"OS error: {err}")
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info())
        raise

    print("\nRaise third exception:")
    # noinspection PyBroadException
    try:
        f = open('fibo.py')
        _s = f.readline()
        _i = 1 / 0
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

    # noinspection PyUnusedLocal
    class InputError(Error):
        """Exception raised for errors in input

        Attributes:
            expression -- input expression in which the error occurred
            message -- explanation of the error
        """

        def __init__(self, expression, message):
            self.expression = expression
            self.message = message

    # noinspection PyUnusedLocal
    class TransitionError(Error):
        """Raised when an operation attempts a state transition that's not
        allowed.

        Attributes:
            previous -- state at beginning of transition
            next -- attempted new state
            message -- explanation of why the specific transition is not allowed
        """

        # noinspection PyShadowingBuiltins
        def __init__(self, previous, next, message):
            self.previous = previous
            self.next = next
            self.message = message

    print("\nFinally:")
    # noinspection PyBroadException
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
    assert not bool_return()

    # noinspection PyShadowingNames
    def divide(x, y):
        """Test all try syntaxes"""
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
        # noinspection PyTypeChecker
        divide("2", "1")
    except TypeError as e:
        print("Caught exception:", e)


def scopes():
    """Experiment with scopes"""
    def scope_test():
        """Test and compare scopes"""
        # noinspection PyShadowingNames
        def do_local():
            """Create a variable in the local scope"""
            # noinspection PyUnusedLocal
            spam = "local spam"

        def do_nonlocal():
            """Create a variable in the non-local scope"""
            nonlocal spam
            spam = "nonlocal spam"

        def do_global():
            """Create a global variable"""
            # noinspection PyGlobalUndefined
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
    # noinspection PyUnboundLocalVariable
    print("In global scope:", spam)


def classes():
    """Class manipulation"""

    # A class created in an "if" is available outside of the test
    a = 1
    if a == 1:
        class Foo:
            """Class create in an if branch"""
            pass
    else:
        print("No class Foo!")

        class Bar:
            """Class never created"""
            pass

    # noinspection PyUnboundLocalVariable
    _x = Foo()
    print("Class Foo, defined in an executed branch of 'if' exists.")

    try:
        # noinspection PyUnboundLocalVariable,PyUnusedLocal
        y = Bar()
    except UnboundLocalError:
        print("Class Bar, defined in a dead branch of 'if', does not exist.")
    else:
        print("Should not happen!")

    class ExecutableStatement:
        """Execute statements during class creation"""
        def __init__(self):
            print("Class ExecutableStatement instantiated!")
            print("namespace content in __init__:", dir())

        print("Class ExecutableStatement declared! __init__ declared!")
        print("namespace content in ExecutableStatement:", dir())
        es_a = 1
        print("'es_a' declared in class!")
        print("namespace content in ExecutableStatement:", dir())

    # noinspection PyUnusedLocal
    es = ExecutableStatement()
    print("namespace content after instantiating 'es':", dir())

    class MyClass:
        """A simple example class"""
        i = 12345

        def __init__(self):
            self.data = []

        # noinspection PyMethodMayBeStatic
        def f(self):
            """Simple method"""
            return "hello world"

    x = MyClass()
    print("MyClass x =", x)
    print("dir(x) = ", dir(x))
    print("MyClass.__doc__ =", MyClass.__doc__)
    print("MyClass.i =", MyClass.i)
    print("MyClass.f =", MyClass.f)
    print("x.i =", x.i)
    print("x.f =", x.f)
    print("x.f() =", x.f())

    print("Add an attribute 'counter' to instance object x.")
    x.counter = 1
    assert hasattr(x, "counter") is True
    while x.counter < 10:
        x.counter = x.counter * 2
    print("x.counter =", x.counter)
    del x.counter
    assert hasattr(x, "counter") is False

    class Complex:
        """A class with initialisation parameters"""
        def __init__(self, realpart, imagpart):
            self.r = realpart
            self.i = imagpart

    y = Complex(3.0, -4.5)
    print("Complex y =", y)
    print("dir(y) = ", dir(y))

    class Dog:
        """A class with class variables and instance variables"""

        kind = 'canine'

        def __init__(self, name):
            self.name = name

    d = Dog('Fido')
    e = Dog('Buddy')
    print("Dog d = ", d)
    print("Dog e = ", e)
    print("d.kind = ", d.kind)
    print("e.kind = ", e.kind)
    print("d.name = ", d.name)
    print("e.name = ", e.name)

    del d, e, Dog

    class Dog:
        """A bad use of class variable"""

        tricks = []

        def __init__(self, name):
            self.name = name

        def add_trick(self, trick):
            """Add trick to dog… or to class Dog"""
            self.tricks.append(trick)

    d = Dog('Fido')
    e = Dog('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')
    print("Bad Dog: d.tricks = ", d.tricks)
    del d, e, Dog

    class Dog:
        """A good use of class variable"""

        def __init__(self, name):
            self.tricks = []
            self.name = name

        def add_trick(self, trick):
            """Add trick to dog"""
            self.tricks.append(trick)

    d = Dog('Fido')
    e = Dog('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')
    print("Good Dog: d.tricks = ", d.tricks)
    print("Good Dog: e.tricks = ", e.tricks)

    # Function defined outside the class
    # noinspection PyShadowingNames,PyUnusedLocal
    def f1(self, x, y):
        """This function will be used as a method"""
        return min(x, x+y)

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    class C:
        """Demonstrate that a method body can be outside of class"""
        f = f1

        def g(self):
            """Sample method"""
            return 'hello world'

        h = g

    # noinspection PyUnusedLocal
    class Bag:
        """Methods can call other methods"""
        def __init__(self):
            self.data = []

        # noinspection PyShadowingNames
        def add(self, x):
            """Add data once"""
            self.data.append(x)

        # noinspection PyShadowingNames
        def addtwice(self, x):
            """Add data twice"""
            self.add(x)
            self.add(x)

    # Inheritance
    class BaseClass:
        """Base class for inheritance"""

        def f(self):
            """Method in base class, can be overloaded"""
            print("This is method 'f' in BaseClass, object =", self)

        def call_b(self):
            """This method from base class can call method from derived class"""
            print("This method, declared in BaseClass, calls a method that is overloaded in DerivedClass")
            self.b()

        def b(self):
            """Placeholder in base class"""
            raise Exception("Should not happen")

    class DerivedClass(BaseClass):
        """Derived class to demonstrate virtual methods"""

        def f(self):
            """This method overrides the one from base class"""
            print("This is method 'f' in DerivedClass, object =", self)
            print("  Now calling 'f' from parent class…")
            BaseClass.f(self)

        def b(self):
            """This method is called by a base class method"""
            print("This is method 'b' in DerivedClass")

    x = BaseClass()
    x.f()
    y = DerivedClass()
    y.f()
    y.call_b()
    # noinspection PyBroadException
    try:
        x.call_b()
    except Exception:
        pass

    assert isinstance(x, BaseClass)
    assert not isinstance(x, DerivedClass)
    assert isinstance(y, BaseClass)
    assert isinstance(y, DerivedClass)

    assert issubclass(DerivedClass, BaseClass)
    assert not issubclass(BaseClass, DerivedClass)
    assert issubclass(BaseClass, object)

    class Reverse:
        """Iterator for looping over q sequence"""
        def __init__(self, data):
            self.data = data
            self.index = len(data)

        def __iter__(self):
            return self

        def __next__(self):
            if self.index == 0:
                raise StopIteration
            self.index -= 1
            return self.data[self.index]

    rev = Reverse('spam')
    print("iter(rev) =", iter(rev))
    for char in rev:
        print(char)

    def reverse(data):
        """Generator function"""
        for index in range(len(data)-1, -1, -1):
            yield data[index]

    for char in reverse('golf'):
        print(char)


def stdlib_tour():
    """A brief tour of the Standard Library"""

    import os

    curdir = os.getcwd()
    pid = str(os.getpid())
    print("Current dir:", curdir)
    os.chdir('/tmp')
    print("New current dir:", os.getcwd())
    os.system('touch python3-tutorial-' + pid)
    print("Our files in /tmp:", [file for file in os.listdir('/tmp') if 'python3' in file])

    import shutil
    shutil.copyfile('python3-tutorial-' + pid, 'copy-python3-tut-' + pid)
    print("Our files with current pid in /tmp:", [file for file in os.listdir('/tmp') if pid in file])
    print("Rename a file")
    shutil.move('python3-tutorial-' + pid, 'old-python3-tutorial-' + pid)

    import glob
    print("Same list with glob():", glob.glob(f"*{pid}"))

    os.chdir(curdir)

    # Regex
    import re

    s = 'which foot or hand fell fastest'
    fwords = re.findall(r'\bf[a-z]*', s)
    print(f"f-words in '{s}: {fwords}")
    s2 = 'cat in the the hat'
    s2_fixed = re.sub(r'(\b[a-z]+) \1', r'\1', s2)
    print(f"Remove redundant words in '{s2}': {s2_fixed}")

    import random

    choice = random.choice(['apple', 'pear', 'banana'])
    print("Random fruit from a choice:", choice)
    sample = random.sample(range(100), 10)  # Sampling without replacement
    print("Sampling without replacement:", sample)
    print("Random float:", random.random())
    print("Random integer from a range of 6:", random.randrange(6))

    import statistics

    data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    print("Data:", data)
    print("Mean:", statistics.mean(data))
    print("Median:", statistics.median(data))
    print("Variance:", statistics.variance(data))

    from urllib.request import urlopen

    with urlopen('https://farzy.org/fr/') as response:
        for line in response:
            line = line.decode('utf-8')
            print(line)

    # import smtplib
    # server = smtplib.SMTP('in1-smtp.messagingengine.com.')
    # server.sendmail('farzad.farid@gmail.com', 'farzy@farzy.org',
    #                 'To: farzy@farzy.org\n' \
    #                 'From: farzad.farid@gmail.com\n' \
    #                 'Subject: Test email\n' \
    #                 '\n' \
    #                 'Beware the Ides of March.')
    # server.quit()

    from datetime import date

    now = date.today()
    print("Now: ", now)
    now_str = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
    print("Now: ", now_str)
    birthday = date(1970, 4, 3)
    age = now - birthday
    print(f"I am {age} days old.")

    import zlib

    s = b'witch which has which witches wrist watch'
    print(f"Len of {s} is {len(s)}")
    t = zlib.compress(s)
    print(f"Len of compressed string {t} is {len(t)}")
    assert s == zlib.decompress(t)
    print("CRC32: ", zlib.crc32(s))

    from timeit import Timer

    t1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
    t2 = Timer('a,b = b,a', 'a=1; b=2').timeit()
    print(f"Timing comparison of classic swap ({t1}) vs tuple swap ({t2}")


def stdlib_tour2():
    """Second tour of the Standard Library"""

    import reprlib
    s = set('supercalifragilisticexpialidocious')
    print("Repr of a long Set:", s)
    print("Customized repr of a long Set:", reprlib.repr(s))
    print(stdlib_tour)
    print(reprlib.repr(stdlib_tour))

    import pprint

    t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
    print("t=", t)
    print("Now pretty printing t on 30 columns:")
    pprint.pprint(t, width=30)
    print("repr(t) =", reprlib.repr(t))

    import textwrap
    doc = """The wrap() method is just like fill() except that it returns
    a list of strings instead of one big string with newlines to separate
    the wrapped lines."""
    print("Long text: ", doc)
    print("Textwrapped on 40 columns:")
    print(textwrap.fill(doc, width=40))
    print(textwrap.wrap(doc, width=40))

    import struct

    with open('myfile.zip', 'rb') as f:
        data = f.read()

    start = 0
    for i in range(3):                      # Show the first 3 file headers
        start += 14
        fields = struct.unpack('<IIIHH', data[start:start+16])
        crc32, comp_size, uncomp_size, filesizename, extra_size = fields

        start += 16
        filename = data[start:start+filesizename]
        start += filesizename
        _extra = data[start:start+extra_size]
        print(f"Zip file #{i+1}: filename {filename}, "
              f"crc32: {hex(crc32)}, compressed size: {comp_size}, "
              f"uncompressed size: {uncomp_size}")

        start += extra_size + comp_size     # Skip to the next header

    import threading, zipfile

    class AsyncZip(threading.Thread):
        """Asynchronous file zipper"""

        def __init__(self, infile, outfile):
            threading.Thread.__init__(self)
            self.infile = infile
            self.outfile = outfile

        def run(self):
            f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
            f.write(self.infile)
            f.close()
            print("Finished background zip of:", self.infile)

    background = AsyncZip('exercices.py', 'myarchive.zip')
    background.start()
    print("The main program continues to run in foreground.")

    background.join()  # Wait for the background task to finish
    print("Main program waited until background was done.")


    import logging

    logging.debug("Debugging information")
    logging.info("Informational message")
    logging.warning("Warning: config file %s not found", 'server.conf')
    logging.error("Error occured")
    logging.critical("Critical error -- shutting down")

    import weakref, gc

    class A:
        def __init__(self, value):
            self.value = value

        def __repr__(self):
            return str(self.value)

    a = A(10)                           # Create a reference
    d = weakref.WeakValueDictionary()
    d['primary'] = a                    # does not create a reference
    print("Wear ref:", d['primary'])   # fetch the object if it is still alive
    del a                               # remove the one reference
    gc.collect()                        # run garbage collection right away
    try:
        d['primary']
    except KeyError as e:
        print("Weak ref deleted:", e)

    from array import array

    a = array('H', [4000, 10, 700, 22222])
    print("sum(array) =", sum(a))
    print("a[1:3] =", a[1:3])

    from _collections import deque

    d = deque(["task1", "task2", "task3"])
    d.append("task4")
    print("deque: Handling", d.popleft())

    import bisect

    scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
    print("scores before bisect insort =", scores)
    bisect.insort(scores, (300, 'ruby'))
    print("scores after bisect insort =", scores)

    from heapq import heapify, heappop, heappush

    data = [1, 3, 5, 6, 9, 2, 4, 6, 8, 0]
    print("data before heapify =", data)
    heapify(data)                               # rearrange the list into heap order
    print("data after heapify =", data)
    heappush(data, -5)                          # add a new entry
    print("data after heappush -5 =", data)
    print("Pop three smallest entries:")
    print([heappop(data) for i in range(3)])    # fetch the three smallest entries

    from decimal import Decimal, getcontext

    print("Calculating a 5% tax on a 70 cent charge:")
    print("Decimal rounding:", round(Decimal('0.70') * Decimal('1.05'), 2))
    print("Float rounding:", round(0.70 * 1.05, 2))
    assert (Decimal('1.00') % Decimal('0.10')) == Decimal('0.00')
    assert 1.00 % 0.10 != 0.0
    assert sum([Decimal('0.1')] * 10) == Decimal('1.0')
    assert sum([0.1] * 10) != 1.0

    getcontext().prec = 36
    print(f"1/7 (precision {getcontext().prec}) = {Decimal(1) / Decimal(7)}")


#########################################################################################
# This section must be executed by calling exercises.py directly from the command line
#########################################################################################

# Quality control
def _average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(_average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


# Run 'python3 exercices.py' to run doc test and unit test
import unittest


class TestStatisticalFunctions(unittest.TestCase):
    """My first unit test"""

    def test_average(self):
        self.assertEqual(_average([20, 30, 70]), 40.0)
        self.assertEqual(round(_average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            _average([])
        with self.assertRaises(TypeError):
            # noinspection PyArgumentList
            _average(20, 30, 70)


if __name__ == "__main__":
    import doctest

    print("Testing documentation code of average()")
    print("Doc: ", _average.__doc__)
    doctest.testmod()

    print("Testing now with unit test…")
    unittest.main()
