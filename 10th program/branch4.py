def branch_bound(row, used, cost_so_far, path):
    global min_cost, answer

    if row == n:
        if cost_so_far < min_cost:
            min_cost = cost_so_far
            answer = path.copy()
        return

    if cost_so_far >= min_cost:
        return

    for col in range(n):

        if not used[col]:

            used[col] = True
            path.append(col)

            branch_bound(
                row + 1,
                used,
                cost_so_far + cost[row][col],
                path
            )

            path.pop()
            used[col] = False


n = int(input("Enter number of employees: "))

cost = []

for i in range(n):
    print("Enter costs for Employee", i + 1)
    cost.append(list(map(int, input().split())))

min_cost = 999999
answer = []

branch_bound(0, [False] * n, 0, [])

print("\nMinimum Cost:", min_cost)

print("Job Allocation:")

for i in range(n):
    print("Employee", i + 1, "-> Job", answer[i] + 1)