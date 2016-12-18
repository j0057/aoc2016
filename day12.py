import re

wrap = lambda c: lambda f: lambda *a, **k: c(f(*a, **k))

@wrap(list)
def parse(program):
    parser = [
        (r'^cpy (\d+) ([a-d])$',    op_cpy_imm),
        (r'^cpy ([a-d]) ([a-d])$',  op_cpy_reg),
        (r'^inc ([a-d])$',          op_inc),
        (r'^dec ([a-d])$',          op_dec),
        (r'^jnz (\d+) (-?\d+)$',    op_jnz_imm),
        (r'^jnz ([a-d]) (-?\d+)$',  op_jnz_reg)
    ]
    for instruction in program:
        for (regex, func) in parser:
            match = re.match(regex, instruction)
            if match:
                yield (func,) + match.groups()
                break
        else:
            raise SyntaxError("Error parsing {0!r}".format(instruction))

def run(ip, regs, code):
    while True:
        if ip >= len(code):
            break
        (op, args) = (code[ip][0], code[ip][1:])
        (ip, regs) = op(ip, regs, *args)
    return (ip, regs)

def op_cpy_imm(ip, reg, v, r):
    reg[r] = int(v)
    return (ip + 1, reg)

def op_cpy_reg(ip, reg, rs, rd):
    reg[rd] = reg[rs]
    return (ip + 1, reg)

def op_inc(ip, reg, r):
    reg[r] += 1
    return (ip + 1, reg)

def op_dec(ip, reg, r):
    reg[r] -= 1
    return (ip + 1, reg)

def op_jnz_imm(ip, reg, v, o):
    if int(v):
        return (ip + int(o), reg)
    else:
        return (ip + 1, reg)

def op_jnz_reg(ip, reg, r, o):
    if reg[r]:
        return (ip + int(o), reg)
    else:
        return (ip + 1, reg)
