import collections
import re

wrap = lambda c: lambda f: lambda *a, **k: c(f(*a, **k))

def parse(rooms):
    for line in rooms:
        n, s, c = re.match('^(.*)-(\d+)\[(.*)\]$', line).groups()
        yield (n, int(s), c)

def checksum(name):
    count = collections.Counter(name.replace('-', ''))
    count = sorted((-c, ch) for (ch, c) in count.most_common())
    return ''.join(ch for (_, ch) in count[:5])

def sum_real_rooms(rooms):
    return sum(s for (n, s, c) in parse(rooms) if checksum(n) == c)

@wrap(''.join)
def caesar(text, key):
    for ch in text:
        if ch == '-':
            yield ' '
        elif 'a' <= ch <= 'z':
            v = ord(ch) + (key % 26)
            if v > ord('z'):
                v -= 26
            yield chr(v)

@wrap(list)
def decode_room_names(rooms):
    for n, s, c in parse(rooms):
        if checksum(n) != c:
            continue
        yield (caesar(n, s), s)
