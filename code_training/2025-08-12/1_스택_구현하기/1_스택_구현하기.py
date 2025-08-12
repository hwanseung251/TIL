class Stack:
    def __init__(self, size):
        self.size = size
        self.capacity =  [None] * size
        self.top = -1

    def push(self, item):
        if self.top >= self.size - 1:
            return "Stack Overflow"
        self.top += 1
        self.capacity[self.top] = item

    def is_empty(self):
        return self.top == -1

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        item = self.capacity[self.top]
        self.capacity[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.capacity[self.top]
    