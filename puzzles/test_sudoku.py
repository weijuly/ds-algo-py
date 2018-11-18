import unittest
from copy import deepcopy

POSSIBILITIES = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def zone(r, c):
    if r >= 0 and r <= 2:
        if c >= 0 and c <= 2:
            return range(0, 3), range(0, 3)
        if c >= 3 and c <= 5:
            return range(0, 3), range(3, 6)
        if c >= 6 and c <= 8:
            return range(0, 3), range(6, 9)
    if r >= 3 and r <= 5:
        if c >= 0 and c <= 2:
            return range(3, 6), range(0, 3)
        if c >= 3 and c <= 5:
            return range(3, 6), range(3, 6)
        if c >= 6 and c <= 8:
            return range(3, 6), range(6, 9)
    if r >= 6 and r <= 8:
        if c >= 0 and c <= 2:
            return range(6, 9), range(0, 3)
        if c >= 3 and c <= 5:
            return range(6, 9), range(3, 6)
        if c >= 6 and c <= 8:
            return range(6, 9), range(6, 9)


def possibilities(matrix, r, c):
    row = set([x for x in matrix[r] if x != 0])
    col = set([x[c] for x in matrix if x[c] != 0])
    row_range, col_range = zone(r, c)
    sub = set([matrix[x][y] for x in row_range for y in col_range])
    return POSSIBILITIES - (row | col | sub)


def solved(matrix):
    return not any([x == 0 for row in matrix for x in row])


def next_slot(matrix):
    return ((r, c) for r in range(0, 9) for c in range(0, 9) if matrix[r][c] == 0)


def solve(matrix):
    if solved(matrix):
        return True, matrix
    r, c = next(next_slot(matrix))
    ps = possibilities(matrix, r, c)
    for p in ps:
        copy = deepcopy(matrix)
        copy[r][c] = p
        status, result = solve(copy)
        if status:
            return status, result
    return False, matrix


class Test(unittest.TestCase):

    def test_solve(self):
        matrix = [
            [0, 0, 3, 0, 2, 0, 6, 0, 0],
            [9, 0, 0, 3, 0, 5, 0, 0, 1],
            [0, 0, 1, 8, 0, 6, 4, 0, 0],
            [0, 0, 8, 1, 0, 2, 9, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 6, 7, 0, 8, 2, 0, 0],
            [0, 0, 2, 6, 0, 9, 5, 0, 0],
            [8, 0, 0, 2, 0, 3, 0, 0, 9],
            [0, 0, 5, 0, 1, 0, 3, 0, 0]
        ]
        status, solution = solve(matrix)
        self.assertEqual(len(solution), 9)
        [self.assertEqual(len(x), 9) for x in solution]
        [self.assertSetEqual(set(x), POSSIBILITIES) for x in solution]


if __name__ == '__main__':
    unittest.main()
