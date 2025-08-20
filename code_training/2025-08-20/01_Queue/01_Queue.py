class Queue:
    def __init__(self, capacity):
        self.capacity = capacity + 1
        self.items = [None] * self.capacity

        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return

        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        self.front = (self.front + 1) % self.capacity

        return self.items[self.front]

q = Queue(3)

# 1, 2, 3을 차례로 큐에 삽입 (enqueue)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# 큐에서 세 개의 데이터를 차례로 꺼내서 출력 (dequeue)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())