import re

class BalanceBotZoo(object):
    def __init__(self):
        self.bot = {}
        self.output = {}
        self.qa = {}

    def initialize_bots(self, program):
        for line in program:
            m = re.match(r'^value (\d+) goes to bot (\d+)$', line)
            if not m:
                continue
            value, botnum = m.groups()
            value, botnum = int(value), int(botnum)
            self.move(value, botnum, self.bot)

    def parse_passes(self, program):
        result = {}
        for line in program:
            m = re.match(r'^bot (\d+) gives low to (output|bot) (\d+) and high to (output|bot) (\d+)$', line)
            if not m:
                continue
            srcnum, lokind, lonum, hikind, hinum = m.groups()
            srcnum, lonum, hinum = int(srcnum), int(lonum), int(hinum)
            result[srcnum] = (lokind, lonum, hikind, hinum)
        return result

    def execute_passes(self, passes):
        while True:
            #print ' '.join('B{0}:{1!r}'.format(k, v) for (k, v) in self.bot.items())
            try:
                bot_with_two = next(k for (k, v) in self.bot.items() if len(v) == 2)
                lokind, lonum, hikind, hinum = passes[bot_with_two]
                self.bot_passes_values(bot_with_two, getattr(self, lokind), lonum, getattr(self, hikind), hinum)
            except StopIteration:
                break

    def execute(self, program):
        self.initialize_bots(program)
        passes = self.parse_passes(program)
        self.execute_passes(passes)

    def move(self, n, i, d):
        n = int(n)
        if i in d:
            d[i] += [n]
        else:
            d[i] = [n]
        if d == self.bot:
            assert len(d[i]) <= 2

    def bot_passes_values(self, bot, lokind, lo, hikind, hi):
        assert len(self.bot[bot]) == 2
        L = min(*self.bot[bot])
        H = max(*self.bot[bot])
        self.move(L, lo, lokind)
        self.move(H, hi, hikind)
        self.bot[bot] = []
        self.qa[L, H] = bot
