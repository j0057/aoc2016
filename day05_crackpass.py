import hashlib
import unittest

wrap = lambda c: lambda f: lambda *a, **k: c(f(*a, **k))

def find_zero(start):
    i = 0
    while 1:
        md5 = hashlib.md5(start + str(i)).hexdigest()
        if md5.startswith('00000'):
            yield md5
        i += 1

@wrap(''.join)
def find_pass(door_id):
    print `door_id`
    return (m[5] for (m, _) in zip(find_zero(door_id), range(8)))

@wrap(''.join)
def find_pass_2(door_id):
    password = ['0'] * 8
    to_be_decoded = set(range(8))
    for m in find_zero(door_id):
        pos = int(m[5], 16)
        if pos > 7:
            continue
        if pos not in to_be_decoded:
            continue
        password[pos] = m[6]
        to_be_decoded.discard(pos)
        if not to_be_decoded:
            break
    return password

class Test05A_CrackPassword(unittest.TestCase):
    def test_05a_example(self):
        result = find_pass('abc')
        self.assertEqual(result, '18f47a30')

    def test_05a_answer(self):
        with open('input/day05.txt') as f:
            result = find_pass(next(f).strip())
        self.assertEqual(result, 'f97c354d')

class Test05B_CrackPassword(unittest.TestCase):
    def test_05b_example(self):
        result = find_pass_2('abc')
        self.assertEqual(result, '05ace8e3')

    def test_05b_answer(self):
        with open('input/day05.txt') as f:
            result = find_pass_2(next(f).strip())
        self.assertEqual(result, '863dde27')

# 06:25 AM ... #194
