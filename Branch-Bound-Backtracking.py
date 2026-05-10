# N-Queens using Backtracking and Branch & Bound
# Simple User Driven Program

# Function to print board
def print_board(board, n):

    for i in range(n):
        for j in range(n):

            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


# ---------- Backtracking ----------
def backtracking(board, row, n):

    if row == n:
        return True

    for col in range(n):

        safe = True

        for i in range(row):

            # Column check
            if board[i] == col:
                safe = False

            # Diagonal check
            if abs(board[i] - col) == abs(i - row):
                safe = False

        if safe:

            board[row] = col

            if backtracking(board, row + 1, n):
                return True

            # Backtrack
            board[row] = -1

    return False


# ---------- Branch and Bound ----------
def branch_bound(board, row, n, cols, d1, d2):

    if row == n:
        return True

    for col in range(n):

        if cols[col] == 0 and d1[row - col + n - 1] == 0 and d2[row + col] == 0:

            board[row] = col

            cols[col] = 1
            d1[row - col + n - 1] = 1
            d2[row + col] = 1

            if branch_bound(board, row + 1, n, cols, d1, d2):
                return True

            # Backtrack
            board[row] = -1

            cols[col] = 0
            d1[row - col + n - 1] = 0
            d2[row + col] = 0

    return False


# ---------- Main ----------
n = int(input("Enter value of N: "))

print("\n1. Backtracking")
print("2. Branch and Bound")

choice = int(input("Enter choice: "))

board = [-1] * n

if choice == 1:

    if backtracking(board, 0, n):

        print("\nSolution using Backtracking:\n")
        print_board(board, n)

    else:
        print("No Solution")

elif choice == 2:

    cols = [0] * n
    d1 = [0] * (2 * n - 1)
    d2 = [0] * (2 * n - 1)

    if branch_bound(board, 0, n, cols, d1, d2):

        print("\nSolution using Branch and Bound:\n")
        print_board(board, n)

    else:
        print("No Solution")

else:
    print("Invalid Choice")