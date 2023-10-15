def compress(pattern):
    np = pattern[0]
    for x in pattern[1:]:
        if x == '*' and np[-1] == '*':
            continue
        np += x
    return np


def find_matches():
    pass


def solve(text, pattern):
    if pattern == '*':
        return True
    pattern = compress(pattern)
    j = 0
    for i, p in enumerate(pattern):
        t = text[j] if j < len(text) else None
        if p == '*':
            pass
        if p == '?':
            pass
        if True:
            matches = find_matches()
            print(i, p)


solve(
    'babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb',
    'b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a'
)
