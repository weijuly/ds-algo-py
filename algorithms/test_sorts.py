import random
import time
import unittest

from algorithms.sorts import insertion_sort, selection_sort, quick_sort, bubble_sort, merge_sort, bucket_sort,heap_sort


def unsorted():
    return [1, 3, 2, 4, 5, 7, 6, 8, 0, 9]


def sorted():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def measure_time(sort):
    array = [random.randint(1, 10000) for x in range(10000)]
    start = time.perf_counter()
    sort(array)
    end = time.perf_counter()
    print('Time taken by %s for 10000 random numbers is %f sec' % (sort.__name__, end - start))


class Test(unittest.TestCase):

    def test_insertion_sort(self):
        self.assertListEqual(insertion_sort(unsorted()), sorted())
        measure_time(insertion_sort)

    def test_selection_sort(self):
        self.assertListEqual(selection_sort(unsorted()), sorted())
        measure_time(selection_sort)

    def test_quick_sort(self):
        self.assertListEqual(quick_sort(unsorted()), sorted())
        measure_time(quick_sort)

    def test_bubble_sort(self):
        self.assertListEqual(bubble_sort(unsorted()), sorted())
        measure_time(bubble_sort)

    def test_merge_sort(self):
        self.assertListEqual(merge_sort(unsorted()), sorted())
        measure_time(merge_sort)

    def test_bucket_sort(self):
        self.assertListEqual(bucket_sort(unsorted()), sorted())
        measure_time(bucket_sort)
    def test_heap_sort(self):
        self.assertListEqual(bucket_sort(unsorted()), sorted())
        measure_time(heap_sort)