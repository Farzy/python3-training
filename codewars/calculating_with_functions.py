"""Calculating with Functions

See https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

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


# Create a number functions generator
def _number(number):
    """Number functions generator

    Create a closure containing a number (0 to 9) and return it.
    If this closure is called with no parameter, it returns the number.
    If this close receives a function as parameter, it applys the function
    to the number and returns the resulting number.
    """
    def f(operation=None):
        if not operation:
            return number
        return operation(number)

    return f


# Create an operation functions generator
def _operation(op):
    """Operation functions generator

    Create a closure containing an operator (+, -, *, //) from the
    'int' class.

    The closure must be called with a number (right operand) as parameter. It returns another
    closure with the right operand + the operator in it.

    In turn, if the inner closure is called with a number parameter (left operand), it
    applies the operator to both operands. The operands must both be Integers (class 'int').
    """

    def f(r_number):
        def f2(l_number):
            return op(l_number, r_number)

        return f2

    return f


# Use the number generator to create the 10 numbers as functions
zero = _number(0)
one = _number(1)
two = _number(2)
three = _number(3)
four = _number(4)
five = _number(5)
six = _number(6)
seven = _number(7)
eight = _number(8)
nine = _number(9)

# Use the functions generator to create the 4 basic operations as functions
plus = _operation(int.__add__)
minus = _operation(int.__sub__)
times = _operation(int.__mul__)
divided_by = _operation(int.__floordiv__)


if __name__ == '__main__':
    assert zero() == 0
    assert one() == 1
    assert nine() == 9
    assert one(plus(two())) == 3
    assert five(times(six())) == 30
    assert nine(divided_by(four())) == 2
    assert six(minus(four())) == 2
    assert seven(times(five())) == 35
    assert four(plus(nine())) == 13
    assert eight(minus(three())) == 5
    assert six(divided_by(two())) == 3
