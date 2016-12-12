from day10_balance_bots import *

def test_10a_example():
    instructions = [
        'value 5 goes to bot 2',
        'bot 2 gives low to bot 1 and high to bot 0',
        'value 3 goes to bot 1',
        'bot 1 gives low to output 1 and high to bot 0',
        'bot 0 gives low to output 2 and high to output 0',
        'value 2 goes to bot 2'
    ]
    zoo = BalanceBotZoo()
    zoo.execute(instructions)

    assert zoo.output[0] == [5]
    assert zoo.output[1] == [2]
    assert zoo.output[2] == [3]

    assert zoo.qa[2, 5] == 2

def test_10a_answer():
    with open('input/day10.txt') as f:
        program = [ line for line in f ]
    zoo = BalanceBotZoo()
    zoo.execute(program)
    assert zoo.qa[17, 61] == 101

def test_10b_answer():
    with open('input/day10.txt') as f:
        program = [ line for line in f ]
    zoo = BalanceBotZoo()
    zoo.execute(program)
    result = zoo.output[0][0] * zoo.output[1][0] * zoo.output[2][0]
    assert result == 37789
