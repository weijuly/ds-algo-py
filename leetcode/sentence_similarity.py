def solve(s1, s2):
    ts1 = s1.split()
    ts2 = s2.split()
    shorter, longer = ts2, ts1
    if len(ts2) > len(ts1):
        shorter, longer = ts1, ts2
    while shorter:
        token = shorter.pop(0)
        while longer and token != longer[0]:
            longer.pop(0)
        if longer and token == longer[0]:
            longer.pop(0)
    if not shorter:
        return True
    return False


print(solve('My name is Haley', 'My Haley'))
print(solve('of', 'A lot of words'))
print(solve('of', 'A lot of words'))
