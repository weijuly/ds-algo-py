def solve(s, p):
    if not p:
        return False
    if p == '*':
        return True
    np = p[0]
    for x in p[1:]:
        if x == '*' and np[-1] == '*':
            continue
        np += x
    p = np
    i = 0
    for px in p:
        if px == '*':
            pass
        if px == '?':
            pass
        if px == s[i]:
            i += 1
            continue
        else:
            return False


solve(
    'babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb',
    'b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a'
)
# wrapper('abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb',
#         '***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**'
#         )
# wrapper('c', '*?*')
# wrapper('acdcb', 'a*c?b')
# wrapper('aaaa', '***a')
# wrapper('abcabczzzde', '*abc???de*')
# wrapper('aa', 'a')
# wrapper('aa', '*')
# wrapper('cb', '?a')
# wrapper('cb', '?b')
# wrapper('abcdef', '*abcd')
# wrapper('abcdef', '*abcdef')
# wrapper('abcdef', 'abcd*')
# wrapper('abcdef', 'ab*ef')
# wrapper('', '******')

# @timer
# def solve_linear(s, p):
#     if not p:
#         return False
#     if p == '*' or set(p) == set('*'):
#         return True
#     if len(s) == 1 and p == '?':
#         return True
#     ps, ss = list(p), list(s)
#     while ps and ss:
#         if ps[0] == '*':
#             if len(ps) == 1:
#                 return True
#             if ps[1] == ss[0]:
#                 ps.pop(0)
#             else:
#                 ss.pop(0)
#             continue
#         elif ps[0] == '?':
#             ps.pop(0)
#             ss.pop(0)
#             continue
#         else:
#             if ps[0] == ss[0]:
#                 ps.pop(0)
#                 ss.pop(0)
#                 continue
#             else:
#                 return False
#     if ps:
#         if len(ps) == 1 and ps[0] == '*':
#             return True  # match anything
#         return False
#     if ss:
#         return False
#     return True
