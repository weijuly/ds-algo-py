import unittest


def getAllSubsets(xs):
    if not xs:
        return [[]]
    head, subsets = xs[0], getAllSubsets(xs[1:])
    subsets.extend([s + [head] for s in subsets])
    return subsets


class Test(unittest.TestCase):
    def test_getAllSubsets(self):
        self.assertListEqual(getAllSubsets(''), [[]])
        self.assertListEqual(getAllSubsets('a'), [[], ['a']])
        self.assertListEqual(getAllSubsets('ab'), [[], ['b'], ['a'], ['b', 'a']])  # Order is important for assert
        self.assertEqual(len(getAllSubsets('ab')), 4)
        self.assertEqual(len(getAllSubsets('abc')), 8)
        self.assertEqual(len(getAllSubsets('abcdef')), 64)


if __name__ == '__main__':
    unittest.main()
