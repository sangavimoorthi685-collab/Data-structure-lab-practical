queue = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    queue.append(value)

print("\nOriginal Queue:")
print(queue)

if len(queue) == 0:
    print("Queue is Empty")
else:
    deleted = queue.pop(0)

    print("\nDeleted element:", deleted)
    print("Queue after deletion:")

    for item in queue:
        print(item, end=" ")
