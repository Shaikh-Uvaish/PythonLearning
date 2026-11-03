class Queue:
    def __init__(self):
        self.capacity = 5
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self, item):
        if self.count == self.capacity:
            print("Queue Overflow! Cannot insert", item)
            return
        self.rear += 1
        self.queue[self.rear] = item
        self.count += 1
        print(f"Enqueued element: {item}")


    def dequeue(self):
        if self.count == 0:
            print("Queue Underflow! Cannot dequeue.")
            return
        item = self.queue[self.front]

        for i in range(1, self.count):
            self.queue[i - 1] = self.queue[i]
        self.queue[self.rear] = None
        self.rear -= 1
        self.count -= 1
        print(f"Dequeued element: {item}")


    def display(self):
        print("Queue:", end=" ")
        for i in range(self.count):
            print(self.queue[i], end=" ")
        print()


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)  
q.display()
q.dequeue()
q.display()
