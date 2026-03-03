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


