
from collections import Counter
import unittest

transpose = lambda items: zip(*items)
commonest = lambda items: Counter(items).most_common(1)[0][0]
least_common = lambda items: Counter(items).most_common()[-1][0]

def words_from_most_common(words):
    return ''.join(commonest(col) for col in transpose(words))

def words_from_least_common(words):
    return ''.join(least_common(col) for col in transpose(words))

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

class Test06A_ColWords(unittest.TestCase):
    def test_06a_example(self):
        result = words_from_most_common(example)
        self.assertEqual(result, 'easter')

    def test_06a_answer(self):
        with open('input/day06.txt', 'r') as f:
            result = words_from_most_common(line.strip() for line in f)
        self.assertEqual(result, 'tkspfjcc')

class Test06B_ColWords(unittest.TestCase):
    def test_06b_example(self):
        result = words_from_least_common(example)
        self.assertEqual(result, 'advent')

    def test_06b_answer(self):
        with open('input/day06.txt', 'r') as f:
            result = words_from_least_common(line.strip() for line in f)
        self.assertEqual(result, 'xrlmbypn')
