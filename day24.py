import itertools
import Queue as queue

def parse(text):
    maze = []
    points = [None] * 10
    for (y, line) in enumerate(text):
        maze.append(list(-1 if ch == '#' else 0 for ch in line.strip()))
        for (x, ch) in enumerate(line):
            if ch.isdigit():
                points[int(ch)] = (y, x)
    return maze, list(p for p in points if p)

def clone(maze):
    return [ row[:] for row in maze ]

def find_next(maze, (y1, x1)):
    for (dy, dx) in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
        y2 = y1 + dy
        x2 = x1 + dx
        if not 0 <= y2 < len(maze):
            continue
        if not 0 <= x2 < len(maze[y2]):
            continue
        if maze[y2][x2]:
            continue
        yield (y2, x2)

def find_path(maze, start, end, avoid):
    route = {start: []}
    queue = [start]
    while queue:
        (y, x) = queue.pop(0)
        if (y, x) == end:
            return route[y, x]
        for (ny, nx) in find_next(maze, (y, x)):
            if (ny, nx) in avoid:
                continue
            maze[ny][nx] = maze[y][x] + 1
            route[ny, nx] = route[y, x] + [(ny, nx)]
            queue.append((ny, nx))
    return None

def find_routes(maze, points):
    avoid = lambda b: [ p for p in points if p != b ]
    routes = { (a, b): find_path(clone(maze), a, b, avoid(b))
               for (a, b) in itertools.combinations(points, 2) }
    routes = { (a, b): p for ((a, b), p) in routes.items() if p }
    routes.update({ (b, a): p[-2::-1]+[a] for ((a, b), p) in routes.items() })
    return { points.index(a): { points.index(b): p for ((_, b), p) in group }
             for (a, group) in itertools.groupby(sorted(routes.items()), lambda ((a, b), p): a) }

def find_route(start, routes, closed=False):
    #import pudb; pudb.set_trace()
    Q = queue.PriorityQueue();
    Q.put((0, len(routes), [start], []))
    best = 10**100
    result = None
    while not Q.empty():
        path_len, unvisited, path, coords = Q.get()
        #print path, len(coords)
        if (unvisited == 0) and (len(coords) < best) and ((not closed) or (path[0] == path[-1])):
            best = len(coords)
            result = path, coords
            print 'best:', result[0], len(result[0]), len(result[1])
            continue
        if best <= len(coords):
            continue
        a = path[-1]
        for (b, coords2) in routes[a].items():
            if len(coords) + len(coords2) >= best:
                continue
            Q.put((len(coords), len(routes)-len(set(path+[b])), path+[b], coords+coords2))
    return result

if __name__ == '__main__':
    import tests.test_day24
    print '#A'
    #tests.test_day24.test_24a_answer()
    print '#B'
    tests.test_day24.test_24b_answer()
