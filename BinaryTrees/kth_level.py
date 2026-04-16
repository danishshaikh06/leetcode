# kth level of the binary tree
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

  def kth(self,root,k):
    if root is None:
      return  

    if k == 1 :
      print(root.data)
      return

    self.kth(root.left,k-1)
    self.kth(root.right,k-1)

build = tree()

preorder = [1,2,-1,-1,3,4,-1,-1,5,-1,-1]

Tree = build.buildtree(preorder)
build.kth(Tree,3)



