import unittest


def distance(source, target, memo=None):
    key = source + '#' + target
    if key in memo:
        return memo[key]
    if not source:
        memo[key] = len(target)
        return memo[key]
    if not target:
        memo[key] = len(source)
        return memo[key]
    if source[0] == target[0]:
        memo[key] = distance(source[1:], target[1:], memo)
        return memo[key]
    else:
        memo[key] = 1 + min(distance(source[1:], target[1:], memo), distance(source, target[1:], memo), distance(source[1:], target, memo))
        return memo[key]


class Test(unittest.TestCase):
    def test_distance(self):
        memo = {}
        self.assertEqual(distance('Gopi', 'Krishnan', memo), 8)
