import datetime
import unittest


def check(x):
    x1, x2, x3, x4, x5, x6 = str(x), str(2 * x), str(3 * x), str(4 * x), str(5 * x), str(6 * x)
    #print(x1, x2, x3, x4, x5, x6)
    if len(set(map(lambda y: len(y), [x1, x2, x3, x4, x5, x6]))) != 1:
        return 2
    if set(x1) == set(x2) and \
            set(x2) == set(x3) and \
            set(x3) == set(x4) and \
            set(x4) == set(x5) and \
            set(x5) == set(x6):
        return 0
    return 1


def solve():
    x = 11
    while True:
        r = check(x)
        if r == 0:
            return x
        if r == 1:
            x += 1
        if r == 2:
            x = int(''.join(['1' for y in range(len(str(x)) + 1)]))


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(142857, solve())
