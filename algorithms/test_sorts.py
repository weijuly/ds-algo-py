import random
import time
import unittest

from algorithms.sorts import insertion_sort, selection_sort, quick_sort, bubble_sort, merge_sort, bucket_sort


def unsorted():
    return [1, 3, 2, 4, 5, 7, 6, 8, 0, 9]


def sorted():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def measure_time_random(sort):
    array = [random.randint(1, 10000) for x in range(10000)]
    start = time.perf_counter()
    sort(array)
    end = time.perf_counter()
    print('Time taken by %s for 10000 random numbers is %f sec' % (sort.__name__, end - start))


def measure_time_sorted(sort):
    array = quick_sort([random.randint(1, 10000) for x in range(10000)])
    start = time.perf_counter()
    sort(array)
    end = time.perf_counter()
    print('Time taken by %s for 10000 sorted numbers is %f sec' % (sort.__name__, end - start))


def measure_time_reversed(sort):
    array = [random.randint(1, 10000) for x in range(10000)]
    array.sort(reverse=True)
    start = time.perf_counter()
    sort(array)
    end = time.perf_counter()
    print('Time taken by %s for 10000 reverse sorted numbers is %f sec' % (sort.__name__, end - start))


class Test(unittest.TestCase):

    def test_insertion_sort(self):
        self.assertListEqual(insertion_sort(unsorted()), sorted())
        measure_time_random(insertion_sort)
        measure_time_sorted(insertion_sort)
        measure_time_reversed(insertion_sort)

    def test_selection_sort(self):
        self.assertListEqual(selection_sort(unsorted()), sorted())
        measure_time_random(selection_sort)
        measure_time_sorted(selection_sort)
        measure_time_reversed(selection_sort)

    def test_quick_sort(self):
        self.assertListEqual(quick_sort(unsorted()), sorted())
        measure_time_random(quick_sort)
        #measure_time_sorted(quick_sort)
        #measure_time_reversed(quick_sort)

    def test_bubble_sort(self):
        self.assertListEqual(bubble_sort(unsorted()), sorted())
        measure_time_random(bubble_sort)
        measure_time_sorted(bubble_sort)
        measure_time_reversed(bubble_sort)

    def test_merge_sort(self):
        self.assertListEqual(merge_sort(unsorted()), sorted())
        measure_time_random(merge_sort)
        measure_time_sorted(merge_sort)
        measure_time_reversed(merge_sort)

    def test_bucket_sort(self):
        self.assertListEqual(bucket_sort(unsorted()), sorted())
        measure_time_random(bucket_sort)
        measure_time_sorted(bucket_sort)
        measure_time_reversed(bucket_sort)
