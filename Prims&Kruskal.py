print("1. Prim's Minimum Spanning Tree")
print("2. Kruskal's Minimum Spanning Tree")

choice = int(input("Enter your choice: "))

if choice == 1:

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

elif choice == 2:

    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    edges = []

    print("Enter edges (source destination weight):")

    for i in range(e):

        u, v, w = map(int, input().split())

        edges.append([w, u, v])

    edges.sort()

    parent = []

    for i in range(n):
        parent.append(i)

    def find(i):

        while parent[i] != i:
            i = parent[i]

        return i

    print("Edges in Minimum Spanning Tree:")

    count = 0

    for edge in edges:

        w, u, v = edge

        x = find(u)
        y = find(v)

        if x != y:

            print(u, "-", v, ":", w)

            parent[x] = y

            count += 1

        if count == n - 1:
            break

else:

    print("Invalid Choice")