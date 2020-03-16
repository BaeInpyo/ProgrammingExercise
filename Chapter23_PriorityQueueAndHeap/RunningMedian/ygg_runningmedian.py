import sys

def input_generator(N, a, b):
    prev = 1983
    yield prev
    for _ in range(1, N):
        nxt = (prev*a + b) % 20090711
        yield nxt
        prev = nxt

class Node():
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.left_len, self.right_len = 0, 0
    
    def insert(self, val):
        if self.val < val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Node(val)
            self.right_len += 1

        else:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val)
            self.left_len += 1

    def find_nth_elt(self, n): # 0 based indexing
        if n == self.left_len:
            return self.val
        elif n > self.left_len:
            return self.right.find_nth_elt(n-self.left_len-1)
        else:
            return self.left.find_nth_elt(n)

class BBST():
    def __init__(self):
        self.root = None
        self.len = 0

    def insert(self, val):
        self.len += 1
        if not self.root:
            self.root = Node(val)
        else:
            self.root.insert(val)

    def find_median(self):
        if not self.root:
            return -1
        else:
            return self.root.find_nth_elt((self.len-1)//2)

def solution(A):
    bbst = BBST()
    result = 0
    for A_i in A:
        bbst.insert(A_i)
        result += bbst.find_median()

    return result % 20090711
    
if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N, a, b = [int(x) for x in sys.stdin.readline().rstrip().split()]
        A = input_generator(N, a, b)
        print(solution(A))


