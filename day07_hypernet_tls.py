import re
import itertools
import unittest

def contains_abba(s):
    for i in range(len(s)-3):
        if s[i:i+2] == s[i+3:i+1:-1] and s[i] != s[i+1]:
            return True
    return False

def find_aba(s):
    for i in range(len(s)-2):
        if s[i:i+2:+1] == s[i+2:i:-1] and s[i] != s[i+1]:
            yield s[i:i+3:+1]

def is_hypernet_tls(address):
    parts = re.split(r'[\[\]]', address)
    if any(contains_abba(s) for s in parts[1::2]):
        return False
    return any(contains_abba(s) for s in parts[0::2])

def is_hypernet_ssl(address):
    parts = re.split(r'[\[\]]', address)
    aba = [ x for p in parts[0::2] for x in find_aba(p) ]
    bab = [ x for p in parts[1::2] for x in find_aba(p) ]
    for (a, b) in itertools.product(aba, bab):
        if a[0] == b[1] and a[1] == b[0]:
            return True
    return False

def count_hypernet_tls(addresses):
    return sum(1 for a in addresses if is_hypernet_tls(a))

def count_hypernet_ssl(addresses):
    return sum(1 for a in addresses if is_hypernet_ssl(a))

class Test07A_HypernetTLS(unittest.TestCase):
    def test_07a_example(self):
        result = count_hypernet_tls([
            'abba[mnop]qrst',
            'abcd[bddb]xyyx',
            'aaaa[qwer]tyui',
            'ioxxoj[asdfgh]zxcvbn'
        ])
        self.assertEqual(result, 2)

    def test_07a_answer(self):
        with open('input/day07.txt', 'r') as f:
            result = count_hypernet_tls(line.strip() for line in f)
        self.assertEqual(result, 115)

class Test07B_HypernetSSL(unittest.TestCase):
    def test_07b_example(self):
        print
        result = count_hypernet_ssl([
            'aba[bab]xyz',
            'xyx[xyx]xyx',
            'aaa[kek]eke',
            'zazbz[bzb]cdb'
        ])
        self.assertEqual(result, 3)

    def test_07b_answer(self):
        with open('input/day07.txt', 'r') as f:
            result = count_hypernet_ssl(line.strip() for line in f)
        self.assertEqual(result, 1)
