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

PUZZLE = 'R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, ' \
       + 'L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, ' \
       + 'L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, ' \
       + 'L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, ' \
       + 'R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, ' \
       + 'L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, ' \
       + 'L4, R5, R3, R2, R2, L3, R3, L2, L5'

class Test01_BunnyHQ(unittest.TestCase):
    def test_example1(self):
        result = bunny_hq('R2, L3')
        self.assertEqual(result, 5)

    def test_example2(self):
        result = bunny_hq('R2, R2, R2')
        self.assertEqual(result, 2)

    def test_example3(self):
        result = bunny_hq('R5, L5, R5, R3')
        self.assertEqual(result, 12)

    def test_answer(self):
        result = bunny_hq(PUZZLE)
        self.assertEqual(result, 236)
        
class Test01_BunnyHQ_2(unittest.TestCase):
    def test_example1(self):
        result = bunny_hq_twice('R8, R4, R4, R8')
        self.assertEqual(result, 4)

    def test_answer(self):
        result = bunny_hq_twice(PUZZLE)
        self.assertEqual(result, 182)
