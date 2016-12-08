import os

import pytest

from day05_crackpass import *

if5 = pytest.mark.skipif('5' not in os.environ.get('TEST', ''), reason='TEST=5 not specified')

@if5
def test_05a_example():
    assert find_pass('abc') == '18f47a30'

@if5
def test_05a_answer():
    with open('input/day05.txt') as f:
        assert find_pass(next(f).strip()) == 'f97c354d'

@if5
def test_05b_example():
    assert find_pass_2('abc') == '05ace8e3'

@if5
def test_05b_answer():
    with open('input/day05.txt') as f:
        assert find_pass_2(next(f).strip()) == '863dde27'
