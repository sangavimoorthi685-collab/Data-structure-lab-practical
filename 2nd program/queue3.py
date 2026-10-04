queue = []

while True:
    print("\n----- QUEUE MENU -----")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the element to insert: "))
        queue.append(value)
        print("Element inserted successfully.")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            deleted = queue.pop(0)
            print("Deleted element:", deleted)

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Queue elements:", end=" ")
            for item in queue:
                print(item, end=" ")
            print()

    elif choice == 4:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
