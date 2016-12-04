import collections
import re
import unittest

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
