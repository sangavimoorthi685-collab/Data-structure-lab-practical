from itertools import permutations

n = int(input("Enter number of employees: "))

cost = []

for i in range(n):
    row = list(map(int, input("Enter costs: ").split()))
    cost.append(row)

minimum = 999999

for jobs in permutations(range(n)):
    total = 0

    for i in range(n):
        total += cost[i][jobs[i]]

    if total < minimum:
        minimum = total
        best = jobs

print("Minimum Cost:", minimum)
print("Assignment:")

for i in range(n):
    print("Employee", i + 1, "-> Job", best[i] + 1)