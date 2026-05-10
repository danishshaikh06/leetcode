'''783. Minimum Distance Between BST Nodes
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.'''

class Solution:
    def __init__(self):
        self.prev = None
        self.ans = float('inf')

    def inorder(self, node):
        if not node:
            return

        self.inorder(node.left)

        if self.prev is not None:
            self.ans = min(self.ans, node.val - self.prev)

        self.prev = node.val

        self.inorder(node.right)

    def mindist(self, root):
        self.inorder(root)
        return self.ans
