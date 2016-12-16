import copy
import inspect
import itertools
import re
from Queue import Queue
import time
import sys

_get_caller_module = lambda: inspect.getmodule(sys._getframe(1))

wrap = lambda c: lambda f: lambda *a, **k: c(f(*a, **k))

def _read_elements(filename):
    with open(filename, 'r') as f:
        tuples = (line.strip().split(',') for line in f)
        return { n.lower(): (int(a), s) for (a, s, n) in tuples }

ELEMENTS = _read_elements('input/elements.csv')

@wrap(tuple)
def parse(lines):
    for line in lines:
        chips = re.findall(r'(\w+)-compatible microchip', line)
        gens = re.findall(r'(\w+) generator', line)
        yield tuple(sorted(+ELEMENTS[e][0] for e in chips)) \
            + tuple(sorted(-ELEMENTS[e][0] for e in gens))

def format_state(elevator, floors, clear=False):
    c = { False: "", True: "\033[4A" }
    return c[clear] + "\n".join(
        "F{} {} {}                    ".format(
            floor_num,
            "E" if floor_num == elevator else ".",
            " ".join("{:+2d}".format(v) for v in floor)) 
        for (floor_num, floor) in zip(range(3, -1, -1), floors[::-1]))

def is_end_state(floors):
    return all(not floor for floor in floors[:-1]) and bool(floors[-1])

def is_ok_state(floors):
    for floor in floors:
        loose = [ v for v in floor if v > 0 if not -v in floor ]
        other = [ v for v in floor if v < 0 ]
        if loose and other:
            return False
    return True

def find_moves(elevator, floors):
    directions = { 0: [+1], 1: [+1, -1], 2: [+1, -1], 3: [-1] }
    for d in directions[elevator]:
        for i in [2, 1]:
            for c in itertools.combinations(floors[elevator], i):
                yield (d, list(c))

def apply_move(move, elevator, floors):
    direction, items = move
    floors = list(list(floor) for floor in floors)
    floors[elevator] = [ item for item in floors[elevator] if item not in items ]
    elevator += direction
    floors[elevator] += items
    return (elevator, tuple(tuple(sorted(floor)) for floor in floors))

def search(root, M=_get_caller_module()):
    q = Queue()
    q.put(root)
    shortest = { root: [] }
    while not q.empty():
        (e1, s1) = q.get()
        if M.is_end_state(s1):
            break
        for move in M.find_moves(e1, s1):
            (e2, s2) = M.apply_move(move, e1, s1)
            if not M.is_ok_state(s2):
                continue
            if (e2, s2) not in shortest:
                shortest[e2, s2] = shortest[e1, s1] + [move]
                q.put((e2, s2))
    return shortest[e1, s1]

def main(state, M=_get_caller_module()):
    print M.format_state(*state)
    moves = search(state, M=M)
    print moves
    print len(moves)

if __name__ == '__main__':
    #from tests.test_day11 import example
    #state = (0, parse(example))

    with open('input/day11.txt') as challenge:
        state = (0, parse(challenge))

    main(state)
