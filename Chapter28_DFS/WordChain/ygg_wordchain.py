import sys

graph_dict = {}
result = []
state_dict = {}
def solution(curr_node):
    words = graph_dict.get(curr_node, {'words':[]})['words']

    while len(words) > 0:
        word = words.pop()
        solution(word[-1])
        result.append(word)

    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N = int(sys.stdin.readline().rstrip())
        graph_dict = {}
        result = []
        state_dict = {}
        for _ in range(N):
            word = sys.stdin.readline().rstrip()
            start_node = graph_dict.get(word[0], {'in':0, 'out':0, 'words':[]})
            start_node['words'].append(word)
            start_node['out'] += 1
            graph_dict[word[0]] = start_node

            end_node = graph_dict.get(word[-1], {'in':0, 'out':0, 'words':[]})
            end_node['in'] += 1
            graph_dict[word[-1]] = end_node

        start_node = ''
        end_node = ''
        for char, node in graph_dict.items():
            if node['in'] - node['out'] == 1:
                if end_node != '':
                    print("IMPOSSIBLE")
                    break
                end_node = char
            elif node['in'] - node['out'] == -1:
                if start_node != '':
                    print("IMPOSSIBLE")
                    break
                start_node = char
            elif node['in'] - node['out'] != 0:
                print("IMPOSSIBLE")
                break

        else:
            if start_node != '':
                if end_node == '':
                    print("IMPOSSIBLE")
                    continue
                solution(start_node)
                if len(result) != N:
                    print("IMPOSSIBLE")
                    continue
                result.reverse()
                print(' '.join(result))
            else:
                if end_node != '':
                    print("IMPOSSIBLE")
                    continue
                start_node = next(iter(graph_dict.keys()))
                solution(start_node)
                if len(result) != N:
                    print("IMPOSSIBLE")
                    continue
                result.reverse()
                print(' '.join(result))
                
