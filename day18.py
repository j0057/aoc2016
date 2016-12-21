from itertools import islice

def parse(line):
    p = { '.': 0, '^': 1 }
    return [ p[ch] for ch in line ]

f = lambda a, b, c: (a & b & ~c) | (~a & b & c) | (a & ~b & ~c) | (~a & ~b & c)
g = lambda a, b, c: (a & ~c) ^ (~a & c)

def gen_rows(row):
    while True:
        yield row
        row = [ g(a, b, c) for (a, b, c) in zip([0] + row, row, row[1:] + [0]) ]

def count_safe(row, count):
    return sum(r.count(0) for r in islice(gen_rows(row), 0, count))
