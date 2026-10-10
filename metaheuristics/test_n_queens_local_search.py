#!/usr/bin/env python3

"""Tests for the N-Queens metaheuristics. Run with: python3 -m unittest discover -s metaheuristics"""

import random
import unittest

from n_queens_local_search import (
    count_attacking_pairs,
    is_solution,
    min_conflicts,
    simulated_annealing,
)


class TestHelpers(unittest.TestCase):
    def test_known_solution(self):
        self.assertTrue(is_solution([0, 4, 7, 5, 2, 6, 1, 3]))

    def test_attacking_pairs(self):
        self.assertEqual(count_attacking_pairs([0, 0, 0]), 3)  # same column
        self.assertEqual(count_attacking_pairs([0, 1, 2, 3]), 6)  # same diagonal
        self.assertEqual(count_attacking_pairs([1, 3, 0, 2]), 0)

    def test_out_of_board(self):
        self.assertFalse(is_solution([0, 4]))


class TestSolvers(unittest.TestCase):
    SOLVERS = (min_conflicts, simulated_annealing)

    def test_finds_valid_solutions(self):
        for solver in self.SOLVERS:
            for n in (1, 4, 8, 50):
                for seed in range(5):
                    with self.subTest(solver=solver.__name__, n=n, seed=seed):
                        result = solver(n, rng=random.Random(seed))
                        if solver is min_conflicts and result.solution is None:
                            continue  # min-conflicts may stall on a plateau; see README
                        self.assertTrue(is_solution(result.solution))

    def test_reproducible_with_seed(self):
        for solver in self.SOLVERS:
            with self.subTest(solver=solver.__name__):
                a = solver(30, rng=random.Random(7))
                b = solver(30, rng=random.Random(7))
                self.assertEqual(a, b)

    def test_no_solution_exists(self):
        # There is no solution for N = 2 or 3: local search must give up, not lie.
        for solver in self.SOLVERS:
            for n in (2, 3):
                with self.subTest(solver=solver.__name__, n=n):
                    result = solver(n, max_steps=1000, rng=random.Random(0))
                    self.assertIsNone(result.solution)
                    self.assertEqual(result.steps, 1000)

    def test_min_conflicts_success_rate(self):
        # Most runs succeed even though a few may stall.
        found = sum(
            min_conflicts(20, rng=random.Random(seed)).solution is not None
            for seed in range(20)
        )
        self.assertGreaterEqual(found, 18)


if __name__ == "__main__":
    unittest.main()
