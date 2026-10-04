
queue = []

n = int(input("Enter the number of elements: "))
for i in range(n):

    value = int(input("Enter element: "))
    queue.append(value)
    
print("\nQueue after insertion:")
for item in queue:
    print(item, end=" ")
