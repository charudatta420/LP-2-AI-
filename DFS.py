def dfs(graph, node, visited):

    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

vertices = int(input("Enter number of vertices: "))
graph = {}

for i in range(vertices):
    vertex = input("\nEnter vertex name: ")

    neighbours = input(
        f"Enter neighbours of {vertex} separated by space: "
    ).split()

    graph[vertex] = neighbours


start = input("\nEnter starting vertex for DFS: ")
visited = set()
print("\nDFS Traversal:")

dfs(graph, start, visited)

# five vertices :-
#         A
#       /  \
#      B     C
#     /      \
#     D        E