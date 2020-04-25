import sys
import collections
distance_dict = {}

def get_distance():
    root_seq = [i+1 for i in range(8)]
    distance_dict[tuple(root_seq)] = 0
    # 모든 경우에대해 다 뒤집어봄, 가장 distance가 낮은거부터 차례대로 확인 (재귀콜을 iterative 하게 수행, 맥스 재귀 깊이 에러떠서)
    call_stack = collections.deque([(root_seq, 1)])
    while call_stack:
        curr_seq, distance = call_stack.popleft()

        # 가장 넓은 범위의 뒤집기부터 모든 경우 확인
        for length in range(7, 0, -1):
            for fr in range(0, 8-length):
                to = fr + length
                rev_seq = curr_seq[:fr] + curr_seq[fr:to+1][::-1] + curr_seq[to+1:]
                rev_seq_key = tuple(rev_seq)

                if distance_dict.get(rev_seq_key) != None: # 이미 확인한 수열이면 패스
                    continue

                distance_dict[rev_seq_key] = distance
                call_stack.append((rev_seq, distance+1))
        
    return

def seq_1_to_8(sequence):
    sorted_seq = sorted(sequence)
    value_to_idx_dict = {value:i+1 for i, value in enumerate(sorted_seq)}
    return [value_to_idx_dict[value] for value in sequence] + [i+1 for i in range(len(sequence), 8)]

if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    get_distance()
    for _ in range(C):
        N = int(sys.stdin.readline().rstrip())
        sequence = seq_1_to_8([int(x) for x in sys.stdin.readline().rstrip().split()])
        print(distance_dict[tuple(sequence)])


