from day13 import *

def test_13a_gen_maze():
    maze = gen_maze(10, 6, 10)
    assert ''.join(maze[0]) == '.#.####.##'

def test_13a_example():
    maze = gen_maze(10, 6, 10)
    path = find_path(maze, (1, 1), (4, 7))
    assert len(path) == 11

def test_13a_answer():
    maze = gen_maze(1362, 64, 64)
    path = find_path(maze, (1, 1), (39, 31))
    assert len(path) == 82

def test_13b_answer():
    maze = gen_maze(1362, 64, 64)
    path = find_path(maze, (1, 1), (39, 31))
    in50 = sum(sum(1 for v in line if isinstance(v, int) and v <= 50) for line in maze)
    assert in50 == 138 
