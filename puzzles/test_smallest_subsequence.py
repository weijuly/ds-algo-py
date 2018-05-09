import sys, unittest

smaller = 'ACE'
bigger = 'ABCDEFGHAIJKCRTYEPUIOACED'

START = 'S'
REMAINING = 'R'
END = 'E'
LENGTH = 'L'


def findSmallestSubsequence(bigger, smaller):
    result = []
    for i, v in enumerate(bigger):
        if v not in smaller:
            continue
        result.append({START: i, LENGTH: sys.maxsize, REMAINING: set(smaller)})
        for data in result:
            data[REMAINING] -= set(v)
            if data[LENGTH] == sys.maxsize and not data[REMAINING]:
                data[END] = i
                data[LENGTH] = data[END] - data[START]
                if data[LENGTH] == len(smaller) - 1:
                    return data
    return sorted(result, key=lambda x: x[LENGTH])[0]


class Test(unittest.TestCase):
    def test_balance(self):
        pass


if __name__ == '__main__':
    unittest.main()
