
from day22 import *

def test_22a_answer():
    with open('input/day22.txt', 'r') as f:
        disks = parse(f)
        gen = lambda: find_combinations(disks)
        assert ilen(gen()) == 967 #*

def test_22a_grid():
    with open('input/day22.txt', 'r') as f:
        disks = grid(parse(f))
        disks[0][32] = (91, 71, 20, -1)
        dump(disks)

    assert len(disks) == 30
    assert len(disks[0]) == 33

    assert next((y, x)
                for (y, row) in enumerate(disks)
                for (x, (s, u, a, p)) in enumerate(row)
                if p == 0) == (12, 26)

    p  = move(disks, (12, 26), (12, 10))
    p += move(disks, (12, 10), ( 0, 10))
    p += move(disks, ( 0, 10), ( 0, 32))
    
    for i in range(32, 1, -1):
        p += move(disks, ( 0, i  ), ( 1, i  ))
        p += move(disks, ( 1, i  ), ( 1, i-2))
        p += move(disks, ( 1, i-2), ( 0, i-2))
        p += move(disks, ( 0, i-2), ( 0, i-1))

    dump(disks)

    assert p == 205 #*
