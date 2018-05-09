import random
from collections import defaultdict


def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i - 1, -1, -1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            else:
                break
    return array


def selection_sort(array):
    for i in range(0, len(array)):
        m, p = array[i], None
        for j in range(i + 1, len(array)):
            if array[j] < m:
                p, m = j, array[j]
        if p:
            array[i], array[p] = array[p], array[i]
    return array


def quick_sort(array):
    if not array:
        return []
    h = array.pop()
    return quick_sort([x for x in array if x <= h]) + [h] + quick_sort([x for x in array if x > h])


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


def merge_sort(array):
    if len(array) < 2:
        return array
    if len(array) == 2:
        x, y = array
        if x <= y:
            return [x, y]
        else:
            return [y, x]
    m = int(len(array) / 2)
    left, right = merge_sort(array[:m]), merge_sort(array[m:])
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def bucket_sort(array):
    # mummy, nooooooo
    bucket = defaultdict(list)
    m, M = min(array), max(array)
    for x in array:
        bucket[int((x - m) * 10 / (M - m))].append(x)
    result = []
    for x in sorted(bucket.keys()):
        result.extend(insertion_sort(bucket[x]))
    return result
