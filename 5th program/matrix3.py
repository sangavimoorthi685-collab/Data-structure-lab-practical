graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

visited = []
queue = []

start = 0

queue.append(start)
visited.append(start)

while queue:

    vertex = queue.pop(0)

    print(vertex, end=" ")

    for neighbour in graph[vertex]:

        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
