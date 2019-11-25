import sys, os

# freopen equivalent
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.stdin = open(os.path.join(abs_path, 'input.txt'), 'r')

'''
- 각각의 힌트마다 힌트를 만족시킬 수 있는 자연수 합의 조합을 구함
    - ex) sum = 6, count = 2 => (1, 5), (2, 4)
- 각각의 힌트간의 관계를 구함
    - ex) 총 힌트가 20개라면 가능한 관계의 갯수는 190개
- 총 힌트의 갯수가 H개이고 각각의 힌트마다 자연수 조합을 Hi개씩 가지고 있다고 하면 총 경우의 수는 H1 * H2 ... Hh
- 힌트간의 관계가 있으므로 H1부터 Hh까지 순서대로 조합을 고르는데, Hi+1을 고를 때 H1~Hi까지를 둘러보면서 가능한 조합만 고른다.
- 정답이 반드시 1개가 존재하므로 가지치기는 하기 어렵다? 대신 바로위에 힌트간의 관계를 고려하여 다음 힌트를 고르는 것 자체가 decision tree의 입장에서 보면 가지치기라고 할 수 있다.
'''

if __name__ == '__main__':
    pass