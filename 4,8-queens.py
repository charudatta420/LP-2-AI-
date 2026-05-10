
import heapq

def is_safe(board, row, col):
    """
    Checks if it's safe to place a queen at (row, col).
    board stores previous queen positions as [row0, row1, row2...]
    """
    for prev_col, prev_row in enumerate(board):
        # Check horizontal row and both diagonals
        if prev_row == row or abs(prev_row - row) == abs(prev_col - col):
            return False
    return True

def solve_n_queens_astar(n):
    # Priority Queue stores: (priority, current_column, board_state)
    # We prioritize states with more queens (lower n - len)
    pq = [(n, 0, [])]
    solutions = []

    while pq:
        priority, col, board = heapq.heappop(pq)

        # Goal state reached
        if col == n:
            solutions.append(board)
            continue

        # Try placing a queen in every row of the current column
        for row in range(n):
            if is_safe(board, row, col):
                new_board = board + [row]
                # Push the new state to the queue
                heapq.heappush(pq, (n - len(new_board), col + 1, new_board))

    return solutions

def print_grid(solution, n):
    """Prints the board in a visual grid format."""
    for row in range(n):
        line = ""
        for col in range(n):
            # Check if the queen in this column is at the current row
            if solution[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("-" * (n * 2))

# --- Execution ---
n = int(input("Enter N for A*: "))
results = solve_n_queens_astar(n)

print(f"\nFound {len(results)} total solutions.\n")

for i, sol in enumerate(results):
    print(f"Solution {i+1}:")
    print_grid(sol, n)