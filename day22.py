
import itertools
import re

wrap = lambda c: lambda f: lambda *a, **k: c(f(*a, **k))
ilen = lambda g: reduce(lambda a, _: a+1, g, 0)

@wrap(sorted)
def parse(output):
    for line in output:
        if not line.startswith('/dev/grid/node-'):
            continue
        node, size, used, avail, usep = line.split()
        _, x, y = node.split('-')
        yield int(y[1:]), int(x[1:]), int(size[:-1]), int(used[:-1]), int(avail[:-1]), int(usep[:-1])

def grid(disks):
    return [ [ (size, used, avail, perc) for (_, _, size, used, avail, perc) in row ]
             for (y, row) in itertools.groupby(disks, lambda d: d[0]) ]

def find_combinations(disks):
    for (a, b) in itertools.permutations(disks, 2):
        ((y1, x1, s1, u1, a1, p1), (y2, x2, s2, u2, a2, p2)) = (a, b)
        if u1 == 0:
            continue
        if (y1, x1) == (y2, x2):
            continue
        if u1 <= a2:
            yield ((y1, x1), (y2, x2))

def dump(disks):
    print '['+'\n '.join(''.join('_' if p == 0 else '#' if p >= 95 else '$' if p == -1 else '.'
                                 for (s, u, a, p) in row)
                         for row in disks)+']'

def move(grid, (y1, x1), (y2, x2)):
    dy, dx = -cmp(y1, y2), -cmp(x1, x2)
    cy, cx = y1, x1
    m = 0
    while (cy, cx) != (y2, x2):
        ny, nx = cy + dy, cx + dx
        grid[cy][cx], grid[ny][nx] = grid[ny][nx], grid[cy][cx]
        m += 1
        cy, cx = ny, nx
    return m
