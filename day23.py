from day12 import *

if __name__ == '__main__': 
    with open('input/day23.txt', 'r') as f:
        code = parse(f)
    (ip, reg) = (0, dict(a=7, b=0, c=0, d=0))
    (ip, reg) = run(ip, reg, code)
    assert reg['a'] == None
