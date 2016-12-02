#!/usr/bin/env python2.7

from math import sin, cos, radians
import unittest

dsin = lambda d: int(sin(radians(d)))
dcos = lambda d: int(cos(radians(d)))

def parse(directions):
    deg = { 'L': -90, 'R': +90 }
    return [ (deg[d[0]], int(d[1:])) for d in directions.split(', ') ]

def walk_bunny_hq(directions):
    #print '>', directions
    c = 0
    x, y = (0, 0)
    for (corner, distance) in parse(directions):
        c = (c + corner) % 360
        dx, dy = dcos(c), dsin(c)
        for _ in range(distance):
            x += dx
            y += dy
            #print c, '(', dx, dy, ') (', x, y, ')'
            yield (x, y)

def bunny_hq(directions):
    for x, y in walk_bunny_hq(directions):
        pass
    return abs(x) + abs(y)

def bunny_hq_twice(directions):
    visited = []
    for x, y in walk_bunny_hq(directions):
        #print x, y
        if (x, y) in visited:
            break
        visited.append((x, y))
    #print x, y
    #print visited
    return abs(x) + abs(y)

class Test01A_BunnyHQ(unittest.TestCase):
    def test_01a_example1(self):
        result = bunny_hq('R2, L3')
        self.assertEqual(result, 5)

    def test_01a_example2(self):
        result = bunny_hq('R2, R2, R2')
        self.assertEqual(result, 2)

    def test_01a_example3(self):
        result = bunny_hq('R5, L5, R5, R3')
        self.assertEqual(result, 12)

    def test_01a_answer(self):
        with open('input/day01.txt', 'r') as f:
            puzzle = f.read()
        result = bunny_hq(puzzle)
        self.assertEqual(result, 236)
        
class Test01B_BunnyHQ(unittest.TestCase):
    def test_01a_example(self):
        result = bunny_hq_twice('R8, R4, R4, R8')
        self.assertEqual(result, 4)

    def test_01a_answer(self):
        with open('input/day01.txt', 'r') as f:
            puzzle = f.read()
        result = bunny_hq_twice(puzzle)
        self.assertEqual(result, 182)
