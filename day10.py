#!/usr/bin/env python3

s = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''.split('\n')

with open('day10.input', 'r') as f:
    s = f.read().strip().split('\n')

counts = {
    'addx': 2,
    'noop': 1
}

cycle = 0
reg = 1
strs = []

for l in s:
    cycle += 1

    if (cycle - 20) % 40 == 0:
        strs.append(reg * cycle)

    if l.startswith('noop'):
        continue

    if l.startswith('addx'):
        cycle += 1
        if (cycle - 20) % 40 == 0:
            strs.append(reg * cycle)

        reg += int(l.split(' ')[1])

print(sum(strs))


grid = [ [' '] * 40 for _ in range(6) ]  # reset
lines = ( l for l in s )

reg = 1
flag = False
for cycle in range(len(s) * 2):
    if not flag:
        try: line = next(lines)
        except StopIteration: break

    if abs(cycle % 40 - reg) < 2:
        grid[cycle // 40][cycle % 40] = '#'

    if line.startswith('addx'):
        if flag:
            reg += int(line.split(' ')[1])
            flag = False
        else:
            flag = True

for l in grid: print(''.join(l))
