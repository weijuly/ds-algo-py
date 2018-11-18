import random
import sys
import unittest

from data_structures.heaps.max_heap import insert, remove


class Test(unittest.TestCase):
    def test_min_heap(self):
        array = set([random.randint(1, 1000) for x in range(100)])
        heap = []
        for x in array:
            heap = insert(heap, x)
        M = sys.maxsize
        while len(heap) > 2:
            m, heap = remove(heap)
            self.assertTrue(m.data < M)
            M = m.data
