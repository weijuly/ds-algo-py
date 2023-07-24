# Problems in common priority queue implementations
# - no support for multiple items with same priority
# - if multiple items are supported, then insertion order isn't maintained

# An attempt at implementing a priority queue that has O(1) for dequeue and O(log n)
# for enqueue

# The idea is as follows:
# priority queue is implemented as a linked list
# the head is the item eligible to be dequeued next
# items are arranged in priority and insertion order in the list
# store positions of priority change for ease of insertion

class Node:
    def __init__(self, prio, data):
        self.prio, self.data, self.prev, self.next = prio, data, None, None

    def __repr__(self):
        p = str(self.prev.data) if self.prev else '|'
        n = str(self.next.data) if self.next else '|'
        return '%s => %d => %s' % (p, self.data, n)


def _prepend(queue, node):
    prev = queue.prev
    queue.prev = node
    node.next = queue
    if prev:
        prev.next = node
        node.prev = prev
    return node


def _append(queue, node):
    next = queue.next
    queue.next = node
    node.prev = queue
    if next:
        node.next = next
        next.prev = node
    return node


class PriorityQueue:

    def __init__(self):
        self.queue = None
        self.lookup = {}

    def enqueue(self, prio, data):
        node = Node(prio, data)
        # if queue is empty, this element becomes the queue
        if not self.queue:
            self.queue = node
            self.lookup[prio] = self.queue
            return
        # If the incoming item has a higher priority, add it to the beginning
        if prio > self.queue.prio:
            self.queue = _prepend(self.queue, node)
            self.lookup[prio] = self.queue
            return
        # If the priority already exists, add it to the sublist
        if prio in self.lookup:
            self.lookup[prio] = _append(self.lookup[prio], node)
            return
        # Else walk the list. This can be optimized still
        curr, prev = self.queue, self.queue.prev
        while curr and prio < curr.prio:
            prev, curr = curr, curr.next
        self.lookup[prio] = _append(prev, node)

    def dequeue(self):
        if not self.queue:
            return None
        data = self.queue.data
        self.queue = self.queue.next
        return data
