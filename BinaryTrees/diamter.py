# Diameter of Binary tree 
# building a tree
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


  def height(self,root):
    if root == None:
      return 0

    left_ht = self.height(root.left)
    right_ht = self.height(root.right)
    self.ans = max(left_ht + right_ht, self.ans)

    return max(left_ht,right_ht) + 1 

  def diam(self,root):
    self.height(root)
    return self.ans 

build = tree()
preorder = [1,2,-1,-1,3,4,-1,-1,5,-1,-1]

Tree = build.buildtree(preorder)
diameter = build.diam(Tree)
print(diameter)
  