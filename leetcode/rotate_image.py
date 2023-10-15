class Solution:
    def rotate(self, matrix):
        sz = len(matrix)
        for row in matrix:
            for i in range(int(sz / 2)):
                row[i], row[sz - 1 - i] = row[sz - 1 - i], row[i]
        for i in range(sz - 1):
            for j in range(sz - i - 1):
                matrix[i][j], matrix[sz - j - 1][sz - i - 1] = matrix[sz - j - 1][sz - i - 1], matrix[i][j]
                # print('%d, %d - %d, %d' % (i, j, sz - j - 1, sz - i - 1))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Solution().rotate(matrix)
print(matrix)

matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
Solution().rotate(matrix)
print(matrix)
