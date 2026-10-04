def solve(cost, employee, used, total, assignment):
    global best_cost, best_assignment

    n = len(cost)

    if employee == n:
        if total < best_cost:
            best_cost = total
            best_assignment = assignment.copy()
        return

    if total >= best_cost:
        return

    for job in range(n):
        if not used[job]:

            used[job] = True
            assignment.append(job)

            solve(
                cost,
                employee + 1,
                used,
                total + cost[employee][job],
                assignment
            )

            assignment.pop()
            used[job] = False


n = int(input("Enter number of employees: "))

cost = []

for i in range(n):
    cost.append(list(map(int, input("Enter costs: ").split())))

best_cost = 999999
best_assignment = []

solve(cost, 0, [False] * n, 0, [])

print("Minimum Cost:", best_cost)

for i in range(n):
    print("Employee", i + 1, "-> Job", best_assignment[i] + 1)