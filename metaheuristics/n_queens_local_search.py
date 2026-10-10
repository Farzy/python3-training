#!/usr/bin/env python3

"""
Two metaheuristics for the N-Queens problem: min-conflicts and simulated annealing.

Unlike the backtracking solver in `eight-queens.py`, which explores the search tree
systematically, these methods start from a complete but wrong board and repair it
step by step. They find one solution very quickly, even for N = 1000, but they cannot
enumerate all solutions nor prove that none exists.

See README.md in this folder for an explanation of both algorithms.
"""

import math
import random
import statistics
import time
from collections.abc import Callable
from dataclasses import dataclass

import click


@dataclass
class SearchResult:
    """Outcome of one local search run."""

    solution: list[int] | None  # solution[row] = column of the queen, None on failure
    steps: int  # number of moves tried


def count_attacking_pairs(cols: list[int]) -> int:
    """Number of pairs of queens attacking each other (same column or diagonal)."""
    n = len(cols)
    col_count = [0] * n
    diag_count = [0] * (2 * n)  # row - col + n
    anti_diag_count = [0] * (2 * n)  # row + col
    for row, col in enumerate(cols):
        col_count[col] += 1
        diag_count[row - col + n] += 1
        anti_diag_count[row + col] += 1
    return sum(
        c * (c - 1) // 2
        for counts in (col_count, diag_count, anti_diag_count)
        for c in counts
    )


def is_solution(cols: list[int]) -> bool:
    """True if `cols` places len(cols) queens with no two attacking each other."""
    n = len(cols)
    return all(0 <= c < n for c in cols) and count_attacking_pairs(cols) == 0


def min_conflicts(
    n: int, max_steps: int = 100_000, rng: random.Random | None = None
) -> SearchResult:
    """
    Min-conflicts local search.

    Start with one queen per row in a random column. At each step, pick a random queen
    that is attacked, and move it, within its row, to the column with the fewest
    conflicts (ties broken at random). Stop when no queen is attacked.
    """
    rng = rng or random.Random()
    cols = [rng.randrange(n) for _ in range(n)]

    # Counters let us evaluate a square in O(1) instead of scanning the whole board.
    col_count = [0] * n
    diag_count = [0] * (2 * n)
    anti_diag_count = [0] * (2 * n)

    def place(row: int, col: int, delta: int) -> None:
        col_count[col] += delta
        diag_count[row - col + n] += delta
        anti_diag_count[row + col] += delta

    def conflicts(row: int, col: int) -> int:
        """Queens attacking square (row, col), excluding the queen of this row."""
        return col_count[col] + diag_count[row - col + n] + anti_diag_count[row + col]

    for row, col in enumerate(cols):
        place(row, col, +1)

    for step in range(max_steps):
        # A queen on its own square counts itself 3 times (column + 2 diagonals).
        attacked = [row for row in range(n) if conflicts(row, cols[row]) > 3]
        if not attacked:
            return SearchResult(cols, step)

        row = rng.choice(attacked)
        place(row, cols[row], -1)  # lift the queen so it does not count itself
        scores = [conflicts(row, col) for col in range(n)]
        best = min(scores)
        cols[row] = rng.choice([col for col, s in enumerate(scores) if s == best])
        place(row, cols[row], +1)

    return SearchResult(None, max_steps)


def simulated_annealing(
    n: int,
    max_steps: int = 1_000_000,
    initial_temperature: float = 2.0,
    cooling_rate: float = 0.99995,
    rng: random.Random | None = None,
) -> SearchResult:
    """
    Simulated annealing.

    The state is a permutation (one queen per row and per column), so only diagonal
    conflicts remain. The "energy" is the number of attacking pairs; 0 means solved.
    A move swaps the columns of two random rows. A move that lowers the energy is
    always accepted; one that raises it by `delta` is accepted with probability
    exp(-delta / T). The temperature T decreases geometrically, so the search accepts
    many bad moves at first (exploration) and almost none at the end (exploitation).
    """
    rng = rng or random.Random()
    if n == 1:
        return SearchResult([0], 0)

    cols = list(range(n))
    rng.shuffle(cols)

    diag_count = [0] * (2 * n)
    anti_diag_count = [0] * (2 * n)
    for row, col in enumerate(cols):
        diag_count[row - col + n] += 1
        anti_diag_count[row + col] += 1
    energy = sum(c * (c - 1) // 2 for c in diag_count + anti_diag_count)

    def move(row: int, col: int, delta: int) -> int:
        """Add (delta=+1) or remove (delta=-1) a queen; return the energy change."""
        d, a = row - col + n, row + col
        if delta < 0:
            diag_count[d] -= 1
            anti_diag_count[a] -= 1
            return -(diag_count[d] + anti_diag_count[a])
        change = diag_count[d] + anti_diag_count[a]
        diag_count[d] += 1
        anti_diag_count[a] += 1
        return change

    def swap(r1: int, r2: int) -> int:
        """Swap the columns of rows r1 and r2; return the energy change."""
        c1, c2 = cols[r1], cols[r2]
        change = move(r1, c1, -1) + move(r2, c2, -1)
        change += move(r1, c2, +1) + move(r2, c1, +1)
        cols[r1], cols[r2] = c2, c1
        return change

    temperature = initial_temperature
    for step in range(max_steps):
        if energy == 0:
            return SearchResult(cols, step)

        r1, r2 = rng.sample(range(n), 2)
        delta = swap(r1, r2)
        if delta <= 0 or rng.random() < math.exp(-delta / temperature):
            energy += delta
        else:
            swap(r1, r2)  # reject: undo the move

        temperature = max(temperature * cooling_rate, 1e-3)

    return SearchResult(None, max_steps)


SOLVERS: dict[str, Callable[..., SearchResult]] = {
    "min-conflicts": min_conflicts,
    "annealing": simulated_annealing,
}


@click.command()
@click.option("--size", "-s", default=100, show_default=True, help="Number of queens.")
@click.option(
    "--runs", "-r", default=20, show_default=True, help="Runs (seeds) per method."
)
@click.option(
    "--method",
    "-m",
    type=click.Choice(["all", *SOLVERS]),
    default="all",
    show_default=True,
    help="Method to benchmark.",
)
def main(size: int, runs: int, method: str):
    """
    Benchmark the metaheuristics on the N-Queens problem.

    Each method runs once per seed (0 .. RUNS-1), so results are reproducible.
    A single run says little about a randomized algorithm: look at the success
    rate and at the spread of times, not only at the median.
    """
    methods = SOLVERS if method == "all" else {method: SOLVERS[method]}
    print(f"N = {size}, {runs} runs per method")
    print(
        f"{'method':<15}{'success':>9}{'median time':>14}{'max time':>11}{'median steps':>14}"
    )
    for name, solver in methods.items():
        times, steps, successes = [], [], 0
        for seed in range(runs):
            start = time.perf_counter()
            result = solver(size, rng=random.Random(seed))
            times.append(time.perf_counter() - start)
            steps.append(result.steps)
            if result.solution is not None:
                assert is_solution(result.solution)
                successes += 1
        print(
            f"{name:<15}{successes:>4}/{runs:<4}"
            f"{statistics.median(times):>13.4f}s{max(times):>10.4f}s"
            f"{statistics.median(steps):>14.0f}"
        )


if __name__ == "__main__":
    main()
