# 4-Digit Lock Rotation Algorithm

This document describes the problem of minimizing manipulations on a 4-digit lock and the algorithmic solution implemented.

## 1. Problem Description

The goal is to create a Python algorithm to minimize the number of rotations required on a 4-digit combination lock to get from a starting code to a target code.

## 2. Algorithmic Solution

The problem can be modeled as finding the shortest path in an unweighted graph, making **Breadth-First Search (BFS)** the ideal algorithm.

### 2.1. Graph Representation
- **Nodes**: Each of the 10,000 possible combinations on the lock (`0000` to `9999`) is a node in the graph.
- **Edges**: An edge exists between two nodes if one can be transformed into the other by a single manipulation. Since each manipulation has a cost of 1, all edge weights are 1.

### 2.2. State Representation
Instead of using the absolute code on the lock as the state, we use a more efficient representation: the **tuple of differences**.

A state is a tuple `(d1, d2, d3, d4)` where each `di` is the difference that still needs to be applied to the i-th wheel to match the target. The difference is calculated as `(target[i] - current[i]) % 10`.

- **Initial State**: The tuple of differences between the `start_code` and `target_code`.
- **Target State**: The tuple `(0, 0, 0, 0)`, which signifies that the current combination matches the target.

This approach simplifies the logic, as the goal is always to reach the zero-tuple.

### 2.3. Generating Moves (Neighbors)
The core of the algorithm is generating all possible states reachable in one manipulation. A naive approach would be to try turning every possible block of wheels by every possible amount (1-9). However, we can use a key insight to be much more efficient.

**The key insight is that the optimal amount to turn a block of wheels is always the amount that makes one of the wheels within that block match its target value.** In our difference model, this means turning the block by an amount equal to the current difference of one of its wheels.

This drastically reduces the number of neighbors to explore for each state. For a block of `k` wheels, we only need to generate `k` new states, not `k * 9`.

The possible moves are:
- **Left-side moves**: Turn a block of 1, 2, 3, or 4 wheels starting from the left.
- **Right-side moves**: Turn a block of 1, 2, or 3 wheels starting from the right. (A 4-wheel turn from the right is identical to a 4-wheel turn from the left).

### 2.4. BFS Implementation
The BFS algorithm proceeds as follows:
1.  Initialize a queue with the starting state: `(initial_difference, [])`, where the second element is the path of moves taken so far.
2.  Initialize a `visited` set to store states that have already been processed, preventing cycles and redundant work.
3.  While the queue is not empty:
    a. Dequeue the current state `(current_diff, path)`.
    b. If `current_diff` is `(0, 0, 0, 0)`, we have found the shortest path. Return it.
    c. Generate all unique neighbor states using the move generation logic described above.
    d. For each new neighbor state that has not been visited:
        i. Add it to the `visited` set.
        ii. Enqueue the new state along with its updated path: `(neighbor_diff, new_path)`.

This process guarantees that the first time we reach the target state `(0, 0, 0, 0)`, we have done so in the minimum number of steps.
