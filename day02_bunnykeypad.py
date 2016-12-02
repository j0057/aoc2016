#!/usr/bin/env python2.7

import unittest

_ = object()

keypad = [[_, _, _, _, _],
          [_, 1, 2, 3, _],
          [_, 4, 5, 6, _],
          [_, 7, 8, 9, _],
          [_, _, _, _, _]][::-1]

keypad_b = [[_,  _,  _,  _,  _,  _,  _],
            [_,  _,  _,  1,  _,  _,  _],
            [_,  _,  2,  3,  4,  _,  _],
            [_,  5,  6,  7,  8,  9,  _],
            [_,  _, 10, 11, 12,  _,  _],
            [_,  _,  _, 13,  _,  _,  _],
            [_,  _,  _,  _,  _,  _,  _]][::-1]

moves = {'U':(+1,0),
         'D':(-1,0),
         'L':(0,-1),
         'R':(0,+1)}

chars = '0123456789ABCDEF'

# turn iterator into list
stringify = lambda f: lambda *a, **k: ''.join(chars[n] for n in f(*a, **k))

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

@stringify
def bunny_keypad(directions, keypad=keypad, y=2, x=2):
    for line in parse(directions):
        #print line
        for move in line:
            #print y, x, move
            dy, dx = moves[move]
            if keypad[y + dy][x] != _: y += dy
            if keypad[y][x + dx] != _: x += dx
        #print '-->', keypad[y][x]
        yield keypad[y][x]

def bunny_keypad_really(directions):
    return bunny_keypad(directions, keypad_b, y=3, x=1)

class Test02A_BunnyKeyPad(unittest.TestCase):
    def test_02a_example(self):
        result = bunny_keypad('ULL\nRRDDD\nLURDL\nUUUUD\n')
        self.assertEqual(result, '1985')

    def test_02a_answer(self):
        with open('input/day02.txt', 'r') as f:
            puzzle = f.read()
        result = bunny_keypad(puzzle)
        self.assertEqual(result, '33444')

class Test02B_BunnyKeyPad(unittest.TestCase):
    def test_02b_example(self):
        result = bunny_keypad_really('ULL\nRRDDD\nLURDL\nUUUUD\n')
        self.assertEqual(result, '5DB3')

    def test_02b_answer(self):
        with open('input/day02.txt', 'r') as f:
            puzzle = f.read()
        result = bunny_keypad_really(puzzle)
        self.assertEqual(result, '446A6')
