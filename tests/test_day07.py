from day07 import *

def test_07a_example():
    assert count_hypernet_tls([
        'abba[mnop]qrst',
        'abcd[bddb]xyyx',
        'aaaa[qwer]tyui',
        'ioxxoj[asdfgh]zxcvbn'
    ]) == 2

def test_07a_answer():
    with open('input/day07.txt', 'r') as f:
        assert count_hypernet_tls(line.strip() for line in f) == 115

def test_07b_example():
    assert count_hypernet_ssl([
        'aba[bab]xyz',
        'xyx[xyx]xyx',
        'aaa[kek]eke',
        'zazbz[bzb]cdb'
    ]) == 3

def test_07b_answer():
    with open('input/day07.txt', 'r') as f:
        assert count_hypernet_ssl(line.strip() for line in f) == 231
