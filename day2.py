#!/usr/bin/env python3

s = '''A Y
B X
C Z'''.split('\n')

with open('day2.input', 'r') as f:
    s = f.read().strip().split('\n')

s = [ c.split(' ') for c in s ]
m = {
    'A': { 'X': 4, 'Y': 8, 'Z': 3 },  # rock
    'B': { 'X': 1, 'Y': 5, 'Z': 9 },  # paper
    'C': { 'X': 7, 'Y': 2, 'Z': 6 }   # scissors
}

for c in s:
    c.append(m[c[0]][c[1]])

m = {
    'A': { 'X': 3, 'Y': 4, 'Z': 8 },  # rock
    'B': { 'X': 1, 'Y': 5, 'Z': 9 },  # paper
    'C': { 'X': 2, 'Y': 6, 'Z': 7 }   # scissors
}

for c in s:
    c.append(m[c[0]][c[1]])

print(sum(map(lambda t: t[2], s)))
print(sum(map(lambda t: t[3], s)))
