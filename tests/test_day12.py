from day12 import *

example = [
    'cpy 41 a',
    'inc a',
    'inc a',
    'dec a',
    'jnz a 2',
    'dec a'
]

def test_12a_parser():
    code = parse(example)
    assert code == [
        (op_cpy, ('41', 'a')),
        (op_inc, ('a',)),
        (op_inc, ('a',)),
        (op_dec, ('a',)),
        (op_jnz, ('a', '2')),
        (op_dec, ('a',))
    ]

def test_12a_example():
    (ip, regs) = run(0, REG(), parse(example))
    assert regs['a'] == 42    

def test_12a_answer():
    with open('input/day12.txt', 'r') as f:
        (ip, regs) = run(0, REG(), parse(f))
        assert regs['a'] == 318009 #*

def test_12b_answer():
    with open('input/day12.txt', 'r') as f:
        (ip, regs) = run(0, REG(c=1), parse(f))
        assert regs['a'] == 9227663 #*
