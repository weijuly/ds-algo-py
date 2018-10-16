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


# distinct permutations
def distinct_permute(seq):
    if len(seq) == 0:
        return []
    if len(seq) == 1:
        return [seq]
    head, *tail = seq
    permutations = []
    for x in distinct_permute(tail):
        for y in [x[:i] + [head] + x[i:] for i in range(len(x) + 1)]:
            if y not in permutations:
                permutations.append(y)
    return permutations


# permuations of length l
def permutations_of_length(seq, l):
    if l == 0 or l > len(seq):
        return []
    permutations = []
    for x in permute(seq):
        if x[:l] not in permutations:
            permutations.append(x[:l])
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

    def test_distinct_permute(self):
        self.assertEqual(len(distinct_permute('ABCA')), 12)

    def test_permutations_of_length(self):
        y = permutations_of_length('ABCDE', 2)
        print(y)
        #print(permutations_of_length('ABCDE', 2))


if __name__ == '__main__':
    unittest.main()
