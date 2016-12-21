#!/usr/bin/env python2.7

from math import sin, cos, radians

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
