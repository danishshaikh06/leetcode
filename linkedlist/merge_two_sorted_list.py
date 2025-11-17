'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]       
'''
# Define a Node class for the linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data    # Store the value of the node
        self.next = next    # Pointer to the next node (None if end of list)


# Function to merge two sorted linked lists
def merge_sorted_lists(list1: Node, list2: Node) -> Node:
    # Create a dummy node as a starting point
    # This helps simplify edge cases (like empty lists)
    dummy = Node(0)
    tail = dummy  # Tail pointer will build the new merged list

    # Loop until one of the lists runs out
    while list1 and list2:
        # Compare current nodes of both lists
        if list1.data < list2.data:
            tail.next = list1  # Append list1 node to merged list
            list1 = list1.next # Move to the next node in list1
        else:
            tail.next = list2  # Append list2 node to merged list
            list2 = list2.next # Move to the next node in list2
        tail = tail.next      # Move tail to the last node in merged list

    # After loop, one of the lists may still have nodes left
    # Append remaining nodes to merged list
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    # Return the head of the merged list (skip dummy)
    return dummy.next


# Example: Create two sorted linked lists

# List 1: 1 -> 3 -> 5
l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)

# List 2: 2 -> 4 -> 6
l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)


# Merge the two lists
merged_head = merge_sorted_lists(l1, l2)

# Print the merged linked list
current = merged_head
while current:
    print(current.data, end=" -> " if current.next else "\n")
    current = current.next
