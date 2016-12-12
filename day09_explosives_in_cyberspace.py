import re

def dec1(s):
    while s:
        m = re.match(r'^\((\d+)x(\d+)\)(.*)$', s)
        if m:
            c, n, s = m.groups()
            c, n = int(c), int(n)
            yield s[:c] * n
            s = s[c:]

        elif '(' in s:
            i = s.index('(')
            yield s[:i]
            s = s[i:]

        else:
            yield s
            break

dec = lambda s: ''.join(dec1(s))

def dec2(s):
    if not s:
        return 0

    m = re.match(r'^\((\d+)x(\d+)\)(.*)$', s)
    if m:
        c, n, t = m.groups()
        c, n = int(c), int(n)
        return n * dec2(t[:c]) + dec2(t[c:])

    m = re.match(r'^([^(]*)(.*)$', s)
    if m:
        r, t = m.groups()
        return len(r) + dec2(t)
