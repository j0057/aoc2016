#!/usr/bin/env python2.7

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

