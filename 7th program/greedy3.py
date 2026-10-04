n = int(input("Enter number of items: "))

items = []

for i in range(n):
    value = int(input("Enter value: "))
    weight = int(input("Enter weight: "))
    items.append((value / weight, value, weight))

capacity = int(input("Enter capacity: "))

items.sort(reverse=True)

profit = 0

for ratio, value, weight in items:
    if weight <= capacity:
        profit += value
        capacity -= weight

print("Maximum Profit:", profit)