n = int(input("Enter number of vertices: "))

graph = []

print("Enter the weighted graph:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

visited = [False] * n
visited[0] = True

total = 0

print("\nMinimum Spanning Tree:")

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
