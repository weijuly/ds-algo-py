from leetcode.utils import timer


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


@timer
def merge(lists):
    if len(lists) == 0:
        return None
    if len(lists) == 1:
        return lists[0]
    head, curr = None, None
    while True:
        candidates = {lists[x].val: x for x in range(len(lists)) if lists[x]}
        if not candidates:
            return head
        i = candidates[sorted(candidates.keys())[0]]
        if not head:
            head = lists[i]
            curr = head
        else:
            curr.next = lists[i]
            curr = curr.next
        lists[i] = lists[i].next


head = merge([
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
])
