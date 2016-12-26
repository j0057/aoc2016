import re
import os

wrap = lambda c: lambda f: lambda *a, **k: c(f(*a, **k))
last = lambda g: reduce(lambda _, x: x, g)
ilen = lambda g: reduce(lambda n, _: n+1, g, 0)

is_num = lambda s: s.isdigit() or (s[0] == '-' and s[1:].isdigit())

@wrap(list)
def parse(program):
    parser = dict((name.replace('op_', ''), func) for (name, func) in globals().items() if name.startswith('op_'))
    for instruction in program:
        try:
            a = instruction.strip().split()
            yield (parser[a[0]], tuple(a[1:]))
        except KeyError as e:
            raise SyntaxError("Error parsing {0!r}".format(instruction))

def fmt_op(op, args):
    return op.__name__[3:] + ' ' + ' '.join(args)

def _run(ip, regs, code):
    _code = optimize(code)
    prof = [0] * len(code)
    try:
        while ip < len(code):
            prof[ip] += 1
            (op, args) = _code[ip]
            if op is op_tgl:
                (ip, regs) = op(ip, regs, code, *args)
                _code = optimize(code)
            else:
                (ip, regs) = op(ip, regs, *args)
            yield (ip, regs)
    finally:
        print 'profile ({} instructions total)\n'.format(sum(prof)) \
            + '\n'.join('{:10}   {:20} {:20}'.format(p, fmt_op(*s), fmt_op(*f)) for p,s,f in zip(prof, code, _code))

def run(ip, regs, code):
    return last(_run(ip, regs, code))

def run_verbose(ip, regs, code):
    for (ip, regs) in _run(ip, regs, code):
        if 0 <= ip < len(code):
            print '{:10} {:2} [{}]'.format(fmt_op(*code[ip]), ip, ' '.join('{:9}'.format(regs[k]) for k in sorted(regs)))
    return (ip, regs)

def optimize(code):
    def optimizer(slow, fast):
        slow, fast = parse(slow.split(' | ')), parse(fast.split(' | '))
        @wrap(list)
        def optimize(code):
            i = 0
            while i < len(code):
                b, f = {}, False
                for (j, (slow_op, slow_args)) in enumerate(slow):
                    if not (0 <= i+j < len(code)):
                        break
                    code_op, code_args = code[i+j]
                    if code_op != slow_op:
                        break
                    if any(is_num(t) and (c != t) for (t, c) in zip(slow_args, code_args)):
                        break
                    if any((not is_num(c)) and (c != b.get(t, c)) for (t, c) in zip(slow_args, code_args)):
                        break
                    b.update({ t: c for (t, c) in zip(slow_args, code_args) if not is_num(t) })
                else:
                    for (fast_op, fast_args) in fast:
                        yield (fast_op, tuple(t if is_num(t) else b[t] for t in fast_args))
                    i += len(slow)
                    continue
                yield code[i]
                i += 1
        return optimize
    return reduce(lambda _code, func: func(_code), [
        optimizer('cpy Q R | inc P | dec R | jnz R -2 | dec S | jnz S -5',
                  'mul Q S | nop   | nop   | nop      | nop   | nop     '),
        optimizer('inc P   | dec Q | jnz Q -2',
                  'add Q P | nop   | nop     ')
    ], code) if int(os.environ.get('OPTIMIZE', '1')) else code

def res(reg, x):
    return int(x) if is_num(x) else reg[x]

def op_cpy(ip, reg, a, b):
    reg[b] = res(reg, a)
    return (ip + 1, reg)

def op_inc(ip, reg, a):
    reg[a] = (reg[a] + 1)
    return (ip + 1, reg)

def op_dec(ip, reg, a):
    reg[a] = (reg[a] - 1)
    return (ip + 1, reg)

def op_jnz(ip, reg, a, b):
    a = res(reg, a)
    b = res(reg, b)
    if int(a):
        return (ip + int(b), reg)
    else:
        return (ip + 1, reg)

def op_tgl(ip, reg, code, a):
    t = res(reg, a) + ip
    if t < len(code):
        print '!!', t, code[t]
        (op, args) = code[t]
        code[t] = \
            (op_dec, args) if len(args) == 1 and op is op_inc else \
            (op_inc, args) if len(args) == 1 else \
            (op_cpy, args) if len(args) == 2 and op is op_jnz else \
            (op_jnz, args) if len(args) == 2 else 1/0
        print '!!', t, code[t]
        print '!!', ' | '.join('{} {}'.format(i, fmt_op(*c)) for (i, c) in enumerate(code))
    else:
        print '!!', t
    return (ip + 1, reg)

def op_nop(ip, reg):
    return (ip + 1, reg)

def op_mul(ip, reg, a, b):
    reg.update({ 'a': reg['a'] + res(reg, a) * res(reg, b), 'c': 0, 'd': 0 })
    return (ip + 1, reg)

def op_add(ip, reg, a, b):
    reg[b] = reg[b] + res(reg, a)
    if a in reg:
        reg[a] = 0
    return (ip + 1, reg)
