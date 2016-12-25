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
    code = parse(example)
    (ip, regs) = (0, dict(a=0, b=0, c=0, d=0))
    (ip, regs) = run(ip, regs, code)
    assert regs['a'] == 3

def test_23a_answer():
    with open('input/day23.txt', 'r') as f:
        code = parse(f)
    (ip, regs) = (0, dict(a=7, b=0, c=0, d=0))
    (ip, regs) = run_verbose(ip, regs, code)
    assert regs['a'] == factorial(7) + 85*76 == 11500

def test_23b_answer():
    with open('input/day23.txt', 'r') as f:
        code = parse(f)
    (ip, regs) = (0, dict(a=12, b=0, c=0, d=0))
    (ip, regs) = run_verbose(ip, regs, code)
    assert regs['a'] == factorial(12) + 85*76 == 479008060

def test_23b_optimize():
    code0 = parse('cpy 6 c\ncpy 7 d\ninc a\ndec d\njnz d -2\ndec c\njnz c -5'.split('\n'))
    code1 = parse('cpy 6 c\nmul 7 c\nnop\nnop\nnop\nnop\nnop'.split('\n'))
    code2 = optimize(code0)
    for c in [code0, code1, code2]:
        (ip, reg) = run(0, dict(a=27, b=0, c=0, d=0), c)
        assert reg['a'] == 6*7+27
    assert code2 == code1
