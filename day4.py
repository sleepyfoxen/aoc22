#!/usr/bin/env python3

s = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''.strip().split('\n')

with open('day4.input', 'r') as f:
    s = f.read().strip().split('\n')

counter = 0

for line in s:
    x, y = line.split(',')           # parse
    xl, xr = map(int, x.split('-'))
    yl, yr = map(int, y.split('-'))

    if xr - xl < yr - yl:
        if yl <= xl and yr >= xr:    # check
            counter += 1

    else:
        if xl <= yl and xr >= yr:
            counter += 1

print(counter)

counter = 0

for line in s:
    x, y = line.split(',')
    xl, xr = map(int, x.split('-'))
    yl, yr = map(int, y.split('-'))

    for i in range(xl, xr+1):
        if i in range(yl, yr+1):
            counter += 1
            break

print(counter)
