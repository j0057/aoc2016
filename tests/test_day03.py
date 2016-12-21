from day03 import *

def test_03a_example():
    triangles = parse('5 10 25\n'.split('\n'))
    assert count_triangles(triangles) == 0

def test_03a_answer():
    with open('input/day03.txt', 'r') as f:
        triangles = parse(f)
    assert count_triangles(triangles) == 1032

def test_03b_example():
    triangles = parse('101 301 501\n102 302 502\n103 303 503\n201 401 601\n202 402 602\n203 403 603\n'.split('\n'))
    triangles = transform_vert(triangles)
    assert count_triangles(triangles) == 6

def test_03b_answer():
    with open('input/day03.txt', 'r') as f:
        triangles = parse(f)
        triangles = transform_vert(triangles)
    assert count_triangles(triangles) == 1838
