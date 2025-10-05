
import collections

def solve_lock(start_code, target_code):
    """
    Calculates the minimum number of manipulations to get from a start code to a target code on an N-digit lock.

    This function models the problem as a shortest path search on a graph where each node is a
    combination and each edge is a single manipulation. It uses a Breadth-First Search (BFS)
    algorithm to find the shortest sequence of manipulations.

    The state is represented by the "difference" tuple `(d1, ..., dN)`, where each `di` is
    the number of upward steps needed for the i-th wheel to match the target. The goal is to
    reach the state (0, ..., 0).

    A "manipulation" is defined as turning a consecutive block of wheels, starting from
    either the far-left or far-right. The key insight is that the optimal amount to turn a
    block of wheels is always the amount that makes one of the wheels in that block match
    its target value (i.e., makes its difference become 0).

    Args:
        start_code (str): The N-digit starting combination (e.g., "1234").
        target_code (str): The N-digit target combination (e.g., "2468").

    Returns:
        list[str]: A list of strings, where each string describes a manipulation.
                   Returns an empty list if the start and target codes are the same.
                   Returns None if no solution is found (which is theoretically impossible).
    """
    if start_code == target_code:
        return []

    if len(start_code) != len(target_code):
        raise ValueError("Start and target codes must have the same number of digits.")

    n_digits = len(start_code)
    start_ints = [int(c) for c in start_code]
    target_ints = [int(c) for c in target_code]

    # The state is the tuple of differences for each wheel. Goal is a tuple of all zeros.
    initial_diff = tuple((target_ints[i] - start_ints[i]) % 10 for i in range(n_digits))

    # Queue for BFS: stores (difference_tuple, path_of_moves)
    queue = collections.deque([(initial_diff, [])])
    # Visited set to avoid cycles and redundant computations
    visited = {initial_diff}

    while queue:
        current_diff, path = queue.popleft()

        if all(d == 0 for d in current_diff):
            return path

        # --- Generate all possible next states (neighbors) ---
        
        # Moves starting from the LEFT
        for num_wheels in range(1, n_digits + 1):
            # The best amount to turn is one that zeros out one of the wheels in the block
            for wheel_to_zero in range(num_wheels):
                turn_amount = current_diff[wheel_to_zero]
                if turn_amount == 0: continue # No use in turning by 0

                new_diff_list = list(current_diff)
                for i in range(num_wheels):
                    new_diff_list[i] = (new_diff_list[i] - turn_amount) % 10
                
                new_diff = tuple(new_diff_list)
                if new_diff not in visited:
                    visited.add(new_diff)
                    direction = "up"
                    amount = turn_amount
                    # It's shorter to turn down if amount > 5
                    if amount > 5:
                        direction = "down"
                        amount = 10 - amount
                    
                    new_path = path + [f"Turn {num_wheels} left wheels {direction} by {amount}"]
                    queue.append((new_diff, new_path))

        # Moves starting from the RIGHT
        for num_wheels in range(1, n_digits):  # N-digit move is covered by the left-side moves
            for wheel_to_zero_idx in range(n_digits - num_wheels, n_digits):
                turn_amount = current_diff[wheel_to_zero_idx]
                if turn_amount == 0: continue

                new_diff_list = list(current_diff)
                for i in range(n_digits - num_wheels, n_digits):
                    new_diff_list[i] = (new_diff_list[i] - turn_amount) % 10

                new_diff = tuple(new_diff_list)
                if new_diff not in visited:
                    visited.add(new_diff)
                    direction = "up"
                    amount = turn_amount
                    if amount > 5:
                        direction = "down"
                        amount = 10 - amount

                    new_path = path + [f"Turn {num_wheels} right wheels {direction} by {amount}"]
                    queue.append((new_diff, new_path))
    
    return None # Should not be reached

if __name__ == "__main__":
    # Example 1 (N=4)
    start_4 = "4564"
    target_4 = "4586"
    print(f"Solving for start: {start_4}, target: {target_4}")
    solution_4 = solve_lock(start_4, target_4)
    if solution_4:
        print(f"Found solution in {len(solution_4)} steps:")
        for step in solution_4:
            print(f"- {step}")
    else:
        print("No steps needed or no solution found.")
    
    print("-" * 20)

    # Example 2 (N=4, more complex)
    start_4_complex = "1234"
    target_4_complex = "5091"
    print(f"Solving for start: {start_4_complex}, target: {target_4_complex}")
    solution_4_complex = solve_lock(start_4_complex, target_4_complex)
    if solution_4_complex:
        print(f"Found solution in {len(solution_4_complex)} steps:")
        for step in solution_4_complex:
            print(f"- {step}")
    else:
        print("No steps needed or no solution found.")

    print("-" * 20)

    # Example 3 (N=5)
    start_5 = "00000"
    target_5 = "12321"
    print(f"Solving for start: {start_5}, target: {target_5}")
    solution_5 = solve_lock(start_5, target_5)
    if solution_5:
        print(f"Found solution in {len(solution_5)} steps:")
        for step in solution_5:
            print(f"- {step}")
    else:
        print("No steps needed or no solution found.")

