class Node:
    def __init__(self, data, n=None):
        self.data, self.next = data, n

    def __repr__(self):
        return '%d' % self.data


def toString(node):
    string = ''
    while node:
        string += ('%d => ' % node.data)
        node = node.next
    string += '|'
    return string


def getLength(node):
    length = 0
    while node:
        length += 1
        node = node.next
    return length


def getLengthRecursive(node):
    if not node:
        return 0
    return 1 + getLengthRecursive(node.next)


def contains(node, data):
    while node:
        if node.data == data:
            return True
        node = node.next
    return False


def containsRecursive(node, data):
    if not node:
        return False
    if node.data == data:
        return True
    return containsRecursive(node.next, data)


def findNthFromLast(node, n):
    i, temp = 0, node
    while i != n and temp:
        temp = temp.next
        i += 1
    if i != n:
        return None
    while node and temp:
        node, temp = node.next, temp.next
    if node and not temp:
        return node.data
    return None


def isAscending(node):
    if not node or not node.next:
        return False
    while node and node.next:
        if node.data > node.next.data:
            return False
        node = node.next
    return True


def isDescending(node):
    if not node or not node.next:
        return False
    while node and node.next:
        if node.data < node.next.data:
            return False
        node = node.next
    return True


def equals(a, b):
    if not a and not b:
        return True
    if True in [a and not b, b and not a]:
        return False
    while a and b:
        if a.data != b.data:
            return False
        a, b = a.next, b.next
    if True in [a and not b, b and not a]:
        return False
    return True


def reverse(node):
    if not node or not node.next:
        return node
    prev, curr = None, node
    while curr:
        next = curr.next
        curr.next = prev
        prev, curr = curr, next
    return prev


def reverseRecursive(node, prev=None):
    if not node:
        return node
    next = node.next
    node.next = prev
    if not next:
        return node
    return reverseRecursive(next, node)


def mergeAscendingOrder(a, b):
    if not b:
        return a
    if not a:
        return b
    if not a and not b:
        return None
    head = node = None
    if a.data < b.data:
        head = node = a
        a = a.next
    else:
        head = node = b
        b = b.next
    while a or b:
        if a and b:
            if a.data < b.data:
                node.next = a
                a = a.next
            else:
                node.next = b
                b = b.next
        elif not a:
            node.next = b
            b = b.next
        elif not b:
            node.next = a
            a = a.next
        node = node.next
    return head


def middle(node):
    if not node or not node.next or not node.next.next:
        return node
    fast = slow = node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def mergeSort(node):
    def merge(a, b):
        if not a:
            return b
        if not b:
            return a
        head = None
        if a.data < b.data:
            head = a
            a.next = merge(a.next, b)
        else:
            head = b
            b.next = merge(a, b.next)
        return head

    if not node or not node.next:
        return node
    mid = middle(node)
    left, rite = node, mid.next
    mid.next = None
    return merge(mergeSort(left), mergeSort(rite))


def isPalindrome(node):
    if not node or not node.next:
        return False
    values = []
    head = node
    while node:
        values.append(node.data)
        node = node.next
    while head:
        if head.data != values.pop():
            return False
        head = head.next
    return True


def removeDuplicates(node):
    if not node:
        return node
    head = curr = node
    while curr:
        prev, next = curr, curr.next
        while next:
            if curr.data == next.data:
                prev.next = next.next
            prev, next = next, next.next
        curr = curr.next
    return head


def findLoop(node):
    if not node or not node.next:
        return False, None
    slow = fast = node
    while slow and fast:
        if not slow.next or not fast.next or fast.next.next:
            return False, None
        slow, fast = slow.next, fast.next.next
        if id(slow) == id(fast):
            return True, slow

