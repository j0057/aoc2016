import hashlib

def find_moves(key, (y, x), path):
    h = hashlib.md5(key + path).hexdigest()
    if h[0] > 'a' and y < 3: yield 'U'
    if h[1] > 'a' and y > 0: yield 'D'
    if h[2] > 'a' and x > 0: yield 'L'
    if h[3] > 'a' and x < 3: yield 'R'

def apply_move((y, x), path, move):
    (dy, dx) = { 'U': (+1,0), 'D': (-1,0), 'L':(0,-1), 'R':(0,+1) }[move]
    return (y + dy, x + dx, path + move)

def find_path(key):
    queue = [(3, 0, '')]
    while queue:
        (y, x, path) = queue.pop(0)
        if (y, x) == (0, 3):
            break
        for move in find_moves(key, (y, x), path):
            queue.append(apply_move((y, x), path, move))
    else:
        raise Exception('Got stranded on {0!r} with path {1!r}'.format((y, x), path))
    return path

def find_longest_path(key):
    longest = ''
    queue = [(3, 0, '')]
    while queue:
        (y, x, path) = queue.pop(0)
        if (y, x) == (0, 3):
            if len(path) > len(longest):
                longest = path
            continue
        for move in find_moves(key, (y, x), path):
            queue.append(apply_move((y, x), path, move))
    return longest
