from day02_bunnykeypad import *

def test_02a_example():
    assert bunny_keypad('ULL\nRRDDD\nLURDL\nUUUUD\n') == '1985'

def test_02a_answer():
    with open('input/day02.txt', 'r') as f:
        puzzle = f.read()
    assert bunny_keypad(puzzle) == '33444'

def test_02b_example():
    assert bunny_keypad_really('ULL\nRRDDD\nLURDL\nUUUUD\n') == '5DB3'

def test_02b_answer():
    with open('input/day02.txt', 'r') as f:
        puzzle = f.read()
    assert bunny_keypad_really(puzzle) == '446A6'
