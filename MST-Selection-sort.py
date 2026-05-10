print("1. Selection Sort")
print("2. Minimum Spanning Tree")

choice = int(input("Enter your choice: "))


# -------- SELECTION SORT --------

if choice == 1:
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        num = int(input("Enter element: "))
        arr.append(num)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    print("Sorted Array:")

    for i in arr:
        print(i, end=" ")


# -------- MINIMUM SPANNING TREE --------

elif choice == 2:
    n = int(input("Enter number of vertices: "))
    graph = []
    print("Enter adjacency matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    selected = [0] * n
    selected[0] = 1
    edges = 0
    print("Edges in Minimum Spanning Tree:")

    while edges < n - 1:
        minimum = 999
        x = 0
        y = 0

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
        print(x, "-", y, ":", graph[x][y])
        selected[y] = 1
        edges += 1
else:
    print("Invalid Choice")