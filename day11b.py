import itertools
import re
import sys
import time
from Queue import Queue

import day11a as A

@A.wrap(tuple)
def parse(lines):
    floors = A.parse(lines)
    return sorted(tuple(
        (a, b)
        for ((_, a), (_, b)) in zip(
            sorted((abs(v), a) for (a, vs) in enumerate(floors) for v in vs if v > 0),
            sorted((abs(v), b) for (b, vs) in enumerate(floors) for v in vs if v < 0))))

def format_state(elevator, floors, clear=False):
    c = { False: "", True: "\033[1A" }
    return "{0} {1} {2!r}  ".format(c[clear], elevator, floors)

def is_end_state(floors):
    return all(f == (3, 3) for f in floors)

def is_ok_state(floors):
    loose = [ a for (a, b) in floors if a != b ]
    other = [ b for (a, b) in floors ]
    return all(f not in other for f in loose)

def find_moves(elevator, floors):
    directions = { 0: [+1], 1: [+1, -1], 2: [+1, -1], 3: [-1] }
    options = [ (i, k) 
                for (i, pair) in enumerate(floors)
                for (k, f) in enumerate(pair)
                if f == elevator ]
    return ((d, list(c)) for d in directions[elevator] 
            for i in [2, 1]
            for c in itertools.combinations(options, i))

def apply_move(move, elevator, floors):
    direction, items = move
    floors = list(list(item) for item in floors)   
    for (a, b) in items:
        floors[a][b] = elevator + direction
    return (elevator + direction, tuple(sorted(tuple(item) for item in floors)))

if __name__ == '__main__':
    #from tests.test_day11 import example
    #(e, f) = (0, parse(example))

    with open('input/day11.txt') as challenge:
        (e, f) = (0, parse(challenge))
        (e, f) = (e, ((0, 0), (0, 0)) + f)

    A.main((e, f), M=A._get_caller_module())
