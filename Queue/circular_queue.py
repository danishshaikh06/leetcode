class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.front = -1
        self.rear = -1

    def push(self, x):
        if (self.rear + 1) % self.capacity == self.front:
            print("Full")
            return
        
        if self.front == -1:
            self.front = 0
        
        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = x

    def pop(self):
        if self.front == -1:
            print("Empty")
            return
        data = self.arr[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return data

    def peek(self):
        if self.front == -1:
            return -1
        return self.arr[self.front]