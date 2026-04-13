# Identical trees 
def identical(self,tree1,tree2):
    if tree1 == None and tree2 == None:
      return True

    if tree1 == None or tree2 == None:
      return False

    left_identical = self.identical(tree1.left,tree2.left)
    right_identical = self.identical(tree1.right,tree2.right)

    return left_identical and right_identical
