#!/usr/bin/env python3

s = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''.strip().split('\n')

with open('day4.input', 'r') as f:
    s = f.read().strip().split('\n')

lines = []
for line in s:
    x, y = line.split(',')
    xl, xr, yl, yr = map(int, (*x.split('-'), *y.split('-')))
    xs, ys = range(xl, xr+1), range(yl, yr+1)
    lines.append((xs, ys))

counter = sum(
    all(p in ys for p in xs) or
    all(p in xs for p in ys)
    for xs, ys in lines)

print(counter)

counter = sum(
    any(p in ys for p in xs)
    for xs, ys in lines)

print(counter)


# map each line to a range() object, and use its __contains__ method to check
# for overlaps: `p in ys for p in xs` checks each int in xs for inclusion in ys

# in part 1, one half must entirely overlap the other, i.e: all() of xs must be
# in ys or vise-versa; while in part 2 any() overlap will work.
