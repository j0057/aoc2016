
from day12 import *

example = [
    'cpy 25 c',
    'out c',
    'out 23'
]

def test_25a_ex():
    code = parse(example)
    (ip, reg) = run(0, REG(out=[]), code)
    assert reg['c'] == 25
    assert reg['out'] == [25, 23]

def test_25a_answer():
    with open('input/day25.txt', 'r') as f:
        (ip, reg) = run(0, REG(a=175, out=[]), parse(f)) #*
        assert reg['out'] == [0, 1, 0, 1, 0, 1, 0, 1]
