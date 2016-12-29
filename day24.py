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

# adapted from day13
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
    clone = lambda m: [ r[:] for r in m ]
    routes = { (a, b): find_path(clone(maze), a, b, avoid(b))
               for (a, b) in itertools.combinations(points, 2) }
    routes = { (a, b): p for ((a, b), p) in routes.items() if p }
    routes.update({ (b, a): p[-2::-1]+[a] for ((a, b), p) in routes.items() })
    return { points.index(a): { points.index(b): p for ((_, b), p) in group }
             for (a, group) in itertools.groupby(sorted(routes.items()), lambda ((a, b), p): a) }

def find_route(start, routes, closed=False):
    closed = (lambda p: p[0] == p[-1]) if closed else (lambda p: True)
    Q = queue.PriorityQueue();
    Q.put((len(routes), 0, [start]))
    best = 10**100
    result = None
    while not Q.empty():
        unvisited, cost, path = Q.get()
        if cost > best:
            continue
        if (unvisited == 0) and closed(path):
            if cost < best:
                best = cost
                result = path
                print 'best:', result, len(result), best
            continue
        a = path[-1]
        for (b, coords) in routes[a].items():
            new_cost = cost + len(coords)
            if new_cost >= best:
                continue
            Q.put((len(routes)-len(set(path+[b])), new_cost, path+[b]))
    return result, reduce(lambda a,b: a+b, [routes[a][b] for a,b in zip(result, result[1:])], [])

if __name__ == '__main__':
    import tests.test_day24
    print '#A'
    tests.test_day24.test_24a_answer()
    print '#B'
    tests.test_day24.test_24b_answer()
