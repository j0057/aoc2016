#!/usr/bin/env python2.7

from math import sin, cos, pi

def parse(directions):
    deg = { 'L': -90, 'R': +90 }
    return [ (deg[d[0]], int(d[1:])) for d in directions.split(', ') ]

def bunny_hq(directions):
    #print '>', directions
    c = 0
    x, y = (0, 0)
    for (corner, distance) in parse(directions):
        c = (c + corner) % 360
        dx, dy = int(sin(c / 180 * pi)), int(cos(c / 180 * pi))
        x += dx * distance
        y += dy * distance
        #print corner, distance, dx, dy, x, y
    return abs(x) + abs(y)

assert bunny_hq('R2, L3') == 5
assert bunny_hq('R2, R2, R2') == 2
assert bunny_hq('R5, L5, R5, R3') == 12

print bunny_hq('R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5')

