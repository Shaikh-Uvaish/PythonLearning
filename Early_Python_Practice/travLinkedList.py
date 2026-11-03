            #Traversal Operation in Linked-List#

class Node:
    def __init__(self,data):
     self.data = data 
     self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def traverse(self):
        current = self.head
        if current is None:
            print("Linked-list is empty")
            return
        print("Linked-list Elements ", end=' ')
        while current is not None:
            print(current.data, end=' ')
            current = current.next

a = LinkedList()
a.insertAtEnd(10)
a.insertAtEnd(20)
a.insertAtEnd(30)
a.traverse()