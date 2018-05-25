import unittest

from data_structures.linked_list.double_linked_list import Node, getLength, getHead, getLengthRecursive, equals, reverse


def make_list(array):
    prev, head = None, None
    for data in array:
        node = Node(data)
        if not prev:
            head = node
            node.prev = None
            prev = node
            continue
        prev.next = node
        node.prev = prev
        prev = node
    return head


def sample_list():
    array = [19, 12, 2, 13, 16, 7, 16, 0, 11, 4, 10, 20, 9, 8, 17, 12, 5, 9, 1, 17]
    return make_list(array)


def another_list():
    array = [32, 36, 38, 30, 28, 24, 26, 35, 24, 40, 26, 29, 25, 40, 36, 33, 26, 30, 22, 26]
    return make_list(array)


def reversed_sample_list():
    array = [19, 12, 2, 13, 16, 7, 16, 0, 11, 4, 10, 20, 9, 8, 17, 12, 5, 9, 1, 17]
    return make_list(reversed(array))


class Test(unittest.TestCase):

    def test_getHead(self):
        self.assertEqual(getHead(None), None)
        self.assertEqual(getHead(sample_list()).data, 19)
        self.assertEqual(getHead(sample_list().next.next).data, 19)

    def test_getLength(self):
        self.assertEqual(getLength(None), 0)
        self.assertEqual(getLength(sample_list()), 20)
        self.assertEqual(getLength(sample_list().next.next.next), 20)

    def test_getLengthRecursive(self):
        self.assertEqual(getLengthRecursive(None), 0)
        self.assertEqual(getLengthRecursive(sample_list()), 20)
        self.assertEqual(getLengthRecursive(sample_list().next.next.next), 20)

    def test_equals(self):
        self.assertTrue(equals(sample_list(), sample_list()))
        self.assertFalse(equals(sample_list(), another_list()))
        self.assertFalse(equals(sample_list(), None))
        self.assertFalse(equals(None, sample_list()))
        self.assertTrue(equals(None, None))

    def test_reverse(self):
        self.assertIsNone(reverse(None))
        self.assertTrue(equals(reverse(sample_list()), reversed_sample_list()))
        self.assertTrue(equals(reversed_sample_list(), reverse(sample_list())))
