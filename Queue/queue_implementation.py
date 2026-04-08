# queue 

class Node:
  def __init__(self,data):
    self.data = data 
    self.next = None


class Queue:
  def __init__(self):
    self.head = self.tail = None 

  def push(self,data):
    newnode = Node(data)

    if self.empty():
      self.head = self.tail = newnode
    else:
      self.tail.next = newnode
      self.tail = newnode

  def pop(self):
    if self.empty():
      return -1
    else:
      temp = self.head
      self.head = temp.next
      del temp 
      #if self.head is None:
        #self.tail = None
      #return data



  def front(self):
    if self.empty():
      return -1 
    else:
      return self.head.data

  def empty(self):
    return self.head is None


q = Queue()

q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)

print('the front is',q.front())

while q.empty() is False:
  print(q.front())
  q.pop()
