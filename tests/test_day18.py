from day18 import *

def test_18a_parse(): assert parse('..^^.') == [0, 0, 1, 1, 0]

def test_18a_demorgan():
    assert all(f(a, b, c) == g(a, b, c) for a in range(2) for b in range(2) for c in range(2))

def test_18a_example_1():
    row0 = parse('..^^.')
    rows = gen_rows(row0)
    assert next(rows) == [0, 0, 1, 1, 0]
    assert next(rows) == [0, 1, 1, 1, 1]
    assert next(rows) == [1, 1, 0, 0, 1]

def test_18a_example_2():
    assert count_safe(parse('.^^.^.^^^^'), 10) == 38

def test_18a_answer():
    with open('input/day18.txt', 'r') as f:
        row0 = parse(f.read().strip())
    assert count_safe(row0, 40) == 1963

def test_18b_answer():
    with open('input/day18.txt', 'r') as f:
        row0 = parse(f.read().strip())
    assert count_safe(row0, 400000) == 20009568
