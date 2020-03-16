import sys

seg_dict = {}

def solution(lo, hi, a, b):
    if lo == a and hi == b:
        return seg_dict[a][b]
    
    mid = lo + (hi-lo)//2
    if a > mid:
        return solution(mid+1, hi, a, b)
    elif b <= mid:
        return solution(lo, mid, a, b)
    else:
        left_min, left_max = solution(lo, mid, a, mid)
        right_min, right_max = solution(mid+1, hi, mid+1, b)
        return min(left_min, right_min), max(left_max, right_max)

def build_seg_dict(heights, lo, hi):
    if lo == hi:
        mx, mi = heights[lo], heights[lo]
        lo_dict = seg_dict.get(lo, {})
        seg_dict[lo] = lo_dict
        lo_dict[hi] = (mx, mi)
        return mx, mi

    mid = lo + (hi-lo)//2
    left_min, left_max = build_seg_dict(heights, lo, mid)
    right_min, right_max = build_seg_dict(heights, mid+1, hi)

    mx, mi = min(left_min, right_min), max(left_max, right_max)
    lo_dict = seg_dict.get(lo, {})
    seg_dict[lo] = lo_dict
    lo_dict[hi] = (mx, mi)
    return mx, mi

if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N, Q = [int(x) for x in sys.stdin.readline().rstrip().split()]
        heights = [int(x) for x in sys.stdin.readline().rstrip().split()]
        seg_dict = {}
        build_seg_dict(heights, 0, N-1)

        for _ in range(Q):
            a, b = [int(x) for x in sys.stdin.readline().rstrip().split()]
            mi, mx = solution(0, N-1, a, b)
            print(mx-mi)


