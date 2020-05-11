from collections import deque

def state(towers):
    """Map towers to 4**12 integer

    Examples
    --------
    >>> state([[1], [3], [5, 4], [2]])
    668
    = 0 * 4**0 + 2 * 4**1 + 1 * 4**2 + 2 * 4**3 + 2 * 4**4
    """
    ret = 0
    for i, row in enumerate(towers):
        for val in row:
            ret += i * 4**(val-1)
    return ret

def print_state(state): # for debugging
    i = 1
    towers = [[] for _ in range(4)]
    while state:
        towers[state % 4].append(i)
        state //= 4
        i += 1
    print(towers)

def search(begin, end):
    queue_begin, queue_end = deque([begin]), deque([end])
    moves_begin, moves_end = {begin: 0}, {end: 0}

    while queue_begin or queue_end:
        _state = queue_begin.popleft()
        na = set()
        for i in range(12):
            if not _state // 4**i: break
            tower = (_state // 4**i) % 4
            if tower not in na:
                na.add(tower)
                for next_ in {0, 1, 2, 3} - na:
                    new_state = _state + (next_-tower)*4**i
                    if new_state not in moves_begin:
                        queue_begin.append(new_state)
                        moves_begin[new_state] = moves_begin[_state] + 1
                        if new_state in moves_end:
                            return moves_end[new_state] + moves_begin[new_state]
                if len(na) > 3:
                    break

        _state = queue_end.popleft()
        na = set()
        for i in range(12):
            if not _state // 4**i: break
            tower = (_state // 4**i) % 4
            if tower not in na:
                na.add(tower)
                for next_ in {0, 1, 2, 3} - na:
                    new_state = _state + (next_-tower)*4**i
                    if new_state not in moves_end:
                        queue_end.append(new_state)
                        moves_end[new_state] = moves_end[_state] + 1
                        if new_state in moves_begin:
                            return moves_end[new_state] + moves_begin[new_state]
                if len(na) > 3:
                    break


for _ in range(int(input())):
    n = int(input())
    begin = state([[int(i) for i in input().split()[1:]] for _ in range(4)])
    end = state([[int(i) for i in input().split()[1:]] for _ in range(4)])
    search(begin, end)
