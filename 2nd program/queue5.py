size = 5
queue = [0] * size

front = -1
rear = -1
def insert(value):
    global front, rear
    if (rear + 1) % size == front:
        print("Circular Queue is Full")
        return
    if front == -1:
        front = 0
    rear = (rear + 1) % size

    queue[rear] = value

    print("Inserted:", value)


# Function to delete an element
def delete():
    global front, rear

    # Check for Empty condition
    if front == -1:
        print("Circular Queue is Empty")
        return

    deleted = queue[front]

    print("Deleted:", deleted)

    # If only one element exists
    if front == rear:
        front = -1
        rear = -1

    else:
        # Move front circularly
        front = (front + 1) % size


# Function to display queue
def display():
    if front == -1:
        print("Circular Queue is Empty")
        return

    print("Circular Queue:", end=" ")

    i = front

    while True:
        print(queue[i], end=" ")

        if i == rear:
            break

        i = (i + 1) % size

    print()


# Main Program

print("----- CIRCULAR QUEUE -----")

insert(10)
insert(20)
insert(30)
insert(40)

print("\nQueue after insertion:")
display()

print("\nPerforming deletion:")
delete()
delete()

print("\nQueue after deletion:")
display()

print("\nInserting new elements:")
insert(50)
insert(60)

print("\nFinal Circular Queue:")
display()
