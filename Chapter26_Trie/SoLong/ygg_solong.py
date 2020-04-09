import sys
from string import ascii_uppercase

def solution(trie_dict, sentence_str):
    result = 0
    sentence = sentence_str.split()
    for word in sentence:
        prev_node = trie_dict
        typing_cnt = 0

        for c in word:
            typing_cnt += 1
            curr_node = prev_node.get(c)
            if not curr_node: # 트라이에 인풋 단어가 존재하지 않으면
                result += len(word)
                break
            else:
                if curr_node['is_first_word'].get(word):
                    result += min(len(word),typing_cnt + 1)# 지금까지 타이핑한 횟수 + 탭
                    break
                prev_node = curr_node['children']

        else:
            result += len(word) # for문 break 없이 종료

    space_cnt = 0
    for c in sentence_str:
        if(c.isspace()):
            space_cnt += 1
    return result + space_cnt # 스페이스바 누르는 횟수 더해줌
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]
        trie_dict = {a:{'children': {}, 'first_char': 'ZZ', 'first_cnt': -1, 'first_word': '_', 'is_first_word': {}} for a in ascii_uppercase} # roots
        for _ in range(N):
            word, cnt = sys.stdin.readline().rstrip().split()
            cnt = int(cnt)

            prev_node = trie_dict
            for c in word:
                curr_node = prev_node.get(c)
                if not curr_node:
                    curr_node = {'children': {}, 'first_char': 'ZZ', 'first_cnt': -1, 'first_word': '_', 'is_first_word': {}}
                    prev_node[c] = curr_node

                if curr_node['first_cnt'] < cnt or \
                (curr_node['first_cnt'] == cnt and curr_node['first_char'] > c) or \
                (curr_node['first_cnt'] == cnt and curr_node['first_char'] == c and curr_node['first_word'] > word):
                    curr_node['first_cnt'] = cnt
                    curr_node['first_char'] = c
                    curr_node['first_word'] = word
                    curr_node['is_first_word'] = {word: True}
                
                prev_node = curr_node['children']

        print(solution(trie_dict, sys.stdin.readline().rstrip()))


