from itertools import count
import re

def parse(lines):
    regex = r'^Disc #\d+ has (\d+) positions; at time=0, it is at position (\d+).$'
    matches = [ re.match(regex, line) for line in lines ]
    return [ tuple(map(int, m.groups())) for m in matches ]

def find_t(state):
    for t in count(0):
        if all((i + t + p) % s == 0 for (p, (s, i)) in enumerate(state, 1)):
            return t
