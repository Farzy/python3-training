"""https://brilliant.org/courses/probability-fundamentals/fairness-and-expected-value-2/symmetry/2/

A stick of length 1 is broken into two pieces somewhere along its length (with the position
being chosen uniformly at random).
In expectation, how long will the longer piece be?
"""

import random


def avg_sticks(count: int) -> float:
    """Cut a stick of length 1 in two, and return the average length
    of the longest half.

    Args:
        count (int): number of sticks to draw

    Returns:
        float: Average length of the longest half
    """
    lengths = 0.0

    for i in range(count):
        # Cut the stick in two
        cut = random.random()
        if cut < 0.5:
            # Keep the longest stick
            cut = 1 - cut
        lengths += cut
    # compute longest sticks average length
    return lengths / count


if __name__ == '__main__':
    avg_longest_stick = avg_sticks(10_000)
    print(f"Average longest stick is {avg_longest_stick} long.")
