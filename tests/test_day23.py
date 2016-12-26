from math import factorial

from day12 import *

example = [
    'cpy 2 a',
    'tgl a',
    'tgl a',
    'tgl a',
    'cpy 1 a',
    'dec a',
    'dec a'
]

def test_23a_ex():
    (ip, regs) = run(0, REG(), parse(example))
    assert regs['a'] == 3

def test_23a_answer():
    with open('input/day23.txt', 'r') as f:
        (ip, regs) = run_verbose(0, REG(a=7), parse(f))
        assert regs['a'] == factorial(7) + 85*76 == 11500

def test_23b_answer():
    with open('input/day23.txt', 'r') as f:
        (ip, regs) = run_verbose(0, REG(a=12), parse(f))
        assert regs['a'] == factorial(12) + 85*76 == 479008060

def test_23b_optimize():
    code0 = parse('cpy 6 c\ncpy 7 d  \ninc a\ndec d\njnz d -2\ndec c\njnz c -5'.split('\n'))
    code1 = parse('cpy 6 c\nmul 7 c a\nnop\nnop\nnop\nnop\nnop'.split('\n'))
    code2 = optimize(code0)
    for c in [code0, code1, code2]:
        (ip, reg) = run(0, REG(a=27, b=42), c)
        assert reg['a'] == 6*7+27
        assert reg['b'] == 42
        assert reg['c'] == 0
        assert reg['d'] == 0
    assert code2 == code1
