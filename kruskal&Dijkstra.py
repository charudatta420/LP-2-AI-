print("1. Kruskal's Minimum Spanning Tree")
print("2. Dijkstra's Shortest Path Algorithm")

choice = int(input("Enter your choice: "))

if choice == 1:

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

elif choice == 2:

    n = int(input("Enter number of vertices: "))

    graph = []

    print("Enter adjacency matrix:")

    for i in range(n):

        row = list(map(int, input().split()))

        graph.append(row)

    source = int(input("Enter source vertex: "))

    visited = [0] * n

    distance = [999] * n

    distance[source] = 0

    for i in range(n):

        minimum = 999
        u = -1

        for j in range(n):

            if not visited[j] and distance[j] < minimum:

                minimum = distance[j]
                u = j

        visited[u] = 1

        for v in range(n):

            if graph[u][v] != 0 and not visited[v]:

                if distance[u] + graph[u][v] < distance[v]:

                    distance[v] = distance[u] + graph[u][v]

    print("Shortest Distances:")

    for i in range(n):

        print(source, "to", i, "=", distance[i])

else:

    print("Invalid Choice")