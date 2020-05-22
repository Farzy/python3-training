"""
Fibonacci number module
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
