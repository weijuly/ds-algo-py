import unittest

from data_structures.linked_list.single_linked_list import Node, toString, getLength, getLengthRecursive, contains, \
    containsRecursive, findNthFromLast, isAscending, isDescending, reverse, equals, reverseRecursive, \
    mergeAscendingOrder, middle, mergeSort, isPalindrome


def random_list():
    return Node(25, Node(12, Node(35, Node(6, Node(15, Node(45))))))


def ascending_list():
    return Node(10, Node(20, Node(30, Node(40, Node(50, Node(60, Node(70)))))))

def palindrome_list():
    return Node(10, Node(20, Node(30, Node(40, Node(30, Node(20, Node(10)))))))


def another_ascending_list():
    return Node(12, Node(22, Node(33, Node(45, Node(53, Node(61, Node(78)))))))


def combined_ascending_list():
    return Node(10,
                Node(12,
                     Node(20,
                          Node(22,
                               Node(30,
                                    Node(33,
                                         Node(40,
                                              Node(45,
                                                   Node(50,
                                                        Node(53,
                                                             Node(60,
                                                                  Node(61,
                                                                       Node(70,
                                                                            Node(78))))))))))))))


def descending_list():
    return Node(70, Node(60, Node(50, Node(40, Node(30, Node(20, Node(10)))))))


class Test(unittest.TestCase):
    def test_toString(self):
        self.assertEqual(toString(None), '|')
        self.assertEqual(toString(random_list()), '25 => 12 => 35 => 6 => 15 => 45 => |')

    def test_getLength(self):
        self.assertEqual(getLength(None), 0)
        self.assertEqual(getLength(random_list()), 6)

    def test_getLengthRecursive(self):
        self.assertEqual(getLengthRecursive(None), 0)
        self.assertEqual(getLengthRecursive(random_list()), 6)

    def test_contains(self):
        self.assertTrue(contains(random_list(), 15))
        self.assertFalse(contains(random_list(), 0))
        self.assertFalse(contains(None, 0))

    def test_containsRecursive(self):
        self.assertTrue(containsRecursive(random_list(), 15))
        self.assertFalse(containsRecursive(random_list(), 0))
        self.assertFalse(containsRecursive(None, 0))

    def test_findNthFromLast(self):
        self.assertEqual(findNthFromLast(random_list(), 2), 15)
        self.assertEqual(findNthFromLast(random_list(), 4), 35)
        self.assertEqual(findNthFromLast(random_list(), 100), None)
        self.assertEqual(findNthFromLast(None, 50), None)

    def test_isAscending(self):
        self.assertTrue(isAscending(ascending_list()))
        self.assertFalse(isAscending(descending_list()))
        self.assertFalse(isAscending(None))

    def test_isDescending(self):
        self.assertFalse(isDescending(ascending_list()))
        self.assertTrue(isDescending(descending_list()))
        self.assertFalse(isDescending(None))

    def test_equals(self):
        self.assertTrue(equals(ascending_list(), ascending_list()))
        self.assertFalse(equals(ascending_list(), descending_list()))

    def test_reverse(self):
        linked_list = reverse(ascending_list())
        self.assertTrue(equals(linked_list, descending_list()))

    def test_reverseRecursive(self):
        linked_list = reverseRecursive(ascending_list())
        self.assertTrue(equals(linked_list, descending_list()))

    def test_mergeAscendingOrder(self):
        self.assertTrue(equals(mergeAscendingOrder(ascending_list(), None), ascending_list()))
        self.assertTrue(equals(mergeAscendingOrder(None, ascending_list()), ascending_list()))
        self.assertTrue(
            equals(mergeAscendingOrder(another_ascending_list(), ascending_list()), combined_ascending_list()))

    def test_middle(self):
        self.assertIsNone(middle(None))
        self.assertTrue(equals(middle(Node(24)), Node(24)))
        self.assertEqual(middle(ascending_list()).data, 40)

    def test_mergeSort(self):
        self.assertTrue(equals(mergeSort(descending_list()), ascending_list()))

    def test_isPalindrome(self):
        self.assertFalse(isPalindrome(None))
        self.assertFalse(isPalindrome(Node(50)))
        self.assertFalse(isPalindrome(ascending_list()))
        self.assertTrue(isPalindrome(palindrome_list()))


if __name__ == '__main__':
    unittest.main()
