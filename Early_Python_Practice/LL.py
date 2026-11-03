class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("The Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

    def addAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def addAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def delAtBegin(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.next




L = LinkedList()
L.addAtBegin(10)
L.addAtBegin(20)
L.addAtEnd(5)
L.delAtBegin()
L.print_LL()
