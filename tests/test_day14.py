from day14 import *

k = 'jlmsuwbz'

def test_14a_triplets_0(): assert nth(0, triplets('abc')) == (18, '8')
def test_14a_triplets_1(): assert nth(1, triplets('abc')) == (39, 'e')

def test_14a_triplets_1180():  assert reduce(lambda a, b: b, takewhile(lambda (i,_): i<=1180,  triplets(k)))[0] == 1180
def test_14a_triplets_34487(): assert reduce(lambda a, b: b, takewhile(lambda (i,_): i<=34487, triplets(k)))[0] == 34487

def test_14a_quintuplets_18(): assert len(list(quintuplets('abc', '8', 18+1))) == 0
def test_14a_quintuplets_39(): assert len(list(quintuplets('abc', 'e', 39+1))) > 0
def test_14a_quintuplets_92(): assert len(list(quintuplets('abc', '9', 92+1))) > 0

def test_14a_quintuplets_34487(): assert len(list(quintuplets(k, '2', 34487+1))) > 0

def test_14a_example_0():  assert nth(0,  keys('abc'))[0] == 39
def test_14a_example_1():  assert nth(1,  keys('abc'))[0] == 92
def test_14a_example_22(): assert nth(22, keys('abc'))[0] == 7833
def test_14a_example_23(): assert nth(23, keys('abc'))[0] == 7858
def test_14a_example_24(): assert nth(24, keys('abc'))[0] == 7918
def test_14a_example_63(): assert nth(63, keys('abc'))[0] == 22728

def test_14a_answer_56(): assert nth(56, keys(k))[0] == 34463
def test_14a_answer_57(): assert nth(57, keys(k))[0] == 34487
def test_14a_answer_63(): assert nth(63, keys(k))[0] == 35186

def test_14b_key_stretch(): assert S('abc', 0) == 'a107ff634856bb300138cac6568c0f24'

def test_14b_example_0():  assert nth(0,  keys('abc', F=memoize(S)))[0] == 10
def test_14b_example_63(): assert nth(63, keys('abc', F=memoize(S)))[0] == 22551

def test_14b_answer(): assert nth(63, keys(k, F=memoize(S)))[0] == 22429
