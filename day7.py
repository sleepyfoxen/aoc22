#!/usr/bin/env python3

from collections import defaultdict as ddict

s = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''.strip().split('$')

with open('day7.input', 'r') as f:
    s = f.read().strip().split('$')

s = [ t.strip().split('\n') for t in s if t ]
pwd = []
paths = ddict(int)

for c in s:
    cmd, c = c[0], c[1:]

    if cmd.startswith('cd '):
        _, tmp = cmd.split(' ')
        pwd.pop() if tmp == '..' else pwd.append(tmp)

    if cmd == 'ls':
        sz = sum(int(t.split(' ')[0]) for t in c if not t.startswith('dir '))
        paths[tuple(pwd)] += sz

for p in sorted(paths, key=len, reverse=True):
    paths[p[:-1]] += paths[p]

needed = paths[('/',)] - 40000000
print(sum(sz for sz in paths.values() if sz < 100000))
print(min(sz for sz in paths.values() if sz >= needed))


# the input is split on $ first, then by newline, so output of commands ends up
# in the same processing block as their input. `pwd` acts as a stack and its
# value is taken as a key to the (path, size) dictionary, which is used to look
# up the answers. initially the value, `sz` only includes its own directory
# but after the input is fully read, the parent directory sizes are updated.
