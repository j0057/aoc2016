from day19 import *

def test_19a_example(): assert elephant_party(5) == 3

def test_19a_log2_31(): assert log2(31) == 4
def test_19a_log2_32(): assert log2(32) == 5
def test_19a_log2_63(): assert log2(63) == 5
def test_19a_log2_64(): assert log2(64) == 6

def test_19a_answers_up_to_128():
    result = [ (n, elephant_party(n), fast_elephant_party(n)) for n in range(1, 128) ]
    for (n, a, b) in result:
        print n, a, b
    assert all(a == b for (n, a, b) in result)

def test_19a_answer(): assert fast_elephant_party(3014387) == 1834471 

def test_19b_example_1(): assert elephant_party_across(5) == 2
def test_19b_example_2(): assert elephant_party_across(6) != 6

def test_19b_answers_up_to_128():
    result = [ (n, elephant_party_across(n), fast_elephant_party_across(n)) for n in range(1, 245) ]
    for (n, a, b) in result:
        print '{:3} {:3} {:3} {} {}'.format(n, a, b, log3(n), a-b)
    assert all(a == b for (n, a, b) in result)
    assert all(b > 0  for (_, _, b) in result)

def test_19b_answer(): assert fast_elephant_party_across(3014387) == 1420064

def test_19b_fast_elephant_party_bug_27(): assert fast_elephant_party_across(27) == 27
