# 99. Recover Binary Search Tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def recover_bst(root):
    current = root
    prev = first = second = None

    while current:
        if current.left is None:
            # Visit node
            if prev and current.val < prev.val:
                if not first:
                    first = prev
                second = current
            
            prev = current
            current = current.right

        else:
            # Find inorder predecessor
            pred = current.left
            while pred.right and pred.right != current:
                pred = pred.right

            if pred.right is None:
                # Create thread
                pred.right = current
                current = current.left
            else:
                # Remove thread
                pred.right = None

                # Visit node
                if prev and current.val < prev.val:
                    if not first:
                        first = prev
                    second = current

                prev = current
                current = current.right

    # Fix swapped nodes
    if first and second:
        first.val, second.val = second.val, first.val