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
    code = parse(example)
    (ip, regs) = (0, dict(a=0, b=0, c=0, d=0))
    (ip, regs) = run(ip, regs, code)
    assert regs['a'] == 42    

def test_12a_answer():
    with open('input/day12.txt', 'r') as challenge:
        code = parse(challenge)
        (ip, regs) = (0, dict(a=0, b=0, c=0, d=0))
        (ip, regs) = run(ip, regs, code)
        assert regs['a'] == 318009 #*

def test_12b_answer():
    with open('input/day12.txt', 'r') as challenge:
        code = parse(challenge)
        (ip, regs) = (0, dict(a=0, b=0, c=1, d=0))
        (ip, regs) = run(ip, regs, code)
        assert regs['a'] == 9227663 #*
