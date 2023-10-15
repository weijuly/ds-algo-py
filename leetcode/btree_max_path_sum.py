class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


L = -1
R = 1


def solve(tree, direction, parent, paths):
    if not tree:
        return []
    if not parent:
        paths.append([tree.val])
    else:
        
        if direction == L:
            candidates = [path for path in paths if path[0] == parent]
            for candidate in candidates:
                paths.append([tree.val, *candidate])
        if direction == R:
            candidates = [path for path in paths if path[-1] == parent]
            for candidate in candidates:
                paths.append([*candidate, tree.val])
            pass
    if tree.left:
        solve(tree.left, L, tree.val, paths)
    if tree.right:
        solve(tree.right, R, tree.val, paths)


paths = []
solve(TreeNode(1,
               TreeNode(2,
                        TreeNode(4),
                        TreeNode(5)),
               TreeNode(3,
                        TreeNode(6),
                        TreeNode(7))), None, None, paths)

#
#                     1
#             2               3
#         4       5       6       7
#
# 2 1 3
# 2 1 1 3
# [2 1][1 3][2 1 3]
#
#  [4 2 1] [4 2 1 3] [5 2 1][5 2 1 3]
