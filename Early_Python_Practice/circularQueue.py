class Queue:
    def __init__(self):
        self.capacity = 5
        self.values = []

    def enqueue(self, x):
        if len(self.values) == self.capacity:
            print("Queue is Full! Cannot insert", x)
        else:
            self.values.append(x)
            print(f"Enqueued: {x}")

    def dequeue(self):
        if len(self.values) == 0:
            print("Queue is Empty! Nothing to dequeue.")
            return None
        front = self.values[0]
        self.values = self.values[1:]
        print(f"Dequeued: {front}")
        return front

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)

print("Current Queue:", q.values)

q.dequeue()
print("After Dequeue:", q.values)
