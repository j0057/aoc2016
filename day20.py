wrap = lambda c: lambda f: lambda *a, **k: c(f(*a, **k))

@wrap(sorted)
def parse(text):
    for line in text:
        a, b = line.strip().split('-')
        yield (int(a), int(b)+1)

def merge(ranges):
    result = [list(ranges[0])]
    for (m, n) in ranges[1:]:
        if result[-1][0] <= m <= (result[-1][1]):
            result[-1][1] = max(n, result[-1][1]) 
        else:
            result += [[m, n]]
    return [tuple(t) for t in result]

def find_lowest_free(ranges):
    ranges = merge(ranges)
    return ranges[0][1]

def count_free_ips(ranges):
    blocked = sum(b - a for (a, b) in ranges)
    return 2**32 - blocked
