def fmp(array):
    missing = 1
    for x in array:
        if x == missing:
            missing += 1
    print(missing)
    return missing


fmp([7, 8, 9, 11, 12])


4,3,2,1