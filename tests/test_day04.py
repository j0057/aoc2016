from day04 import *

def test_04a_example():
    rooms = [
        'aaaaa-bbb-z-y-x-123[abxyz]',
        'a-b-c-d-e-f-g-h-987[abcde]',
        'not-a-real-room-404[oarel]',
        'totally-real-room-200[decoy]'
    ]
    assert sum_real_rooms(rooms) == 1514

def test_04a_answer():
    with open('input/day04.txt', 'r') as rooms:
        assert sum_real_rooms(rooms) == 137896

def test_04b_example():
    assert caesar('qzmt-zixmtkozy-ivhz', 343) == 'very encrypted name'

def test_04b_answer():
    with open('input/day04.txt', 'r') as rooms:
        result =  decode_room_names(rooms)
        #print result
        result = next(s for (n, s) in result if n == 'northpole object storage')
    assert result == 501
