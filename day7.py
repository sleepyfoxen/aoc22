#!/usr/bin/env python3

from typing import List
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
    if len(c) == 1 and c[0].startswith('cd '):
        _, tmp = c[0].split(' ')
        if tmp == '..': pwd.pop()
        else: pwd.append(tmp)

    if c[0] == 'ls':
        sz = sum(map(int, (t.split(' ')[0]
                           for t in c[1:] if not t.startswith('dir '))))
        paths[tuple(pwd)] += sz

for p in sorted(paths, key=len, reverse=True):
    paths[p[:-1]] += paths[p]

needed = 30000000 - (70000000 - paths[('/',)])
print(sum(sz for sz in paths.values() if sz < 100000))
print(min(sz for sz in paths.values() if sz >= needed))
