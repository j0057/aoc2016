from pudb import set_trace
from day16 import *

def test_16a_dragon_curve_1(): assert dragon_curve(P('1'), 2) == P('100')
def test_16a_dragon_curve_2(): assert dragon_curve(P('0'), 2) == P('001')
def test_16a_dragon_curve_3(): assert dragon_curve(P('11111'), 6) == P('11111000000')
def test_16a_dragon_curve_4(): assert dragon_curve(P('111100001010'), 13) == P('1111000010100101011110000')

def test_16a_checksum_1(): assert checksum(P('110010110100')) == P('100')

def test_16a_example():
    s1 = P('10000')
    (s2, c2) = fill_disk(s1, 20)
    assert c2 == '01100'

def test_16a_answer():
    s1 = P('11110010111001001')
    (s2, c2) = fill_disk(s1, 272)
    assert c2 == '01110011101111011'

def test_16b_answer():
    s1 = P('11110010111001001')
    (s2, c2) = fill_disk(s1, 35651584)
    assert c2 == '11001111011000111'
