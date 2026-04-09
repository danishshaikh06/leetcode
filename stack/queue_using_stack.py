# implement queue using stack 

class MyQueue(object):

    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.pop(0)
      
    def peek(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0
        
# another approach
class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        
    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
      
    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack