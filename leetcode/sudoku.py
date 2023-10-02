nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}


def qrange(i):
    if i > 5:
        return [6, 7, 8]
    if i > 2:
        return [3, 4, 5]
    return [0, 1, 2]


def find_possibilities(board, x, y):
    vals = set()
    vals.update([board[i][y] for i in range(9) if board[i][y] != '.'])
    vals.update([board[x][i] for i in range(9) if board[x][i] != '.'])
    vals.update([board[i][j] for i in qrange(x) for j in qrange(y) if board[i][j] != '.'])
    return sorted(list(set(nums) - vals))


def solved(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                return False
    return True


def ppprint(board, ):
    for i in range(9):
        print(' '.join([board[i][j] for j in range(9)]))


def fill_position(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                return i, j
    return 9, 9


def solve(board):
    i, j = fill_position(board)
    if i == 9 and j == 9:
        return True
    possibilities = find_possibilities(board, i, j)
    for possibility in possibilities:
        board[i][j] = possibility
        if solve(board):
            ppprint(board)
            return True
    board[i][j] = '.'
    return False


# @timer


solve([["5", "3", ".", ".", "7", ".", ".", ".", "."],
       ["6", ".", ".", "1", "9", "5", ".", ".", "."],
       [".", "9", "8", ".", ".", ".", ".", "6", "."],
       ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
       ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
       ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
       [".", "6", ".", ".", ".", ".", "2", "8", "."],
       [".", ".", ".", "4", "1", "9", ".", ".", "5"],
       [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
