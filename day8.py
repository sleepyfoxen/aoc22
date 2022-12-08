#!/usr/bin/env python3

from typing import List

s = '''30373
25512
65332
33549
35390'''.split('\n')

with open('day8.input', 'r') as f:
    s = f.read().strip().split('\n')

s = [ [ int(t) for t in r ] for r in s ]

def visible(s: List[int]) -> List[bool]:
    v = [ t > max((*s[:i], -1)) for i, t in enumerate(s) ]
    return v

rows = []
for r in s:
    ltr, rtl = visible(r), visible(r[::-1])[::-1]
    row = [ l or r for l, r in zip(ltr, rtl) ]
    rows.append(row)

cols = []
for c in zip(*s):
    utd, dtu = visible(c), visible(c[::-1])[::-1]
    col = [ u or d for u, d in zip(utd, dtu) ]
    cols.append(col)

total = 0
for r, c in zip(rows, zip(*cols)):
    total += sum(r[i] or c[i] for i in range(len(rows)))

print(total)


def vis(i: int, s: List[int]) -> int:
    count, t, i = 0, s[i], i - 1

    while s[i] < t and i >= 0:
        count += 1
        i -= 1

    if i >= 0: count += 1  # blocked by this tree
    return count

scores = []
for i, r in enumerate(s):
    for j, t in enumerate(r):
        c = list(zip(*s))[j]

        ltr, utd = vis(j, r), vis(i, c)
        rtl = vis(len(r) - j - 1, r[::-1])
        dtu = vis(len(c) - i - 1, c[::-1])
        sc = ltr * rtl * utd * dtu
        scores.append(sc)

print(max(scores))
