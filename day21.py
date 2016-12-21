
import re

wrap = lambda c: lambda f: lambda *a, **k: c(f(*a, **k))

last = lambda seq: reduce(lambda _, b: b, seq)

def op_swap_pos(s, x, y):
    s[x], s[y] = s[y], s[x]
    return s

def op_swap_chr(s, x, y):
    return op_swap_pos(s, s.index(x), s.index(y))

def op_rotate_pos(s, d, x):
    return s[x:]  + s[:x]  if d == 'left'  else  \
           s[-x:] + s[:-x] if d == 'right' else 1/0 

def op_rotate_chr(s, x):
    x = s.index(x)
    return op_rotate_pos(s, 'right', (1 + x + (x >= 4)) % len(s))

def op_reverse(s, x, y):
    return s[:x] + s[x:y+1][::-1] + s[y+1:]

def op_move(s, x, y):
    return s[:x] + s[x+1:y+1] + [s[x]] + s[y+1:] if x < y else \
           s[:y] + [s[x]] + s[y:x] + s[x+1:]   if x > y else 1/0

_parser = [
    (op_swap_pos,   [int, int], r'swap position (\d+) with position (\d+)'),
    (op_swap_chr,   [str, str], r'swap letter (\w) with letter (\w)'),
    (op_rotate_pos, [str, int], r'rotate (left|right) (\d+)'),
    (op_rotate_chr, [str],      r'rotate based on position of letter (\w)'),
    (op_reverse,    [int, int], r'reverse positions (\d+) through (\d+)'),
    (op_move,       [int, int], r'move position (\d+) to position (\d+)')
]

def parse(program):
    for instruction in program:
        if not instruction.strip():
            continue
        for (func, types, regex) in _parser:
            match = re.match(regex, instruction)
            if not match:
                continue
            yield (func, [ t(a) for (t, a) in zip(types, match.groups()) ])
            break
        else:
            raise SyntaxError('Error parsing {!r}'.format(instruction))

def run(code, s):
    print '>', s
    for (op, args) in code:
        s = list(s)
        s = op(s, *args)
        print '{:15} {:15} {}'.format(op.__name__, args, s)
        s = ''.join(s)
        yield s
    print '.'

@wrap(lambda r: reversed(list(r)))
def flip(code):
    RL=['right', 'left']
    for (op, args) in code:
        if op is op_rotate_pos:
            yield (op, (RL[1 - RL.index(args[0])], args[1]))
        elif op is op_move:
            yield (op, (args[1], args[0]))
        else:
            yield (op, args)
