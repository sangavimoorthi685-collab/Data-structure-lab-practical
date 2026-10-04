class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_operator(value):
    return isinstance(value, str) and value in "+-*/"


def construct_tree(expression):
    stack = []

    for symbol in expression:

        # Operator
        if symbol in "+-*/":
            node = Node(symbol)

            node.right = stack.pop()
            node.left = stack.pop()

            stack.append(node)

        # Operand
        else:
            node = Node(int(symbol))
            stack.append(node)

    return stack.pop()


def evaluate(root):

    # Operand
    if root.left is None and root.right is None:
        return root.data

    left = evaluate(root.left)
    right = evaluate(root.right)

    if root.data == "+":
        return left + right

    elif root.data == "-":
        return left - right

    elif root.data == "*":
        return left * right

    elif root.data == "/":
        return left / right


def inorder(root):

    if root is None:
        return

    if is_operator(root.data):
        print("(", end="")

    inorder(root.left)

    print(root.data, end="")

    inorder(root.right)

    if is_operator(root.data):
        print(")", end="")


# Main Program

expression = "234*+"

print("Postfix Expression:", expression)

root = construct_tree(expression)

print("Inorder Expression:", end=" ")
inorder(root)

result = evaluate(root)

print("\nResult:", result)
