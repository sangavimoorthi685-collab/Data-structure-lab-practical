class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            print("Popped:", self.stack.pop())
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Top:", self.stack[-1])
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Stack:", s.stack)
s.peek()
s.pop()
s.peek()
