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

    print("Inserted element:", value)


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

insert(10)
insert(20)
insert(30)
insert(40)
display()
