#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script solves the classic N-Queens problem using a backtracking algorithm.
It generates all possible solutions for placing N non-attacking queens on an NxN chessboard
and prints them with an elegant Unicode visualization.
"""

import time
from typing import Generator
import click


def solve_n_queens(n: int) -> Generator[list[int], None, None]:
    """
    Generator that solves the N queens problem using backtracking.
    Yields a list representing the column of the queen for each row.
    """

    def backtrack(
        row: int, cols: set[int], diag: set[int], anti_diag: set[int], state: list[int]
    ):
        """
        Recursive helper function to find valid queen placements.
        """
        if row == n:
            yield state.copy()
            return

        for col in range(n):
            curr_diag = row - col
            curr_anti_diag = row + col

            # O(1) collision detection using sets
            if col in cols or curr_diag in diag or curr_anti_diag in anti_diag:
                continue

            # Add constraint
            cols.add(col)
            diag.add(curr_diag)
            anti_diag.add(curr_anti_diag)
            state.append(col)

            # Recursive call
            yield from backtrack(row + 1, cols, diag, anti_diag, state)

            # Remove constraint (Backtrack)
            cols.remove(col)
            diag.remove(curr_diag)
            anti_diag.remove(curr_anti_diag)
            state.pop()

    yield from backtrack(0, set(), set(), set(), [])


def render_board(solution: list[int]) -> str:
    """
    Transforms a solution into an elegant Unicode representation.
    """
    n = len(solution)

    # Top border
    board_str = ["┌" + "───┬" * (n - 1) + "───┐"]

    for row in range(n):
        row_chars = []
        for col in range(n):
            if solution[row] == col:
                row_chars.append(" ♛ ")
            else:
                # Create a checkerboard pattern (light and dark squares)
                is_dark = (row + col) % 2 != 0
                row_chars.append("░░░" if is_dark else "   ")

        board_str.append("│" + "│".join(row_chars) + "│")

        # Intermediate separators
        if row < n - 1:
            board_str.append("├" + "───┼" * (n - 1) + "───┤")

    # Bottom border
    board_str.append("└" + "───┴" * (n - 1) + "───┘")

    return "\n".join(board_str)


@click.command()
@click.option("--size", "-s", default=8, help="Size of the board (number of queens).")
def main(size: int):
    """
    Solves the N-Queens problem and prints all possible solutions.

    This program calculates all valid arrangements of N non-attacking queens
    on an NxN chessboard. It uses a backtracking algorithm to find the solutions
    and prints each one with a Unicode visualization.
    """
    start_time = time.perf_counter()
    solutions = list(solve_n_queens(size))
    execution_time = time.perf_counter() - start_time

    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}/{len(solutions)}")
        print(render_board(sol))
        print("\n")

    print(f"Total solutions found: {len(solutions)}")
    print(f"Execution time: {execution_time:.4f} seconds")


if __name__ == "__main__":
    main()
