class CityNode:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.left = None
        self.right = None

class CityBST:
    def __init__(self):
        self.root = None

    def insert(self, name, population):
        self.root = self._insert_rec(self.root, name, population)

    def _insert_rec(self, root, name, population):
        if root is None:
            return CityNode(name, population)
        if name < root.name:
            root.left = self._insert_rec(root.left, name, population)
        elif name > root.name:
            root.right = self._insert_rec(root.right, name, population)
        else:
            print(f"⚠️ City {name} already exists. Use update to change population.")
        return root

    def search(self, name):
        return self._search_rec(self.root, name)

    def _search_rec(self, root, name):
        if root is None:
            return None
        if name == root.name:
            return root
        elif name < root.name:
            return self._search_rec(root.left, name)
        else:
            return self._search_rec(root.right, name)

    def update(self, name, population):
        node = self.search(name)
        if node:
            node.population = population
            print(f"✅ Updated {name}'s population to {population}.")
        else:
            print(f"⚠️ City {name} not found!")

    def delete(self, name):
        self.root = self._delete_rec(self.root, name)

    def _delete_rec(self, root, name):
        if root is None:
            print(f"⚠️ City {name} not found!")
            return root
        if name < root.name:
            root.left = self._delete_rec(root.left, name)
        elif name > root.name:
            root.right = self._delete_rec(root.right, name)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_node = self._min_value_node(root.right)
            root.name = min_node.name
            root.population = min_node.population
            root.right = self._delete_rec(root.right, min_node.name)
        print(f"🗑️ City {name} deleted successfully.")
        return root

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder_rec(self.root, result)
        return result

    def _inorder_rec(self, root, result):
        if root:
            self._inorder_rec(root.left, result)
            result.append((root.name, root.population))
            self._inorder_rec(root.right, result)

    def descending(self):
        result = []
        self._descending_rec(self.root, result)
        return result

    def _descending_rec(self, root, result):
        if root:
            self._descending_rec(root.right, result)
            result.append((root.name, root.population))
            self._descending_rec(root.left, result)

    def max_comparisons(self):
        height = self._height(self.root)
        print(f"🔹 Maximum comparisons required to search a city: {height}")
        return height

    def _height(self, root):
        if root is None:
            return 0
        left_h = self._height(root.left)
        right_h = self._height(root.right)
        return 1 + max(left_h, right_h)

def main():
    bst = CityBST()

    while True:
        print("\n--- City BST Menu ---")
        print("1. Add City")
        print("2. Delete City")
        print("3. Update Population")
        print("4. Display Cities Ascending")
        print("5. Display Cities Descending")
        print("6. Maximum Comparisons to Search")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter city name: ")
            pop = int(input("Enter population: "))
            bst.insert(name, pop)

        elif choice == '2':
            name = input("Enter city name to delete: ")
            bst.delete(name)

        elif choice == '3':
            name = input("Enter city name to update: ")
            pop = int(input("Enter new population: "))
            bst.update(name, pop)

        elif choice == '4':
            print("\n📈 Cities in Ascending Order:")
            for city, pop in bst.inorder():
                print(f"{city}: {pop}")

        elif choice == '5':
            print("\n📉 Cities in Descending Order:")
            for city, pop in bst.descending():
                print(f"{city}: {pop}")

        elif choice == '6':
            bst.max_comparisons()

        elif choice == '7':
            print("👋 Exiting program...")
            break

        else:
            print("❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
