
from day15 import *

example = [
    'Disc #1 has 5 positions; at time=0, it is at position 4.',
    'Disc #2 has 2 positions; at time=0, it is at position 1.'
]

def test_15a_parse(): assert parse(example) == [(5, 4), (2, 1)]

def test_15a_example(): 
    state = parse(example)
    assert find_t(state) == 5

def test_15a_answer():
    with open('input/day15.txt', 'r') as challenge:
        state = parse(challenge)
    assert find_t(state) == 148737

def test_15b_answer():
    with open('input/day15.txt', 'r') as challenge:
        state = parse(challenge)
        state.append((11, 0))
    assert find_t(state) == 2353212
