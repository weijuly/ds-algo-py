class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def reverse(node):
    if not node or not node.next:
        return node
    prev, curr = None, node
    while curr:
        next = curr.next
        curr.next = prev
        prev, curr = curr, next
    return prev, node


def reverse_k_group(head, k):
    if k < 2:
        return head
    curr = head
    modified_head = None
    prev_group_tail = None
    while curr:
        curr_group_head = curr
        for i in range(k - 1):
            if curr:
                curr = curr.next
        if not curr:
            break
        next_group_head = curr.next
        curr.next = None
        curr_group_head, curr_group_tail = reverse(curr_group_head)
        curr_group_tail.next = next_group_head
        curr = next_group_head
        if not modified_head:
            modified_head = curr_group_head
        if prev_group_tail:
            prev_group_tail.next = curr_group_head
        prev_group_tail = curr_group_tail
    return modified_head


head = reverse_k_group(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3)
