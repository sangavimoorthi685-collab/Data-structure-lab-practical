n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

for i in range(e):
    u, v, w = map(int, input("Enter source, destination, weight: ").split())
    edges.append([w, u, v])

edges.sort()

parent = list(range(n))

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

total = 0

print("\nMinimum Spanning Tree:")

for w, u, v in edges:
    a = find(u)
    b = find(v)

    if a != b:
        print(u, "-", v, "=", w)
        total += w
        parent[b] = a

print("Minimum Cost:", total)