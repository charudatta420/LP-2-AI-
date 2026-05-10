def bfs(graph, queue, visited):

    if not queue:
        return

    node = queue.pop(0)

    print(node, end=" ")

    for neighbour in graph[node]:

        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)

    bfs(graph, queue, visited)


vertices = int(input("Enter number of vertices: "))

graph = {}

for i in range(vertices):

    vertex = input("Enter vertex: ")

    neighbours = input(
        f"Enter neighbours of {vertex}: "
    ).split()

    graph[vertex] = neighbours


start = input("Enter starting vertex: ")

visited = [start]

queue = [start]

print("BFS Traversal:")

bfs(graph, queue, visited)

# five vertices :- 
#         A
#       /  \
#      B     C
#     /      \
#     D        E