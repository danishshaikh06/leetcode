def reverse(head, k):
    if head is None:
        return None

    temp = head
    count = 0

    # check if k nodes exist
    while temp and count < k:
        temp = temp.next
        count += 1

    if count < k:
        return head

    # reverse next groups first
    start_node = reverse(temp, k)

    temp = head
    count = 0

    while count < k:
        next_node = temp.next
        temp.next = start_node
        start_node = temp
        temp = next_node
        count += 1

    return start_node