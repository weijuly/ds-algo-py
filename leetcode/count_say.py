from leetcode.utils import timer


def say(n):
    stack, num, res = [], list(str(n)), ''
    while True:
        if stack and stack[-1] != num[0]:
            res += '%d%s' % (len(stack), stack[0])
            stack = []
        stack.append(num.pop(0))
        if stack and not num:
            res += '%d%s' % (len(stack), stack[0])
            break
    return res


@timer
def solve(n):
    if n == 1:
        return '1'
    return say(solve(n - 1))


solve(5)
