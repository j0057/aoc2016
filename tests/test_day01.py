from day01 import *

def test_01a_example1():
    assert bunny_hq('R2, L3') == 5

def test_01a_example2():
    assert bunny_hq('R2, R2, R2') == 2

def test_01a_example3():
    assert bunny_hq('R5, L5, R5, R3') == 12

def test_01a_answer():
    with open('input/day01.txt', 'r') as f:
        puzzle = f.read()
    assert bunny_hq(puzzle) == 236
    
def test_01b_example():
    assert bunny_hq_twice('R8, R4, R4, R8') == 4

def test_01b_answer():
    with open('input/day01.txt', 'r') as f:
        puzzle = f.read()
    assert bunny_hq_twice(puzzle) == 182
