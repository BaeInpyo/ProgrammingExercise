import sys
import string
topo_dict = {}
state_dict = {}
result = []
def solution(curr_node):
    if state_dict.get(curr_node) == 'v':
        return
    elif state_dict.get(curr_node) == 'c':
        raise Exception()
    
    state_dict[curr_node] = 'c'
    for next_node in topo_dict[curr_node]:
        solution(next_node)
    state_dict[curr_node] = 'v'
    result.append(curr_node)


def get_order(prev_word, curr_word):
    for prev_c, curr_c in zip(prev_word, curr_word):
        if prev_c != curr_c:
            topo_dict[curr_c].add(prev_c)
            return

        
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        topo_dict = {a:set([]) for a in string.ascii_lowercase}
        state_dict = {}
        result = []
        N = int(sys.stdin.readline().rstrip())
        prev_word = sys.stdin.readline().rstrip()
        for _ in range(N-1):
            curr_word = sys.stdin.readline().rstrip()
            get_order(prev_word, curr_word)
            prev_word = curr_word

        for node in topo_dict.keys():
            try:
                solution(node)
            except:
                print('INVALID HYPOTHESIS')
                break
        else:
            print(''.join(result))

