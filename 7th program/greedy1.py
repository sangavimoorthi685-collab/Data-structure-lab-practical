n = int(input("Enter number of items: "))

items = []

for i in range(n):
    value, weight = map(int, input("Enter value and weight: ").split())
    ratio = value / weight
    items.append((ratio, value, weight))

capacity = int(input("Enter capacity: "))

items.sort(reverse=True)

profit = 0

for ratio, value, weight in items:
    if capacity >= weight:
        capacity -= weight
        profit += value
    else:
        profit += ratio * capacity
        break

print("Maximum Profit:", profit)