# 333 -> Largest BST 

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def largestBST(root):
    max_size = 0

    def helper(node):
        nonlocal max_size
        
        # return: (isBST, size, min, max)
        if not node:
            return True, 0, float('inf'), float('-inf')

        left_isBST, left_size, left_min, left_max = helper(node.left)
        right_isBST, right_size, right_min, right_max = helper(node.right)

        if left_isBST and right_isBST and left_max < node.val < right_min:
            size = left_size + right_size + 1
            max_size = max(max_size, size)

            return True, size, min(left_min, node.val), max(right_max, node.val)
        else:
            return False, 0, 0, 0

    helper(root)
    return max_size