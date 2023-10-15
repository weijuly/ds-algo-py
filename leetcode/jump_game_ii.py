from leetcode.utils import timer


@timer
def solve(nums):
    paths, target = [], len(nums) - 1
    minsteps = 4294967296
    for num in nums:
        steps = [x + 1 for x in range(num)]
        if not steps:
            continue
        if paths:
            paths = [[*path, x] for path in paths for x in steps]
        else:
            paths = [[x] for x in steps]
        paths = [path for path in paths if sum(path) <= target]
        for path in paths:
            if sum(path) == target and minsteps > len(path):
                minsteps = len(path)
    return minsteps


# solve([2, 3, 1, 1, 4])
# solve([2, 3, 0, 1, 4])
# solve([2, 0, 2, 0, 1])
solve([4, 1, 1, 3, 1, 1, 1])
