"""
Fibonacci number module

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


def fib(n: int):
    """Write Fibonacci series up to n

    :param n:
    :return:
    """
    a, b = 1, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n: int) -> list:
    """Return Fibonacci series up to n

    :param n:
    :return:
    """
    result = []
    a, b = 1, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))
