class Element:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '%s' % self.data

    def __repr__(self):
        return self.__str__()


def adjustUp(heap):
    if not heap or len(heap) < 2:
        return heap
    e_idx = len(heap) - 1
    p_idx = e_idx // 2
    while heap[e_idx].data < heap[p_idx].data:
        heap[e_idx], heap[p_idx] = heap[p_idx], heap[e_idx]
        e_idx, p_idx = p_idx, p_idx // 2
    return heap


def adjustDn(heap):
    if not heap or len(heap) < 2:
        return heap
    p_idx, e_idx = 1, 2
    while e_idx < len(heap):
        if e_idx + 1 < len(heap) and heap[e_idx + 1].data < heap[e_idx].data:
            e_idx = e_idx + 1
        if heap[e_idx].data < heap[p_idx].data:
            heap[e_idx], heap[p_idx] = heap[p_idx], heap[e_idx]
        p_idx, e_idx = e_idx, e_idx * 2
    return heap


def insert(heap, data):
    if not heap:
        return [Element(0), Element(data)]
    heap.append(Element(data))
    return adjustUp(heap)


def remove(heap):
    if not heap or len(heap) < 2:
        return None, heap
    elem = heap.pop(1)
    heap.insert(1, heap.pop())
    return elem, adjustDn(heap)


# heap = None
# heap = insert(heap, 5)
# heap = insert(heap, 9)
# heap = insert(heap, 11)
# heap = insert(heap, 14)
# heap = insert(heap, 18)
# heap = insert(heap, 19)
# heap = insert(heap, 21)
# heap = insert(heap, 33)
# heap = insert(heap, 17)
# heap = insert(heap, 27)
# elem, heap = remove(heap)
# print(elem, heap)
# elem, heap = remove(heap)
# print(elem, heap)
# elem, heap = remove(heap)
# print(elem, heap)
# elem, heap = remove(heap)
# print(elem)
# elem, heap = remove(heap)
# print(elem)
# elem, heap = remove(heap)
# print(elem)
# elem, heap = remove(heap)
# print(elem)
# elem, heap = remove(heap)
# print(elem)
# elem, heap = remove(heap)
# print(elem)
# elem, heap = remove(heap)
# print(elem)
# elem, heap = remove(heap)
# print(elem)
# elem, heap = remove(heap)
# print(elem)
