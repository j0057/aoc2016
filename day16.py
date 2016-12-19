P = lambda t: map(int, list(t))
T = lambda s: ''.join(str(v) for v in s)

def dragon_curve(a, n):
    while len(a) < n:
        b = reversed(a)
        b = list(1-v for v in b)
        a = a + [0] + b
    return a

def checksum(s):
    while 1:
        s = [ 1 - a ^ b for (a, b) in zip(s[0::2], s[1::2]) ]
        if len(s) % 2 == 1:
            return s

def fill_disk(state, length):
    state = dragon_curve(state, length)[:length]
    return (T(state), T(checksum(state)))
