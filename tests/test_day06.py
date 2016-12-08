from day06_colwords import *

example = [
    'eedadn',
    'drvtee',
    'eandsr',
    'raavrd',
    'atevrs',
    'tsrnev',
    'sdttsa',
    'rasrtv',
    'nssdts',
    'ntnada',
    'svetve',
    'tesnvt',
    'vntsnd',
    'vrdear',
    'dvrsen',
    'enarar'
]

def test_06a_example():
    assert words_from_most_common(example) == 'easter'

def test_06a_answer():
    with open('input/day06.txt', 'r') as f:
        assert words_from_most_common(line.strip() for line in f) == 'tkspfjcc'

def test_06b_example():
    assert words_from_least_common(example) == 'advent'

def test_06b_answer():
    with open('input/day06.txt', 'r') as f:
        assert words_from_least_common(line.strip() for line in f) == 'xrlmbypn'
