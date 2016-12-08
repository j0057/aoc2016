import pytest

from day08_led_display import *

@pytest.fixture
def d(): return LEDDisplay(3, 7)

@pytest.fixture
def D(): return LEDDisplay()

def test_08_example(d):
    d.rect(y=2, x=3) ; assert str(d) == '###....\n###....\n.......'
    d.rotx(x=1, n=1) ; assert str(d) == '#.#....\n###....\n.#.....'
    d.roty(y=0, n=4) ; assert str(d) == '....#.#\n###....\n.#.....'
    d.rotx(x=1, n=1) ; assert str(d) == '.#..#.#\n#.#....\n.#.....'
    assert int(d) == 6

def test_08a_example_str(d):
    script = ['rect 3x2', 'rotate column x=1 by 1', 'rotate row y=0 by 4', 'rotate column x=1 by 1']
    d.execute(script)
    assert str(d).split() == ['.#..#.#','#.#....','.#.....']

def test_08a_example_int(d):
    script = ['rect 3x2']
    d.execute(script)
    assert int(d) == 6

def test_08a_answer(D):
    with open('input/day08.txt') as script:
        D.execute(script)
    #ssert int(D) == 124
    assert int(D) == 128
