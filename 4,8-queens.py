import heapq

# ---------- Check Safe Position ----------
def is_safe(board, row, col):

    for prev_col, prev_row in enumerate(board):

        # Same row
        if prev_row == row:
            return False

        # Same diagonal
        if abs(prev_row - row) == abs(prev_col - col):
            return False

    return True


# ---------- Heuristic Function h(n) ----------
# Estimate remaining queens to place
def heuristic(board, n):

    return n - len(board)


# ---------- Cost Function g(n) ----------
# Number of queens already placed
def cost(board):

    return len(board)


# ---------- A* Algorithm ----------
def solve_n_queens_astar(n):

    # Priority Queue stores:
    # (f(n), g(n), column, board)

    pq = []

    initial_board = []

    g = cost(initial_board)

    h = heuristic(initial_board, n)

    f = g + h

    heapq.heappush(pq, (f, g, 0, initial_board))

    solutions = []

    while pq:

        f, g, col, board = heapq.heappop(pq)

        # Goal State
        if col == n:

            solutions.append(board)

            continue

        # Try all rows in current column
        for row in range(n):

            if is_safe(board, row, col):

                new_board = board + [row]

                new_g = cost(new_board)

                new_h = heuristic(new_board, n)

                new_f = new_g + new_h

                heapq.heappush(
                    pq,
                    (new_f, new_g, col + 1, new_board)
                )

    return solutions


# ---------- Print Board ----------
def print_board(solution, n):

    for row in range(n):

        for col in range(n):

            if solution[col] == row:
                print("Q", end=" ")

            else:
                print(".", end=" ")

        print()

    print("-" * (2 * n))


# ---------- Main ----------
n = int(input("Enter value of N: "))

solutions = solve_n_queens_astar(n)

print("\nTotal Solutions Found:", len(solutions))
print()

for i, sol in enumerate(solutions):

    print(f"Solution {i + 1}:\n")

    print_board(sol, n)
