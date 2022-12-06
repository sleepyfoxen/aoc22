#!/usr/bin/env python3

from re import findall

s = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''.strip().split('\n')

with open('day4.input', 'r') as f:
    s = f.read().strip().split('\n')

counter = sum(
    (   int(
        all(
            p in range(yl, yr+1) for p in range(xl, xr+1)
        ) or
        all(
            p in range(xl, xr+1) for p in range(yl, yr+1)
        )
    )
        for xl, xr, yl, yr in ( (int(xl), int(xr), int(yl), int(yr))
        for xl, xr, yl, yr in ( (*x.split('-'), *y.split('-'))
        for x, y in ( line.split(',')
        for line in s ) ) )
    )
)

print(counter)

counter = 0

for line in s:
    x, y = line.split(',')
    xl, xr, yl, yr = map(int, (*x.split('-'), *y.split('-')))

    counter += int(
        any(
            p in range(yl, yr+1) for p in range(xl, xr+1)
        ))

print(counter)
