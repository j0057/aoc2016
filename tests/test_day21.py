from itertools import izip

from day21 import *

example = [
    ('ebcda', (op_swap_pos, [4, 0]),        'swap position 4 with position 0'),
    ('edcba', (op_swap_chr, ['d', 'b']),    'swap letter d with letter b'),
    ('abcde', (op_reverse, [0, 4]),         'reverse positions 0 through 4'),
    ('bcdea', (op_rotate_pos, ['left', 1]), 'rotate left 1 step'),
    ('bdeac', (op_move, [1, 4]),            'move position 1 to position 4'),
    ('abdec', (op_move, [3, 0]),            'move position 3 to position 0'),
    ('ecabd', (op_rotate_chr, ['b']),       'rotate based on position of letter b'),
    ('decab', (op_rotate_chr, ['d']),       'rotate based on position of letter d')
]
expect = list(exp for (exp, _, _) in example)
ex_code = list(op for (_, op, _) in example)
example = list(instr for (_, _, instr) in example)

def test_21a_parse():
    code = parse(example)
    assert list(code) == ex_code

def test_21a_ex():
    code = parse(example)
    gen = run(code, 'abcde')
    for (exp, result) in izip(expect, gen):
        assert result == exp

def test_21a_answer():
    with open('input/day21.txt', 'r') as program:
        code = parse(program)
        gen = run(code, 'abcdefgh')
        assert last(gen) == 'dgfaehcb' #*

def _test_21b_ex():
    code = list(parse(example))
    gen1 = run(code, 'abcde')
    gen2 = run(flip(code), 'decab')
    assert last(gen1) == 'decab'
    assert last(gen2) == 'abcde'

def _test_21b_answer():
    with open('input/day21.txt', 'r') as program:
        code = parse(program)
        gen = run(flip(code), 'fbgdceah')
        result = last(gen)
        assert result == 'fdhgacbe'
        assert result != 'hbefcadg'

def test_21b_answer_by_force():
    with open('input/day21.txt', 'r') as program:
        code = parse(program)
        assert brute(code, 'fbgdceah') == 'fdhgacbe' #*

def test_21b_bug():
    c = 'fdhgacbe'
    with open('input/day21.txt', 'r') as program:
        code = list(parse(program))
        for i in range(1, len(code)):
            p1 = brute(code[:i], c)
            p2 = last(run(flip(code[:i]), c))
            print i, p1, p2
            assert p1 == p2

def test_21b_rotate_pos_right():
    assert op_rotate_pos('fdhgacbe', 'right', 2) == 'befdhgac'
