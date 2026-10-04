edges = [
    (1, 1, 2),
    (2, 0, 1),
    (3, 0, 2),
    (4, 1, 3),
    (5, 2, 3)
]

edges.sort()
parent = [0, 1, 2, 3]
def find(x):
    while parent[x] != x:
        x = parent[x]
    return x
total = 0
print("Edges in Minimum Spanning Tree:")
for weight, u, v in edges:

    root1 = find(u)
    root2 = find(v)

    if root1 != root2:

        print(u, "-", v, "=", weight)

        total = total + weight

        parent[root2] = root1

print("Minimum Cost:", total)
