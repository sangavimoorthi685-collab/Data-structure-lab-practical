def assign(employee, used, total, assignment):
    global minimum

    if employee == n:
        if total < minimum:
            minimum = total
            result[:] = assignment
        return

    if total >= minimum:
        return

    for job in range(n):
        if not used[job]:

            used[job] = True
            assignment.append(job)

            assign(
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
    print("Employee", i + 1)
    row = list(map(int, input("Enter job costs: ").split()))
    cost.append(row)

minimum = 999999
result = []

assign(0, [False] * n, 0, [])

print("\nMinimum Cost:", minimum)

for i in range(n):
    print("Employee", i + 1, "-> Job", result[i] + 1)