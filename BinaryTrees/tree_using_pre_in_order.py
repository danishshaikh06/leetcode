class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None

def buildTree(preorder, inorder):
    inorder_map = {val: i for i, val in enumerate(inorder)}
    pre_idx = 0
  

    def helper(left, right):
        nonlocal pre_idx

        if left > right:
            return None

        root_val = preorder[pre_idx]
        pre_idx += 1
        root = Node(root_val)

        mid = inorder_map[root_val]

        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)

        return root

    return helper(0, len(inorder) - 1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = buildTree(preorder, inorder)
print(root.data)  # Output: 3
print(root.left.data)  # Output: 9
print(root.right.data)  # Output: 20
print(root.right.left.data)  # Output: 15
print(root.right.right.data)  # Output: 7

