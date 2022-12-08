#!/usr/bin/env python3

from typing import Tuple

s = '''30373
25512
65332
33549
35390'''.split('\n')

with open('day8.input', 'r') as f:
    s = f.read().strip().split('\n')

s = tuple(tuple(map(int, r)) for r in s)
s_ = tuple(zip(*s))  # s inverted: columns are now rows

def outer_visible(ts: Tuple[int]) -> Tuple[bool]:
    v = tuple( t > max((*ts[:i], -1)) for i, t in enumerate(ts) )
    return v

rows, cols = [], []
for r, c in zip(s, s_):
    ltr, utd = map(outer_visible, (r, c))
    rtl, dtu = map(lambda t: outer_visible(t[::-1])[::-1], (r, c))
    row = [ l or r for l, r in zip(ltr, rtl) ]
    col = [ u or d for u, d in zip(utd, dtu) ]
    rows.append(row)
    cols.append(col)

total = 0
for r, c in zip(rows, zip(*cols)):
    total += sum(r[i] or c[i] for i in range(len(rows)))

print(total)

def inner_visible(i: int, ts: Tuple[int]) -> int:
    count, t, i = 0, ts[i], i - 1

    while ts[i] < t and i >= 0:
        count += 1
        i -= 1

    count += int(i >= 0)  # blocked by this tree
    return count

scores = []
for i, r in enumerate(s):
    for j, t in enumerate(r):
        c = s_[j]

        ltr, utd = inner_visible(j, r), inner_visible(i, c)
        rtl = inner_visible(len(r) - j - 1, r[::-1])
        dtu = inner_visible(len(c) - i - 1, c[::-1])
        sc = ltr * rtl * utd * dtu
        scores.append(sc)

print(max(scores))
