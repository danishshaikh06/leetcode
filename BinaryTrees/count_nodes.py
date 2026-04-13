class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right= None

class tree:
  def __init__(self):
    self.idx = -1

  def buildtree(self,preorder):
    self.idx +=1

    if preorder[self.idx] == -1:
      return None

    node = Node(preorder[self.idx])
    node.left = self.buildtree(preorder)
    node.right = self.buildtree(preorder)

    return node

# Count of Nodes
  def count(self, root):
    if root == None:
      return 0

    left_count = self.count(root.left)
    right_count = self.count(root.right)

    return left_count + right_count + 1