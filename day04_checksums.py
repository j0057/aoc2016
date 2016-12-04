import collections
import re
import unittest

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

class Test04A_Checksums(unittest.TestCase):
    def test_04a_example(self):
        rooms = [
            'aaaaa-bbb-z-y-x-123[abxyz]',
            'a-b-c-d-e-f-g-h-987[abcde]',
            'not-a-real-room-404[oarel]',
            'totally-real-room-200[decoy]'
        ]
        result = sum_real_rooms(rooms)
        self.assertEqual(result, 1514)

    def test_04a_answer(self):
        with open('input/day04.txt', 'r') as rooms:
            result = sum_real_rooms(rooms)
        self.assertEqual(result, 137896)

class Test04B_ChecksumCipher(unittest.TestCase):
    maxDiff = None

    def test_04b_example(self):
        result = caesar('qzmt-zixmtkozy-ivhz', 343)
        self.assertEqual(result, 'very encrypted name')

    def test_04b_answer(self):
        with open('input/day04.txt', 'r') as rooms:
            result = decode_room_names(rooms)
        #print result
        result = next(s for (n, s) in result
                      if n == 'northpole object storage')
        self.assertEqual(result, 501)
