import hashlib
from itertools import count, islice, takewhile

class memoize(object):
    def __init__(self, f):
        self.f = f
        self.c = {}
    def __call__(self, *a):
        if a not in self.c:
            self.c[a] = self.f(*a)
        return self.c[a]

H = lambda s, i: hashlib.md5(s + str(i)).hexdigest()
S = lambda s, i: reduce(lambda a, b: hashlib.md5(a).hexdigest(), xrange(2016), H(s, i))
nth = lambda n, g: next(islice(g, n, n+1))
ilen = lambda g: reduce(lambda a, _: a + 1, g, 0)

def triplets(salt, F=H):
    for i in count(0):
        h = F(salt, i)
        for j in range(0, len(h)-2):
            if h[j] != h[j+1] or h[j] != h[j+2]:
                continue
            yield (i, h[j])
            break

def quintuplets(salt, ch, start, F=H):
    return (i for i in xrange(start, start + 1000) if ch*5 in F(salt, i))

def keys(salt, F=H):
    return ((i, ch, H(salt, i))
            for (i, ch) in triplets(salt, F=F)
            if ilen(quintuplets(salt, ch, i+1, F=F)) > 0)
