
from day09 import *

with open('input/day09.txt', 'r') as compressed:
    c = compressed.read().strip()

def test_09a_ex1(): assert dec('ADVENT') == 'ADVENT'
def test_09a_ex2(): assert dec('A(1x5)BC') == 'ABBBBBC'
def test_09a_ex3(): assert dec('(3x3)XYZ') == 'XYZXYZXYZ'
def test_09a_ex4(): assert dec('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG'
def test_09a_ex5(): assert dec('(6x1)(1x3)A') == '(1x3)A'
def test_09a_ex6(): assert dec('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY'

def test_09a_answer(): assert len(dec(c)) == 99145

def test_09b_ex1(): assert dec2('(3x3)XYZ') == 9
def test_09b_ex2(): assert dec2('X(8x2)(3x3)ABCY') == 20
def test_09b_ex3(): assert dec2('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920
def test_09b_ex4(): assert dec2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTx(18x9)(3x2)TWO(5x7)SEVEN') == 445

def test_09b_answer(): assert dec2(c) == 10943094568
