#!/usr/bin/env python2.7

import unittest

def parse(f):
    for line in f:
        if not line: continue
        yield [ int(item) for item in line.split() ]

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
