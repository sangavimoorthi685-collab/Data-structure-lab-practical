stack = []
def push():
    x = int(input("Enter element: "))
    stack.append(x)
    print("Pushed:", x)
def pop():
    if not stack:
        print("Stack Underflow")
    else:
        print("Popped:", stack.pop())
def peek():
    if not stack:
        print("Stack is Empty")
    else:
        print("Top element:", stack[-1])

def display():
    if not stack:
        print("Stack is Empty")
    else:
        print("Stack:", stack)
while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
