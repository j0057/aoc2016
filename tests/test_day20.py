
from day20 import *

example = ['5-8', '0-2', '4-7', '9-10']

def test_20a_parse():
    assert parse(example) == [(0, 3), (4, 8), (5, 9), (9, 11)]

def test_20a_merge():
    ranges = parse(example)
    ranges = merge(ranges)
    assert ranges == [(0, 3), (4, 11)]

def test_20a_example():
    ranges = parse(example)
    ranges = merge(ranges)
    assert find_lowest_free(ranges) == 3

def test_20a_answer():
    with open('input/day20.txt', 'r') as f:
        ranges = parse(f)
        ranges = merge(ranges)
        print '\n'.join('{:10} {:10}'.format(a, b) for (a, b) in ranges)
    assert find_lowest_free(ranges) == 17348574

def test_20b_answer():
    with open('input/day20.txt', 'r') as f:
        ranges = parse(f)
        ranges = merge(ranges)
    assert count_free_ips(ranges) == 104
