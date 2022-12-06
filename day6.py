#!/usr/bin/env python3

s = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

with open('day6.input', 'r') as f:
    s = f.read().strip()

a = next(i for i in range(4, len(s)) if len(set(s[i-4:i])) == 4)
b = next(i for i in range(14, len(s)) if len(set(s[i-14:i])) == 14)

print(a)
print(b)
