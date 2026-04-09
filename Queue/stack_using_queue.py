# Implement a stack using queue the queue shoulf work like a stack a stack follows LIFO principle same the queue should follow 

class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0


# another approach 


class MyStack:
    def __init__(self):
        self.q = []  # normal list as queue

    def push(self, x: int) -> None:
        # enqueue new element
        self.q.append(x)
        # rotate all previous elements behind it
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.pop(0))

    def pop(self) -> int:
        # front of the queue is the top of the stack
        return self.q.pop(0)

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
