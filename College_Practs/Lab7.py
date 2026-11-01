class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size  

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            temp = self.table[index]
            while temp:
                if temp.key == key:
                    temp.value = value 
                    print(f"🔁 Key {key} updated with new value '{value}'")
                    return
                if temp.next is None:
                    break
                temp = temp.next
            temp.next = new_node

        print(f"✅ Inserted key: {key}, value: {value} at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        temp = self.table[index]
        while temp:
            if temp.key == key:
                print(f"🔍 Found -> Key: {key}, Value: {temp.value}")
                return temp.value
            temp = temp.next
        print(f"⚠️ Key {key} not found.")
        return None

    def delete(self, key):
        index = self.hash_function(key)
        temp = self.table[index]
        prev = None

        while temp:
            if temp.key == key:
                if prev:
                    prev.next = temp.next
                else:
                    self.table[index] = temp.next
                print(f"🗑️ Key {key} deleted successfully.")
                return
            prev = temp
            temp = temp.next

        print(f"⚠️ Key {key} not found, nothing to delete.")

    def display(self):
        print("\n📋 Hash Table Contents:")
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            temp = self.table[i]
            if temp is None:
                print("Empty")
            else:
                chain = []
                while temp:
                    chain.append(f"({temp.key}, {temp.value})")
                    temp = temp.next
                print(" -> ".join(chain))


def main():
    ht = HashTable()

    while True:
        print("\n========= Hash Table Menu =========")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display Table")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            key = int(input("Enter key (integer): "))
            value = input("Enter value: ")
            ht.insert(key, value)

        elif choice == '2':
            key = int(input("Enter key to search: "))
            ht.search(key)

        elif choice == '3':
            key = int(input("Enter key to delete: "))
            ht.delete(key)

        elif choice == '4':
            ht.display()

        elif choice == '5':
            print("\n👋 Exiting... Thank you for using the Hash Table!")
            break

        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
