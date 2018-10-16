def intersect(x, y):
    if x[0] > y[0]:
        x, y = y, x




def max_no_platforms(trains):
    timelines = {}
    for train in trains:
        for patch in timelines:
            if patch[0] <= train[0] < patch[1]:
                v = timelines.pop(patch)
                timelines[(patch[0], train[0])] = v
                if train[1] <= patch[1]:
                    timelines[(train[0], train[1])] = v + 1
                    timelines[(train[1], patch[1])] = v
                else:
                    timelines[(train[0], patch[1])] = v + 1
                    timelines[(patch[1], train[1])] = v
                break
            elif train[0] <= patch[0] < train[1]:
                v = timelines.pop(patch)
                timelines[(train[0], patch[0])] = v
                if train[1] >= patch[1]:
                    timelines[(patch[0], patch[1])] = v + 1
                    timelines[(patch[1], train[1])] = v
                else:
                    timelines[(patch[0], train[1])] = v + 1
                    timelines[(train[1], patch[1])] = v
                break
        else:
            timelines[train] = 1
    return max(timelines.values())
    pass


trains = [
    (2, 3),
    (1, 4),
    (2, 3),
    (3, 4),
    (4, 6)
]

a = max_no_platforms(trains)
print(a)
