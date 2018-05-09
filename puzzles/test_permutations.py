import unittest


def permute(sequence):
    if len(sequence) == 0:
        return []
    if len(sequence) == 1:
        return [sequence]
    head, *tail = sequence
    permutations = []
    for x in permute(tail):
        permutations.extend([x[:i] + [head] + x[i:] for i in range(len(x) + 1)])
    return permutations


class Test(unittest.TestCase):
    def test_permute(self):
        self.assertListEqual(permute(list('ab')), [['a', 'b'], ['b', 'a']])
        self.assertListEqual(permute(list('abc')),
                             [['a', 'b', 'c'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['a', 'c', 'b'], ['c', 'a', 'b'],
                              ['c', 'b', 'a']])
        self.assertEqual(permute(list('a')), [['a']])
        self.assertEqual(permute(list('')), [])
        self.assertEqual(len(permute(list('abcd'))), 24)
        self.assertEqual(len(permute(list('abcde'))), 120)


if __name__ == '__main__':
    unittest.main()

