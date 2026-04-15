# Top view of binary tree
class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right= None

class tree:
  def __init__(self):
    self.idx = -1
    self.ans = 0 

  def buildtree(self,preorder):
    self.idx +=1

    if preorder[self.idx] == -1:
      return None

    node = Node(preorder[self.idx])
    node.left = self.buildtree(preorder)
    node.right = self.buildtree(preorder)

    return node

# Top view of binary tree
from collections import deque
def topview(root):
  dq = deque()
  my_dict = {}
  dq.append((root,0))

  while(len(dq)> 0):
    curr = dq[0][0]
    currhd= dq[0][1]
    dq.popleft()

    if currhd not in my_dict:
      my_dict[currhd] = curr.data

    if curr.left:
      dq.append((curr.left,currhd-1))

    if curr.right:
      dq.append((curr.right,currhd+1))

  for key, val in sorted(my_dict.items()):
    print(val)

build = tree()
preorder = [1,2,-1,-1,3,4,-1,-1,5,-1,-1]

Tree = build.buildtree(preorder)
topview(Tree)
