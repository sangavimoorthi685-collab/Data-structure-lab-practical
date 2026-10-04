n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
edges = []
print("Enter edges as: source destination weight")
for i in range(e):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
edges.sort()
parent = list(range(n))
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
total = 0
count = 0
print("\nMinimum Spanning Tree:")
for w, u, v in edges:
    root1 = find(u)
    root2 = find(v)
    if root1 != root2:
        print(u, "-", v, "=", w)
        total = total + w
        parent[root2] = root1
        count = count + 1
        if count == n - 1:
            break
print("Minimum Cost:", total)
