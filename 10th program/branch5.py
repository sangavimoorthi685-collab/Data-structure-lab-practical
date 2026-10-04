from itertools import permutations

n = int(input("Enter number of employees: "))

cost = []

for i in range(n):
    cost.append(list(map(int, input("Enter costs: ").split())))

best_cost = 999999
best = None

for assignment in permutations(range(n)):

    total = 0

    for employee in range(n):
        job = assignment[employee]
        total += cost[employee][job]

    if total < best_cost:
        best_cost = total
        best = assignment

print("\nBest Assignment:")

for i in range(n):
    print("Employee", i + 1, "-> Job", best[i] + 1)

print("Minimum Total Cost:", best_cost)