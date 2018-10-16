import datetime
import unittest
from collections import defaultdict

ROYAL_FLUSH_V = set('BCDEF')

LOOKUP = {
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'T': 'B',
    'J': 'C',
    'Q': 'D',
    'K': 'E',
    'A': 'F',
}


def card_v(cards):
    return sorted([LOOKUP[x[0]] for x in cards])


def card_s(cards):
    return [x[1] for x in cards]


def conseq(vs):
    if '23456789BCDEF'.find(''.join(vs)) >= 0:
        return True
    return False


def vcount(vs):
    m = defaultdict(int)
    for v in vs:
        m[v] += 1
    return m


def kforv(m, v):
    for k in m:
        if m[k] == v:
            return k
    return None


def four_of_a_kind(vs):
    m = vcount(vs)
    if 4 in m.values():
        return True, kforv(m, 4)
    return False, 0


def full_house(vs):
    m = vcount(vs)
    if 2 in m.values() and 3 in m.values():
        return True, max(m.keys())
    return False, 0


def three_of_a_kind(vs):
    m = vcount(vs)
    if 3 in m.values():
        return True, kforv(m, 3)
    return False, 0


def two_pairs(vs):
    m = vcount(vs)
    if len([x for x in m.values() if x == 2]) == 2:
        return True, max([lambda y: kforv(m, y) for y in m.values() if y == 2])
    return False, 0


def one_pair(vs):
    m = vcount(vs)
    if 2 in m.values():
        return True, kforv(m, 2)
    return False, 0


def poker(cards):
    cvs, css = card_v(cards), card_s(cards)
    if len(set(css)) == 1 and set(cvs) == ROYAL_FLUSH_V:
        return '9RF', 0
    if len(set(css)) == 1 and conseq(cvs):
        return '8SF', card_v(cards)[-1]
    if four_of_a_kind(cvs)[0]:
        return '7FK', four_of_a_kind(cvs)[1]
    if full_house(cvs)[0]:
        return '6FK', full_house(cvs)[1]
    if len(set(css)) == 1:
        return '5FF', max(cvs)
    if conseq(cvs):
        return '4SR', max(cvs)
    if three_of_a_kind(cvs)[0]:
        return '3TK', three_of_a_kind(cvs)[1]
    if two_pairs(cvs)[0]:
        return '2TP', two_pairs(cvs)[1]
    if one_pair(cvs)[0]:
        return '1OP', one_pair(cvs)[1]
    return '0HC', max(cvs)


def winner(line):
    cards = line.split(' ')
    p1, p2 = 0, 0
    p1r, p2r = poker(cards[:5]), poker(cards[5:])
    print(p1r, p2r)
    if p1r > p2r:
        p1 += 1
    else:
        p2 += 1
    print(p1, p2)


winner('4D 6S 9H QH QC 3D 6D 7H QD QS')
