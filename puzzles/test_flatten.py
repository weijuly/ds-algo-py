import unittest


def flatten(nested):
    out = []
    for x in nested:
        if type(x) is list:
            out.extend(flatten(x))
        else:
            out.append(x)
    return out


def oned():
    return [1, 2, 3]


def twod():
    return [oned(), oned(), oned()]


def threed():
    return [twod(), twod(), twod()]


def fourd():
    return [threed(), threed(), threed()]


class Test(unittest.TestCase):
    def test_flatten(self):
        self.assertEqual(len(flatten(oned())), 3)
        self.assertEqual(len(flatten(twod())), 9)
        self.assertEqual(len(flatten(threed())), 27)
        self.assertEqual(len(flatten(fourd())), 81)

        if __name__ == '__main__':
            unittest.main()
