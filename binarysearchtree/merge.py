class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Inorder traversal
def inorder(root, arr):
    if not root:
        return
    inorder(root.left, arr)
    arr.append(root.val)
    inorder(root.right, arr)

# Merge two sorted arrays
def merge(arr1, arr2):
    i = j = 0
    merged = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    
    return merged

# Convert sorted array to BST
def sorted_array_to_bst(arr):
    if not arr:
        return None
    
    mid = len(arr) // 2
    root = Node(arr[mid])
    
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid+1:])
    
    return root


def merge_bsts(root1, root2):
    arr1, arr2 = [], []
    
    inorder(root1, arr1)
    inorder(root2, arr2)
    
    merged_arr = merge(arr1, arr2)
    
    return sorted_array_to_bst(merged_arr)