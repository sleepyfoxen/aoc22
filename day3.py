#!/usr/bin/env python3

from functools import reduce
from string import ascii_letters as letters
from typing import Tuple

s = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''.split('\n')

with open('day3.input', 'r') as f:
    s = f.read().strip().split('\n')

def partition(s: str) -> Tuple[str]:
    return s[:len(s)//2], s[len(s)//2:]

def common(p: Tuple[str]) -> str:
    l, r = p
    return ''.join(set(l) & set(r))

def score(s: str) -> int:
    return letters.index(s) + 1

t = map(partition, s)
t = map(common, t)
t = map(score, t)

print(sum(t))

t = [ set(n) for n in s ]
t = [ t[i:i+3] for i in range(0, len(t), 3) ]
t = [ score(reduce(lambda a, b: a & b, k).pop()) for k in t ]

print(sum(t))


# only unique characters matter, so sets and their __intersection__ method finds
# common characters.
