class Solution():
    def __init__(self, head):
        self.head = head

    def reversell(self):
        curr = self.head
        prev = None
        
        while curr is not None:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node

        return prev

# using recursion 

def reverse_ll(head):
    if head is None or head.next is None:
        return head

    newnode = reverse_ll(head.next)
    front = head.next 
    front.next = head
    head.next = None

    return newnode

    
