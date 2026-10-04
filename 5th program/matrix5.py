graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}
def bfs(start):

    visited = []
    queue = []

    queue.append(start)
    visited.append(start)

    while queue:

        vertex = queue.pop(0)

        print(vertex, end=" ")

        for neighbour in graph[vertex]:

            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# DFS
def dfs(vertex, visited):

    visited.add(vertex)

    print(vertex, end=" ")

    for neighbour in graph[vertex]:

        if neighbour not in visited:
            dfs(neighbour, visited)


print("BFS Traversal:")
bfs(0)

print("\nDFS Traversal:")

visited = set()

dfs(0, visited)
