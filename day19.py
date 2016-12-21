from math import log

log2 = lambda n: int(log(n, 2))
log3 = lambda n: int(log(n, 3))

def elephant_party(n):
    elves = range(1, n+1)
    i = 0
    while len(elves) > 1:
        j = (i + 1) % len(elves)
        del elves[j]
        i = 0 if i > j else (i + 1) % len(elves)
    return elves[0]

def fast_elephant_party(n):
    return (n - 2**log2(n)) * 2 + 1

def elephant_party_across(n):
    elves = range(1, n+1)
    i = 0
    while len(elves) > 1:
        j = (i + (len(elves) / 2)) % len(elves)
        del elves[j]
        if j < i: i -= 1
        i = (i + 1) % len(elves)
    return elves[0]

def fast_elephant_party_across(n):
    return (n - 3**log3(n) + max(n - 2 * 3**log3(n), 0)) or n
