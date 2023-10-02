import time


def findfoursum(array, target, foursum, collector):
    if len(foursum) == 4 and sum(foursum) == target and sorted(foursum) not in collector:
        if sorted(foursum) not in collector:
            collector.append(sorted(foursum))
        return
    if len(foursum) < 4:
        for i in range(len(array)):
            findfoursum(
                [array[j] for j in range(len(array)) if i != j],
                target,
                [*foursum, array[i]],
                collector
            )


def get(array, position): pass


def find_(nums, target):
    acc = []
    l = len(nums)
    M = 2 ** l
    for i in range(M):
        pos = bin(i)[2:].rjust(l, '0')
        if pos.count('1') != 4:
            continue
        vals = sorted([x[0] for x in zip(nums, pos) if x[1] == '1'])
        if sum(vals) == target and vals not in acc:
            acc.append(vals)
            print(pos, vals)
    return acc


def timer(f):
    def i(*args):
        s = time.time()
        r = f(*args)
        print('t: ', time.time() - s)
        return r

    return i


@timer
def find(nums, target):
    _nums = sorted(nums)
    _len = len(_nums)
    _result = []
    pa = None
    for i in range(_len - 3):
        a = _nums[i]
        if pa == a:
            continue
        if a > 0 and a > target:
            break
        pb = None
        for j in range(i + 1, _len - 2):
            b = _nums[j]
            if pb == b:
                continue
            s = a + b
            if s > 0 and s > target:
                break
            pc = None
            for k in range(j + 1, _len - 1):
                c = _nums[k]
                if pc == c:
                    continue
                s = a + b + c
                if s > 0 and s > target:
                    break
                pd = None
                for l in range(k + 1, _len):
                    d = _nums[l]
                    if pd == d:
                        continue
                    s = a + b + c + d
                    if s == target:
                        _fsum = [a, b, c, d]
                        if _fsum not in _result:
                            _result.append([a, b, c, d])
                    if s > target:
                        break
                    pd = d
                pc = c
            pb = b
        pa = a
    print(_result)
    print(len(_result))
    return _result


find([1, 0, -1, 0, -2, 2], 0)
find([1, -2, -5, -4, -3, 3, 3, 5], -11)
find([2, 2, 2, 2, 2], 8)
find([-493, -482, -482, -456, -427, -405, -392, -385, -351, -269, -259, -251, -235, -235, -202, -201, -194, -189, -187,
      -186, -180, -177, -175, -156, -150, -147, -140, -122, -112, -112, -105, -98, -49, -38, -35, -34, -18, 20, 52, 53,
      57, 76, 124, 126, 128, 132, 142, 147, 157, 180, 207, 227, 274, 296, 311, 334, 336, 337, 339, 349, 354, 363, 372,
      378, 383, 413, 431, 471, 474, 481, 492], 6189)
find(
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20,
     20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
     30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 50, 50, 50, 50, 50, 50, 50,
     50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60,
     60, 60, 60, 60, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 80, 80, 80, 80, 80,
     80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90,
     90, 90, 90, 90, 90, 90], 200)
find([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
      2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
      2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
      2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
      2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
      2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 8)

# def findfoursum_(array, target, candidate, accumulator):
#     if len(candidate) == 4 and sum(candidate) == target and sorted(candidate) not in accumulator:
#         accumulator.append(sorted(candidate))
#     x, *ys = array
#     for y in ys:
#         findfoursum_(ys, target, [*candidate, x], accumulator)
#
#
# collector = []
# findfoursum([2, 2, 2, 2], 8, [], collector)
# print(collector)
