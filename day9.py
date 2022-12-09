#!/usr/bin/env python3

s = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''.split('\n')

s = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''.split('\n')

with open('day9.input', 'r') as f:
    s = f.read().strip().split('\n')

tails = [ (0+0j) for _ in range(10) ]
grid, grid_ = {}, {}

directions = {
    'U': -1+0j,
    'D':  1+0j,
    'L':  0-1j,
    'R':  0+1j
}

def clamp(z: complex) -> complex:
    a, b = z.real, z.imag
    if a == 0: return 0 + (b // abs(b) * 1j)
    if b == 0: return (a // abs(a)) + 0j
    return (a // abs(a) + (b // abs(b) * 1j))

for l in s:
    d, n = l.split(' ')
    d, n = directions[d], int(n)

    for _ in range(n):
        for i, tail in enumerate(tails):
            if i == 0:
                tails[i] += d
                continue

            dist = tails[i - 1] - tail
            if abs(dist) > 1.42:
                tail += clamp(dist)

            tails[i] = tail
            
            if i == 1: grid[tail] = 1
            if i == 9: grid_[tail] = 1

print(sum(grid.values()))
print(sum(grid_.values()))


# 1. make a big grid of zeros.
# 2. set (x, y) = 1 in the grid if the tail touches (x, y) by modelling where
#    the snake segments go.
# 3. (x, y) is represented as y+xj to make the maths easier.
# 4. sum the grid.

# each snake segment `s` follows its predecessor `p` by calculating `p - s`,
# this gives distance and direction. check that distance > sqrt(2) and then
# clamp() the distance to move a maximum of one unit.
