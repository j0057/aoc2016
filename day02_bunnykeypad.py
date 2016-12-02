#!/usr/bin/env python2.7

import unittest

_ = object()

keypad = [[_, _, _, _, _],
          [_, 1, 2, 3, _],
          [_, 4, 5, 6, _],
          [_, 7, 8, 9, _],
          [_, _, _, _, _]][::-1]

moves = {'U':(+1,0),
         'D':(-1,0),
         'L':(0,-1),
         'R':(0,+1)}

# turn iterator into list
listify = lambda f: lambda *a, **k: list(f(*a, **k))

def listify(func):
    def listify_wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        result = list(result)
        return result
    return listify_wrapped

def parse(directions):
    for line in directions.split('\n'):
        if not line:
            break
        yield line

@listify
def bunny_keypad(directions):
    y, x = 2, 2
    for line in parse(directions):
        #print line
        for move in line:
            #print y, x, move
            dy, dx = moves[move]
            if keypad[y + dy][x] != _: y += dy
            if keypad[y][x + dx] != _: x += dx
        #print '-->', keypad[y][x]
        yield keypad[y][x]

class Test02A_BunnyKeyPad(unittest.TestCase):
    def test_02a_example(self):
        result = bunny_keypad('ULL\nRRDDD\nLURDL\nUUUUD\n')
        self.assertEqual(result, [1, 9, 8, 5])

    def test_02a_answer(self):
        with open('input/day02.txt', 'r') as f:
            puzzle = f.read()
        result = bunny_keypad(puzzle)
        self.assertEqual(result, [3, 3, 4, 4, 4])
