import os

import pytest

import day11a as A
import day11b as B

if11 = pytest.mark.skipif('11' not in os.environ.get('TEST', '').split(','), reason='TEST=11 not specified')

example = [
    'The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip',
    'The second floor contains a hydrogen generator.',
    'The third floor contains a lithium generator.',
    'The fourth floor contains nothing relevant'
]

def test_11a_elements(): assert A.ELEMENTS['polonium'] == (84, 'Po')

def test_11a_example_parser(): assert A.parse(example) == ((1, 3), (-1,), (-3,), ())
def test_11b_example_parser(): assert B.parse(example) == ((0,1), (0,2))

def test_11a_end_state_00(): assert A.is_end_state(((), (), (-1,), (+1, -3, +3))) == False
def test_11a_end_state_01(): assert A.is_end_state(((1, 3), (-1,), (-3,), ())) == False
def test_11a_end_state_1(): assert A.is_end_state(((), (), (), (-1, +1, -3, +3))) == True

def test_11a_ok_state_0(): assert A.is_ok_state(((), (-3,), (-1, +1, +3), ())) == False
def test_11a_ok_state_1(): assert A.is_ok_state(((+3,), (-3,), (-1, +1), ())) == True

def test_11b_ok_state_0(): assert B.is_ok_state(((2,1), (2,2))) == False
def test_11b_ok_state_1(): assert B.is_ok_state(((0,1), (2,2))) == True

def test_11a_find_moves():
    floors = A.parse(example)
    moves = A.find_moves(0, floors)
    assert list(moves) == [ (+1, [1, 3]), (+1, [1]), (+1, [3]) ]

def test_11b_find_moves():
    floors = B.parse(example)
    moves = B.find_moves(0, floors)
    assert list(moves) == [ (+1, [(0, 0), (1, 0)]), (+1, [(0, 0)]), (+1, [(1, 0)]) ]

def test_11a_apply_move():
    state1 = (0, A.parse(example))
    state2 = A.apply_move((+1, [1]), *state1)
    assert state2 == (1, ((3,), (-1, 1), (-3,), ()))

def test_11b_apply_move():
    state1 = (0, B.parse(example))
    state2 = B.apply_move((+1, [(0,0)]), *state1)
    assert state2 == (1, ((0, 2), (1, 1)))

@if11
def test_11a_example():
    state = (0, A.parse(example))
    moves = A.search(state)
    assert len(moves) == 11

@if11
def test_11a_answer():
    with open('input/day11.txt', 'r') as f:
        state = (0, A.parse(f))
    moves = A.search(state)
    assert len(moves) == 47

@if11
def test_11b_answer():
    with open('input/day11.txt', 'r') as f:
        (e, f) = (0, B.parse(f))
        (e, f) = (e, ((0, 0), (0, 0)) + f)
    moves = A.search((e, f), M=B)
    assert len(moves) == 71
