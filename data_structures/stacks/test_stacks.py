import unittest
from unittest import skip

from data_structures.stacks.stacks import sort_stack, sort_stack2, sort_stack_r


class Test(unittest.TestCase):

    @skip("skip")
    def test_sort(self):
        self.assertEqual(sort_stack_r([]), [])
        self.assertEqual(sort_stack_r([1]), [1])
        self.assertEqual(sort_stack_r([2, 1]), [1, 2])
        stack = [1, 4, 2, 5, 3, 6, 8, 7]
        self.assertEqual(sort_stack_r(stack[:]), sorted(stack))
