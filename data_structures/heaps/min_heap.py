class Element:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '%s' % self.data

    def __repr__(self):
        return self.__str__()


def adjust(heap):
    e_idx = len(heap) - 1
    p_idx = int(e_idx / 2)
    while heap[e_idx].data > heap[p_idx].data:
        heap[e_idx], heap[p_idx] = heap[p_idx], heap[e_idx]
        e_idx, p_idx = p_idx, int(p_idx / 2)
    return heap


def insert(heap, data):
    if not heap:
        return [Element(data)]
    heap.append(Element(data))
    return adjust(heap)


def remove(heap):
    return heap[0], adjust(heap[1:])
