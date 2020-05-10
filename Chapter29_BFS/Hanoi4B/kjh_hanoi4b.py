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

def search(state, end):
    queue = deque([state])
    moves = {state: 0}
    na = 0
    while queue:
        _state = queue.popleft()
        na = set()
        for i in range(12):
            if not _state // 4**i: break
            tower = (_state // 4**i) % 4
            if tower not in na:
                na.add(tower)
                for next_ in {0, 1, 2, 3} - na:
                    new_state = _state + (next_-tower)*4**i
                    if new_state not in moves:
                        queue.append(new_state)
                        moves[new_state] = moves[_state] + 1
                if len(na) > 3:
                    break
    print(moves[end])

for _ in range(int(input())):
    n = int(input())
    begin = state([[int(i) for i in input().split()[1:]] for _ in range(4)])
    end = state([[int(i) for i in input().split()[1:]] for _ in range(4)])
    search(begin, end)
