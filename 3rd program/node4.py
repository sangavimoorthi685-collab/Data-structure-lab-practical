class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def is_operator(value):
    return value in "+-*/"
def construct_expression_tree(expression):
    stack = []
    for symbol in expression:

        if not is_operator(symbol):
            node = Node(symbol)
            stack.append(node)
        else:
            node = Node(symbol)

            node.right = stack.pop()
            node.left = stack.pop()

            stack.append(node)

    return stack[-1]
def inorder(root):
    if root is not None:
        if is_operator(root.data):
            print("(", end="")
        inorder(root.left)
        print(root.data, end="")
        inorder(root.right)
        if is_operator(root.data):
            print(")", end="")
expression = "ab+c*"
root = construct_expression_tree(expression)
print("Postfix Expression:", expression)
print("Inorder Expression:")
inorder(root)
