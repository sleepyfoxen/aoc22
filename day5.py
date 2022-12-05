#!/usr/bin/env python3

from copy import deepcopy

s = '''    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''.split('\n\n')

with open('day5.input', 'r') as f:
    s = f.read().split('\n\n')

state, moves = map(lambda t: t.split('\n'), s)
state = list(map(lambda l: l.ljust(len(state[-1]) + 1), state))

stacks = [ [] for s in state.pop() if s.isdigit() ]
for l in state[::-1]:
    for i, k in enumerate(range(1, len(l), 4)):
        c = l[k]
        if not c.isspace():
            stacks[i].append(c)

stacks_ = deepcopy(stacks)

for l in moves:
    if l == '': continue
    _, n, _, s, _, t = l.split(' ')
    n, s, t = map(int, (n, s, t))
    for i in range(n):
        stacks[t - 1].append(stacks[s - 1].pop())

print(''.join(s[-1] for s in stacks))

stacks = stacks_

for l in moves:
    if l == '': continue
    _, n, _, s, _, t = l.split(' ')
    n, s, t = map(int, (n, s, t))
    tmp = []
    for i in range(n):
        tmp.append(stacks[s - 1].pop())
    stacks[t - 1].extend(tmp[::-1])

print(''.join(s[-1] for s in stacks))
