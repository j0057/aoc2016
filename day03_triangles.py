#!/usr/bin/env python2.7

import unittest

listify = lambda f: lambda *a, **k: list(f(*a, **k))

@listify
def parse(f):
    for line in f:
        if not line: continue
        yield [ int(item) for item in line.split() ]

def transform_vert(lines):
    for (line1, line2, line3) in zip(lines[::3], lines[1::3], lines[2::3]):
        for x in range(3):
            yield [ line1[x], line2[x], line3[x] ]

def is_triangle(a, b, c):
    return a + b > c

def count_triangles(triangles):
    result = 0
    for (a, b, c) in map(sorted, triangles):
        if is_triangle(a, b, c):
            result += 1
    return result

class Test03A_Triangles(unittest.TestCase):
    def test_03a_example(self):
        triangles = parse('5 10 25\n'.split('\n'))
        result = count_triangles(triangles)
        self.assertEqual(result, 0)

    def test_03a_answer(self):
        with open('input/day03.txt', 'r') as f:
            triangles = parse(f)
            result = count_triangles(triangles)
        self.assertEqual(result, 1032)

class Test03B_Triangles(unittest.TestCase):
    def test_03b_example(self):
        triangles = parse('101 301 501\n102 302 502\n103 303 503\n201 401 601\n202 402 602\n203 403 603\n'.split('\n'))
        triangles = transform_vert(triangles)
        result = count_triangles(triangles)
        self.assertEqual(result, 6)

    def test_03b_answer(self):
        with open('input/day03.txt', 'r') as f:
            triangles = parse(f)
            triangles = transform_vert(triangles)
            result = count_triangles(triangles)
        self.assertEqual(result, 1838)
