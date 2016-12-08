import re
import sys
import time
import unittest

class LEDDisplay(object):
    def __init__(self, sy=6, sx=50):
        self.sy = sy
        self.sx = sx
        self.leds = [ [0] * sx for _ in range(sy) ]

    def __str__(self):
        ch = { 0: '.', 1: '#' }
        return '\n'.join(''.join(ch[v] for v in row) for row in self.leds)

    def __int__(self):
        return sum(sum(row) for row in self.leds)

    def rect(self, y, x):
        for i in range(y):
            self.leds[i][ 0 ] = 1
            self.leds[i][x-1] = 1

        for i in range(x):
            self.leds[ 0 ][i] = 1
            self.leds[y-1][i] = 1

    def fill(self, y, x):
        for r in range(y):
            for c in range(x):
                self.leds[r][c] = 1

    def roty(self, y, n):
        cur = self.leds[y][:]
        for (x, v) in zip(range(n, n + self.sx), cur):
            self.leds[y][x % self.sx] = v

    def rotx(self, x, n):
        cur = list(row[x] for row in self.leds)
        for (y, v) in zip(range(n, n + self.sy), cur):
            self.leds[y % self.sy][x] = v

    def parse(self, script):
        parser = [
            #self.rect, r'^rect (?P<x>\d+)x(?P<y>\d+)$'),
            (self.fill, r'^rect (?P<x>\d+)x(?P<y>\d+)$'),
            (self.rotx, r'^rotate column x=(?P<x>\d+) by (?P<n>\d+)$'),
            (self.roty, r'^rotate row y=(?P<y>\d+) by (?P<n>\d+)$')
        ]
        for command in script:
            for (method, regex) in parser:
                match = re.match(regex, command)
                if not match:
                    continue
                yield (method, { k: int(v) for (k, v) in match.groupdict().items() })
                break
            else:
                raise SyntaxError('Cannot parse command {0!r}'.format(command))

    def run(self, script):
        commands = self.parse(script)
        for (method, kwargs) in commands:
            method(**kwargs)
            yield method, kwargs

    def execute(self, script):
        return sum(1 for _ in self.run(script))

    def animate(self, script, speed=1.0):
        for (method, kwargs) in self.run(script):
            print method.__name__, kwargs, '   '
            print
            print str(self)
            print
            print ''.join(str(sum(led[x] for led in self.leds)) for x in range(self.sx)), int(self)
            time.sleep(speed)
            sys.stdout.write('\033[{0}A'.format(self.sy+4))
        sys.stdout.write('\033[{0}B'.format(self.sy+4))

class Test_08_Display(unittest.TestCase):
    def test_08_example1(self):
        d = LEDDisplay(3, 7)
        d.rect(y=2, x=3)
        self.assertEqual(str(d).split(), ['###....','###....','.......'])
        self.assertEqual(int(d), 6)

    def test_08_example2(self):
        d = LEDDisplay(3, 7)
        d.rect(y=2, x=3)
        d.rotx(x=1, n=1)
        self.assertEqual(str(d).split(), ['#.#....','###....','.#.....'])
        self.assertEqual(int(d), 6)

    def test_08_example3(self):
        d = LEDDisplay(3, 7)
        d.rect(y=2, x=3)
        d.rotx(x=1, n=1)
        d.roty(y=0, n=4)
        self.assertEqual(str(d).split(), ['....#.#','###....','.#.....'])
        self.assertEqual(int(d), 6)

    def test_08_example4(self):
        d = LEDDisplay(3, 7)
        d.rect(y=2, x=3)
        d.rotx(x=1, n=1)
        d.roty(y=0, n=4)
        d.rotx(x=1, n=1)
        self.assertEqual(str(d).split(), ['.#..#.#','#.#....','.#.....'])
        self.assertEqual(int(d), 6)

class Test_08A_DisplayScript(unittest.TestCase):
    def test_08a_example_str(self):
        script = ['rect 3x2', 'rotate column x=1 by 1', 'rotate row y=0 by 4', 'rotate column x=1 by 1']
        d = LEDDisplay(3, 7)
        d.execute(script)
        self.assertEqual(str(d).split(), ['.#..#.#','#.#....','.#.....'])

    def test_08a_example_int(self):
        script = ['rect 3x2']
        d = LEDDisplay(3, 7)
        d.execute(script)
        self.assertEqual(int(d), 6)

    def test_08a_answer(self):
        with open('input/day08.txt') as script:
            d = LEDDisplay()
            d.execute(script)
        #elf.assertEqual(int(d), 124)
        self.assertEqual(int(d), 128)

def main():
    try:
        if len(sys.argv) >= 1:
            speed = int(sys.argv[1]) / 1000.0
        with open('input/day08.txt') as script:
            d = LEDDisplay()
            d.animate(script, speed=speed)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
