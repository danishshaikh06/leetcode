def nodes_pair(head):
    
    if head is None or head.next is None:
        return head

    prev = None
    first = head
    second = head.next

    while first and second:

        third = second.next

        # swap
        second.next = first
        first.next = third

        if prev:
            prev.next = second
        else:
            head = second

        # move pointers
        prev = first
        first = third

        if first:
            second = first.next
        else:
            second = None

    return head