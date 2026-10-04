n = int(input("Enter number of vertices: "))

graph = [[0 for j in range(n)] for i in range(n)]

edges = int(input("Enter number of edges: "))

for i in range(edges):
    u = int(input("Enter starting vertex: "))
    v = int(input("Enter ending vertex: "))

    graph[u][v] = 1
    graph[v][u] = 1

print("\nAdjacency Matrix:")

for row in graph:
    print(row)
