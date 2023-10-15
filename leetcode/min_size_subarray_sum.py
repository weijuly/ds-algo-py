from leetcode.utils import timer


@timer
def solve(target, nums):
    if not nums:
        return nums
    msa = []
    f, s, l = 0, 1, len(nums)
    while f < l and s <= l:
        sa = nums[f:s]
        sm = sum(sa)
        if sm < target:
            s += 1
        if sm == target:
            if msa and len(sa) < len(msa):
                msa = sa
            else:
                msa = sa
            f += 1
        if sm > target:
            f += 1
    print(msa)
    return len(msa)


solve(11, [1, 2, 3, 4, 5])
solve(7, [2, 3, 1, 2, 4, 3])
solve(4, [1, 4, 4])
solve(11, [1, 1, 1, 1, 1, 1, 1, 1])
