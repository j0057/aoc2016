
from collections import Counter

transpose = lambda items: zip(*items)
commonest = lambda items: Counter(items).most_common(1)[0][0]
least_common = lambda items: Counter(items).most_common()[-1][0]

def words_from_most_common(words):
    return ''.join(commonest(col) for col in transpose(words))

def words_from_least_common(words):
    return ''.join(least_common(col) for col in transpose(words))
