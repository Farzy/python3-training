# N-Digit Lock Rotation Algorithm (Weighted)

This document describes the problem of minimizing the *cost* of manipulations on an N-digit lock where different manipulations have different costs.

## 1. Problem Description

The goal is to create a Python algorithm to find the lowest-cost sequence of rotations to get from a starting code to a target code on an N-digit lock.

This version introduces a critical change: the graph is **weighted**.
- Manipulations starting from the **left** have a higher cost (`LEFT_WEIGHT`, e.g., 2).
- Manipulations starting from the **right** have a baseline cost (`RIGHT_WEIGHT` = 1).

The objective is no longer to find the path with the fewest steps, but the path with the minimum total accumulated cost.

## 2. Algorithmic Solution

Because the problem is now to find the shortest path in a **weighted graph**, the ideal algorithm is **Dijkstra's Algorithm**.

### 2.1. Why Not BFS?
Breadth-First Search (BFS) is perfect for unweighted graphs because it explores layer by layer, guaranteeing that the first time it reaches the target, it has done so in the fewest steps. However, it cannot handle varying costs. A 1-step path with a cost of 10 is worse than a 3-step path where each step costs 1, but BFS would find the 1-step path first and incorrectly declare it the winner.

### 2.2. Graph Representation
- **Nodes**: Each of the 10^N possible combinations on the lock is a node.
- **Edges**: An edge exists between two nodes if one can be transformed into the other by a single manipulation. Each edge now has a weight associated with it (`LEFT_WEIGHT` or `RIGHT_WEIGHT`).

### 2.3. State Representation
The state representation remains the same: the **tuple of differences** `(d1, ..., dN)`, where the goal is to reach the zero-tuple `(0, ..., 0)`.

### 2.4. Dijkstra's Algorithm Implementation
Dijkstra's algorithm is a modification of BFS that uses a **priority queue** to decide which node to explore next. The node with the lowest accumulated cost is always chosen.

1.  Initialize a **priority queue** with the starting state: `(0, initial_difference, [])`, where the elements are `(cost, state, path)`. The initial cost is 0.
2.  Initialize a `visited_costs` dictionary to store the minimum cost found so far to reach each state. This prevents cycles and redundant work on more expensive paths.
3.  While the priority queue is not empty:
    a. Dequeue the state with the **lowest cost**: `(current_cost, current_diff, path)`.
    b. If `current_diff` is the target (all zeros), we have found the lowest-cost path. Return it.
    c. If the `current_cost` is greater than the cost we've already recorded in `visited_costs` for this state, it means we've found a better path previously, so we skip this one.
    d. Generate all unique neighbor states (moves).
    e. For each neighbor:
        i. Calculate the `new_cost` by adding the move's weight (`LEFT_WEIGHT` or `RIGHT_WEIGHT`) to `current_cost`.
        ii. If this neighbor has not been visited, or if the `new_cost` is less than the previously recorded cost for this neighbor, update its cost in `visited_costs` and push the new state to the priority queue: `(new_cost, neighbor_diff, new_path)`.

This process guarantees that the first time we reach the target state, we have done so via the path with the minimum possible total cost.
