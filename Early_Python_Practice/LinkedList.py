class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.lastNode = None

    def insert_at_end(self, data):
        # If list is empty
        if self.head is None:
            self.head = Node(data)
            self.lastNode = self.head
        else:
            self.lastNode.next = Node(data)
            self.lastNode = self.lastNode.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next


# ---- Driver code ----
a = LinkedList()
n = int(input("How many elements would you like to add? "))

for i in range(n):
    data = int(input("Enter data item: "))
    a.insert_at_end(data)

print("The linked list: ", end='')
a.display()
