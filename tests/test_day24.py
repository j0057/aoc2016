from pprint import pprint

from day24 import *

example = [
    '###########',
    '#0.1.....2#',
    '#.#######.#',
    '#4.......3#',
    '###########'
]

def test_24a_parse_maze():
    maze, points = parse(example)

    assert maze[0] == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert maze[1] == [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1]
    assert maze[2] == [-1,  0, -1, -1, -1, -1, -1, -1, -1,  0, -1]
    assert maze[3] == [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1]
    assert maze[4] == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

    assert points == [(1, 1), (1, 3), (1, 9), (3, 9), (3, 1)]

def test_24a_find_path():
    maze, points = parse(example)
    path = find_path(maze, points[0], points[4], avoid=[])
    assert path == [(2, 1), (3, 1)]

def test_24a_find_routes():
    maze, points = parse(example)
    routes = find_routes(maze, points)
    pprint({ a: { b: len(p) for (b, p) in bs.items() } for (a, bs) in routes.items() })
    assert routes[0][4] == [(2, 1), (3, 1)]
    assert routes[4][0] == [(2, 1), (1, 1)]

def test_24a_example():
    maze, points = parse(example)
    routes = find_routes(maze, points)
    nodes, coords = find_route(0, routes)
    assert nodes == [0, 4, 0, 1, 2, 3]
    assert len(coords) == 14

def test_24a_answer():
    with open('input/day24.txt', 'r') as f:
        maze, points = parse(f)
        routes = find_routes(maze, points)
        pprint({ a: { b: len(p) for (b, p) in bs.items() } for (a, bs) in routes.items() })
        nodes, coords = find_route(0, routes)
    assert len(nodes) == 8
    assert len(coords) == 518 #*
    assert nodes == [0, 1, 7, 6, 5, 4, 3, 2]

def test_24b_answer():
    with open('input/day24.txt', 'r') as f:
        maze, points = parse(f)
        routes = find_routes(maze, points)
        pprint({ a: { b: len(p) for (b, p) in bs.items() } for (a, bs) in routes.items() })
        nodes, coords = find_route(0, routes, closed=True)
    assert len(nodes) == 9
    assert len(coords) == 716 #* - this took 109m 11s
    assert nodes == [0, 1, 7, 6, 5, 4, 2, 3, 0]
