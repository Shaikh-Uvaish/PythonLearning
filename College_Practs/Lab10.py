class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_rec(self.root, value)

    def _insert_rec(self, root, value):
        if root is None:
            return Node(value)
        if value < root.value:
            root.left = self._insert_rec(root.left, value)
        elif value > root.value:
            root.right = self._insert_rec(root.right, value)
        return root

    def search(self, value):
        return self._search_rec(self.root, value)

    def _search_rec(self, root, value):
        if root is None:
            return False
        if root.value == value:
            return True
        elif value < root.value:
            return self._search_rec(root.left, value)
        else:
            return self._search_rec(root.right, value)

    def delete(self, value):
        self.root = self._delete_rec(self.root, value)

    def _delete_rec(self, root, value):
        if root is None:
            return root
        if value < root.value:
            root.left = self._delete_rec(root.left, value)
        elif value > root.value:
            root.right = self._delete_rec(root.right, value)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_node = self._min_value_node(root.right)
            root.value = min_node.value
            root.right = self._delete_rec(root.right, min_node.value)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder_rec(self.root, result)
        return result

    def _inorder_rec(self, root, result):
        if root:
            self._inorder_rec(root.left, result)
            result.append(root.value)
            self._inorder_rec(root.right, result)

    def preorder(self):
        result = []
        self._preorder_rec(self.root, result)
        return result

    def _preorder_rec(self, root, result):
        if root:
            result.append(root.value)
            self._preorder_rec(root.left, result)
            self._preorder_rec(root.right, result)

    def postorder(self):
        result = []
        self._postorder_rec(self.root, result)
        return result

    def _postorder_rec(self, root, result):
        if root:
            self._postorder_rec(root.left, result)
            self._postorder_rec(root.right, result)
            result.append(root.value)

if __name__ == "__main__":
    bst = BinarySearchTree()

    while True:
        print("\n--- Binary Search Tree Operations ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display Inorder")
        print("5. Display Preorder")
        print("6. Display Postorder")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = int(input("Enter value to insert: "))
            bst.insert(val)
        elif choice == 2:
            val = int(input("Enter value to delete: "))
            bst.delete(val)
        elif choice == 3:
            val = int(input("Enter value to search: "))
            found = bst.search(val)
            if found:
                print(f"Value {val} found in the BST.")
            else:
                print(f"Value {val} not found in the BST.")
        elif choice == 4:
            print("Inorder Traversal:", bst.inorder())
        elif choice == 5:
            print("Preorder Traversal:", bst.preorder())
        elif choice == 6:
            print("Postorder Traversal:", bst.postorder())
        elif choice == 7:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")
