#!/usr/bin/env python3

from collections import defaultdict as ddict
from functools import reduce
from string import ascii_letters as letters
from typing import Tuple, List

s = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''.strip().split('\n')

with open('day3.input', 'r') as f:
    s = f.read().strip().split('\n')

def partition(s: str) -> Tuple[str]:
    return s[:len(s)//2], s[len(s)//2:]

def common(p: Tuple[str]) -> str:
    l, r = p
    return ''.join(set(l).intersection(set(r)))

def score(s: str) -> int:
    return letters.index(s) + 1

t = [ partition(a) for a in s ]
t = [ common(a) for a in t ]
t = [ score(a) for a in t ]

print(sum(t))

t = [ set(n) for n in s ]
t = [ (t[i], t[i+1], t[i+2]) for i in range(0, len(t), 3) ]
t = [ score(reduce(lambda a, b: a.intersection(b), k).pop()) for k in t ]

print(sum(t))
