#!/usr/bin/env python3

s = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''.strip().split('\n\n')

with open('day1.input', 'r') as f:
    s = f.read().strip().split('\n\n')

s = [ (*c,) for c in map(lambda c: map(int, c), [c.split('\n') for c in s]) ]
print(max(map(sum, s)))
print(sum(sorted(map(sum, s), reverse=True)[:3]))
