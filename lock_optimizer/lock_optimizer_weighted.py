
import collections
import heapq

# Define the weights for the moves
LEFT_WEIGHT = 2  # Turning left is more "costly"
RIGHT_WEIGHT = 1 # Turning right is the baseline cost

def solve_lock_weighted(start_code, target_code, left_weight=LEFT_WEIGHT, right_weight=RIGHT_WEIGHT):
    """
    Calculates the minimum cost path to get from a start code to a target code on a
    weighted N-digit lock.

    This function models the problem as a shortest path search on a weighted graph.
    It uses Dijkstra's algorithm to find the path with the minimum accumulated cost.

    - Each combination is a node in the graph.
    - A manipulation (move) is a weighted edge. Left-side moves have a weight of
      `left_weight`, and right-side moves have `right_weight`.

    The state is represented by the "difference" tuple `(d1, ..., dN)`, where each `di` is
    the number of upward steps needed for the i-th wheel to match the target. The goal is to
    reach the state (0, ..., 0).

    Args:
        start_code (str): The N-digit starting combination.
        target_code (str): The N-digit target combination.
        left_weight (int): The cost of a manipulation starting from the left.
        right_weight (int): The cost of a manipulation starting from the right.

    Returns:
        tuple[int, list[str]]: A tuple containing the total cost and the list of moves.
                               Returns (0, []) if start and target are the same.
                               Returns None if no solution is found.
    """
    if start_code == target_code:
        return 0, []

    if len(start_code) != len(target_code):
        raise ValueError("Start and target codes must have the same number of digits.")

    n_digits = len(start_code)
    start_ints = [int(c) for c in start_code]
    target_ints = [int(c) for c in target_code]

    initial_diff = tuple((target_ints[i] - start_ints[i]) % 10 for i in range(n_digits))

    # Priority Queue for Dijkstra's: stores (cost, difference_tuple, path_of_moves)
    # The heap will always return the item with the smallest cost.
    pq = [(0, initial_diff, [])]
    
    # Visited dict to store the minimum cost found so far for each state
    visited_costs = {initial_diff: 0}

    while pq:
        cost, current_diff, path = heapq.heappop(pq)

        # If we pop a state and its cost is higher than one we've already processed, skip it.
        if cost > visited_costs[current_diff]:
            continue

        if all(d == 0 for d in current_diff):
            return cost, path

        # --- Generate all possible next states (neighbors) ---

        # Moves starting from the LEFT (higher cost)
        for num_wheels in range(1, n_digits + 1):
            for wheel_to_zero in range(num_wheels):
                turn_amount = current_diff[wheel_to_zero]
                if turn_amount == 0: continue

                new_diff_list = list(current_diff)
                for i in range(num_wheels):
                    new_diff_list[i] = (new_diff_list[i] - turn_amount) % 10
                
                new_diff = tuple(new_diff_list)
                new_cost = cost + left_weight

                # If we haven't seen this state, or if we found a cheaper path to it
                if new_diff not in visited_costs or new_cost < visited_costs[new_diff]:
                    visited_costs[new_diff] = new_cost
                    direction = "up"
                    amount = turn_amount
                    if amount > 5:
                        direction = "down"
                        amount = 10 - amount
                    
                    new_path = path + [f"Turn {num_wheels} left wheels {direction} by {amount} (cost: {left_weight})"]
                    heapq.heappush(pq, (new_cost, new_diff, new_path))

        # Moves starting from the RIGHT (lower cost)
        for num_wheels in range(1, n_digits):
            for wheel_to_zero_idx in range(n_digits - num_wheels, n_digits):
                turn_amount = current_diff[wheel_to_zero_idx]
                if turn_amount == 0: continue

                new_diff_list = list(current_diff)
                for i in range(n_digits - num_wheels, n_digits):
                    new_diff_list[i] = (new_diff_list[i] - turn_amount) % 10

                new_diff = tuple(new_diff_list)
                new_cost = cost + right_weight

                if new_diff not in visited_costs or new_cost < visited_costs[new_diff]:
                    visited_costs[new_diff] = new_cost
                    direction = "up"
                    amount = turn_amount
                    if amount > 5:
                        direction = "down"
                        amount = 10 - amount

                    new_path = path + [f"Turn {num_wheels} right wheels {direction} by {amount} (cost: {right_weight})"]
                    heapq.heappush(pq, (new_cost, new_diff, new_path))
    
    return None # Should not be reached

if __name__ == "__main__":
    start = "0000"
    target = "1000"

    print(f"Solving for start: {start}, target: {target} with LEFT_WEIGHT={LEFT_WEIGHT}")
    
    # In this case, turning 1 left wheel is a single move with cost 2.
    # Turning 4 left wheels is also a single move with cost 2.
    # The algorithm should find the single move.
    
    solution = solve_lock_weighted(start, target)
    if solution:
        total_cost, path = solution
        print(f"Found solution with total cost {total_cost}:")
        for step in path:
            print(f"- {step}")
    else:
        print("No solution found.")

    print("-" * 20)

    start_complex = "4564"
    target_complex = "4586"
    print(f"Solving for start: {start_complex}, target: {target_complex} with LEFT_WEIGHT={LEFT_WEIGHT}")

    # The optimal unweighted solution is one move: "Turn 3 left wheels up by 2". Cost = 2
    # Another solution is two moves: "Turn 2 right wheels up by 2", then "Turn 1 right wheel down by 2". Cost = 1+1=2
    # Dijkstra should find one of these paths.
    
    solution_complex = solve_lock_weighted(start_complex, target_complex)
    if solution_complex:
        total_cost, path = solution_complex
        print(f"Found solution with total cost {total_cost}:")
        for step in path:
            print(f"- {step}")
    else:
        print("No solution found.")
