
def is_wall(seed, y, x):
    return bin(x*x + 3*x + 2*x*y + y + y*y + seed).count('1') & 1

def gen_maze(seed, sy, sx):
    return [ [ '.#'[is_wall(seed, y, x)] for x in range(sx) ] for y in range(sy) ]

def find_next(maze, (y1, x1)):
    for (dy, dx) in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
        y2 = y1 + dy
        x2 = x1 + dx
        if not 0 <= y2 < len(maze):
            continue
        if not 0 <= x2 < len(maze[y2]):
            continue
        if maze[y2][x2] != '.':
            continue
        yield (y2, x2)

def find_path(maze, start, end):
    maze[start[0]][start[1]] = 0
    route = { start: [] }
    queue = [start]
    while queue:
        (y, x) = queue.pop(0)
        if (y, x) == end:
            break
        for (ny, nx) in find_next(maze, (y, x)):
            maze[ny][nx] = maze[y][x] + 1
            route[ny, nx] = route[y, x] + [(ny, nx)]
            queue.append((ny, nx))
    else:
        raise Exception("Didn't find end position at {0!r}; got stranded at {1!r}".format(end, (y, x)))
    return route[y, x]

def print_maze(maze):
    for line in maze:
        print ' '.join('%3s' % c for c in line)
