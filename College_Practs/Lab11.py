class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None

    def is_operator(self, c):
        return c in ['+', '-', '*', '/', '^']

    def construct_from_prefix(self, prefix):
        stack = []
        for symbol in reversed(prefix):
            if not self.is_operator(symbol):
                node = Node(symbol)
                stack.append(node)
            else:
                node = Node(symbol)
                left = stack.pop()
                right = stack.pop()
                node.left = left
                node.right = right
                stack.append(node)

        self.root = stack[-1]

    def postorder_non_recursive(self):
        if self.root is None:
            return []

        stack1 = []
        stack2 = []
        stack1.append(self.root)

        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        postorder_result = []
        while stack2:
            node = stack2.pop()
            postorder_result.append(node.value)
        return postorder_result

    def delete_tree(self):
        self.root = None
        print("Expression Tree deleted successfully!")

if __name__ == "__main__":
    et = ExpressionTree()
    expression = input("Enter Prefix Expression (e.g. +--a*bc/def): ")

    et.construct_from_prefix(expression)
    print("\nExpression Tree constructed successfully!")

    postorder_result = et.postorder_non_recursive()
    print("Non-Recursive Postorder Traversal:", ''.join(postorder_result))

    et.delete_tree()
