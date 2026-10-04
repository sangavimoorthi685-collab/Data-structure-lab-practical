
graph = [
    [0, 2, 3, 0],
    [2, 0, 1, 4],
    [3, 1, 0, 5],
    [0, 4, 5, 0]
]

n = 4
visited = [False] * n
visited[0] = True

print("Edges in Minimum Spanning Tree:")

total = 0

for i in range(n - 1):

    minimum = 999
    x = 0
    y = 0

    for j in range(n):
        if visited[j]:

            for k in range(n):
                if not visited[k] and graph[j][k] != 0:

                    if graph[j][k] < minimum:
                        minimum = graph[j][k]
                        x = j
                        y = k
    print(x, "-", y, "=", minimum)
    total = total + minimum
    visited[y] = True
print("Minimum Cost:", total)
