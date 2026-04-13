# 572. Subtree of Another Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isIdentical(self, root1, root2):

        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False

        return (self.isIdentical(root1.left, root2.left) and
                self.isIdentical(root1.right, root2.right))

    def isSubtree(self, root, subroot):
        
        if subroot == None:
            return True

        if root == None:
            return False

        if self.isIdentical(root,subroot):
            return True

        return (self.isSubtree(root.left,subroot) or
          self.isSubtree(root.right,subroot))

    