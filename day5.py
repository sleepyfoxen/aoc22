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
    s = f.read().strip().split('\n\n')

state, moves = map(lambda t: t.split('\n'), s)
stacks = [ [] for s in state.pop() if s.isdigit() ]

for l in state[::-1]:
    for i, k in enumerate(range(1, len(l), 4)):
        stacks[i].append(l[k]) if not l[k].isspace() else None

stacks_ = deepcopy(stacks)  # part 2

for l in moves:
    n, s, t = ( int(x) for x in l.split(' ') if x.isdigit() )
    s, t = s - 1, t - 1  # source, target

    stacks[t].extend([ stacks[s].pop() for _ in range(n) ])

    stacks_[s], tmp = stacks_[s][:-n], stacks_[s][-n:]
    stacks_[t].extend(tmp)

print(''.join(s[-1] for s in stacks))
print(''.join(s[-1] for s in stacks_))
