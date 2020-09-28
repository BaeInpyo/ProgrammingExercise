from collections import Counter
import sys

class Node:
    def __init__(self, start, end, counter, left=None, right=None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right
        self.counter = counter

def merge(left, right):
    """ merge 2 noeds. """
    new_counter = left.counter.copy()
    new_counter.update(right.counter)
    return Node(left.start, right.end, new_counter, left, right)

def read_input():
    N, k = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    ranges = []
    for _ in range(k):
        ranges.append([int(x) for x in input().split()])
        
    return N, k, ranges, nums

def init(start, end, nums):
    """ Return root of segtree in range [start, end] """
    if start == end:
        #print("return:", start, end)
        return Node(start, end, Counter(nums[start:end+1]))
    else:
        mid = (start+end) // 2
        left = init(start, mid, nums)
        right = init(mid+1, end, nums)
        #print("return:", start, end, mid)
        return merge(left, right)
    
def search(root, start, end):
    """ Return answer in range [start, end] """
    counter = Counter()
    if not root or end < root.start or start > root.end:
        return counter
    #print("search:", start, end, root.start, root.end)
    if start <= root.start and root.end <= end:
        return root.counter

    counter.update(search(root.left, start, end))
    counter.update(search(root.right, start, end))
    return counter

def print_tree(root, indent):
    if not root:
        return
    string = "\t" * indent
    string += "(start: {}, end: {}, counter: {})".format(root.start, root.end, root.counter)
    print(string)
    print_tree(root.left, indent+1)
    print_tree(root.right, indent+1)

def solution(N, k, ranges, nums):
    root = init(0, N-1, nums)
    print_tree(root, 0)
    for (start, end) in ranges:
        counter = search(root, start-1, end-1)
        answer = 0
        print("start, end, counter:", start-1, end-1, counter)
        for (num, count) in counter.items():
            answer += (num * count * (count+1) // 2)
            
        print(answer)

if __name__ == "__main__":
    sys.setrecursionlimit(300000)
    N, k, ranges, nums = read_input()
    solution(N, k, ranges, nums)