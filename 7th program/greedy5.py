n = int(input("Enter number of items: "))

items = []

for i in range(n):
    value, weight = map(int, input("Enter value and weight: ").split())
    ratio = value / weight
    items.append((ratio, value, weight, i + 1))

capacity = int(input("Enter capacity: "))

items.sort(reverse=True)

profit = 0

print("\nSelected Items:")

for ratio, value, weight, number in items:
    if weight <= capacity:
        print("Item", number)
        profit += value
        capacity -= weight

print("Maximum Profit:", profit)