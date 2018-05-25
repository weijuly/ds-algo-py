class Node:
    def __init__(self, data, prev=None, next=None):
        self.data, self.prev, self.next = data, prev, next

    def __repr__(self):
        p = str(self.prev.data) if self.prev else '|'
        n = str(self.next.data) if self.next else '|'
        return '%s => %d => %s' % (p, self.data, n)


def getHead(node):
    if not node:
        return None
    while node.prev:
        node = node.prev
    return node


def getLength(node):
    node, length = getHead(node), 0
    while node:
        length += 1
        node = node.next
    return length


def getLengthRecursive(node):
    def helper(node):
        if not node:
            return 0
        return 1 + helper(node.next)

    return helper(getHead(node))


def reverse(node):
    head = getHead(node)
    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        curr.prev = next
        prev = curr
        curr = next
    return prev


def equals(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    while a and b:
        if a.data != b.data:
            return False
        a, b = a.next, b.next
    return True
