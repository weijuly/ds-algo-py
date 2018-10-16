def product(xs):
    y = 1
    for x in xs:
        y = y * x
    return y


def solve():
    xs = [1, 1, 1, 1, 1, 1, 1]
    while True:
        s = sum(xs)
        p = product(xs)
        print(s, p)
        if s > p:
            xs[-1] += 1
        if p > s:
            xs[-1] += 1
        if p == s:
            break


solve()
