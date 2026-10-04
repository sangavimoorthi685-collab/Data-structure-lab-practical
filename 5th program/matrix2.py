n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    graph[i] = []

edges = int(input("Enter number of edges: "))

for i in range(edges):
    u = int(input("Enter starting vertex: "))
    v = int(input("Enter ending vertex: "))

    graph[u].append(v)
    graph[v].append(u)

print("\nAdjacency List:")

for vertex in graph:
    print(vertex, "->", graph[vertex])
