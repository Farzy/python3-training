"""Benchmark code on a CodeWars Kata
https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/solutions/python

https://www.codewars.com/kata/reviews/55249a95de8b4b5ae2000464/groups/552540ce2142d7ba24000e65
seems awful in complexity.

With a large word (10.000 characters) my code is 2OO to 300 times
faster than the best voted solution I found because there is no
exponential complexity in it.

>>> python3 codewars/duplicate_encoder.py                                                                                                                                                               ─╯
Benchmark 'duplicate_encode_liked', word size = 50000, rounds = 100
274.265376327
Benchmark 'duplicate_encode_mine', word size = 50000, rounds = 100
1.6030242989999692
Benchmark 'duplicate_encode_mine2', word size = 50000, rounds = 100
0.730968928999971

"""


def duplicate_encode_liked(word):
    """Solution https://www.codewars.com/kata/reviews/55249a95de8b4b5ae2000464/groups/552540ce2142d7ba24000e65"""

    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


def duplicate_encode_mine(word):
    """My first solution"""

    result = {}
    for c in word:
        c = c.lower()
        if c in result:
            result[c] = ")"
        else:
            result[c] = "("
    return "".join(result[c.lower()] for c in word)


def duplicate_encode_mine2(word):
    """Optimize lower() calls"""

    result = {}
    word = word.lower()
    for c in word:
        if c in result:
            result[c] = ")"
        else:
            result[c] = "("
    return "".join(result[c] for c in word)


def setup(size=1_000):
    """Initialize test by creating a long word once

    The long_word variable is placed in the module namespace."""

    import random

    # noinspection PyGlobalUndefined
    global long_word

    chars = [chr(i) for i in range(ord(' '), 127)]
    long_word = "".join(random.choices(chars, k=size))


def test(func):
    """Start the with the selected function"""
    func(long_word)


if __name__ == '__main__':
    import timeit

    word_size = 50_000
    rounds = 100
    solutions = ['duplicate_encode_liked', 'duplicate_encode_mine',
                 'duplicate_encode_mine2']

    for solution in solutions:
        print(f"Benchmack '{solution}', word size = {word_size}, rounds = {rounds}")
        print(timeit.timeit(
            f"test({solution})",
            setup=f"from __main__ import test, {solution}, setup;"
                  f"setup({word_size})",
            number=rounds
        ))
