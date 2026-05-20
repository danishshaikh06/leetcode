def flatten(head):
    if head is None:
        return head

    curr = head

    while curr is not None:
        if curr.child is not None:
            next_node = curr.next

            child_head = flatten(curr.child)

            curr.next = child_head
            child_head.prev = curr
            curr.child = None

            tail = child_head
            while tail.next is not None:
                tail = tail.next

            tail.next = next_node

            if next_node is not None:
                next_node.prev = tail

        curr = curr.next

    return head