from pudb import set_trace

from day17 import *

def test_17a_find_moves_1(): assert list(find_moves('hijkl', (3, 0), ''))  == ['D']
def test_17a_find_moves_2(): assert list(find_moves('hijkl', (2, 0), 'D')) == ['U', 'R']

def test_17a_apply_move_1(): assert apply_move((3, 0), '', 'D')  == (2, 0, 'D')
def test_17a_apply_move_2(): assert apply_move((2, 0), 'D', 'U') == (3, 0, 'DU')

def test_17a_find_example_1(): assert find_path('ihgpwlah') == 'DDRRRD'
def test_17a_find_example_2(): assert find_path('kglvqrro') == 'DDUDRLRRUDRD'
def test_17a_find_example_3(): assert find_path('ulqzkmiv') == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'

def test_17a_answer(): assert find_path('pgflpeqp') == 'RDRLDRDURD'

def test_17b_find_example_1(): assert len(find_longest_path('ihgpwlah')) == 370
def test_17b_find_example_2(): assert len(find_longest_path('kglvqrro')) == 492
def test_17b_find_example_3(): assert len(find_longest_path('ulqzkmiv')) == 830

def test_17b_answer(): assert len(find_longest_path('pgflpeqp')) == 596
