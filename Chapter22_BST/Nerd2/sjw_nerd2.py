import sys
import os
import bisect


abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")

"""
We will keep list of (p, q) in sorted order.
When new person is added, we will remove victims if exist
"""

# def solution(people):
#     remains = []    # list of remaining people
#     answer = 0
#     for person in people:
#         # since there is no duplicate p or q, we can use both
#         # bisect_left() and bisect_right()
#         index = bisect.bisect(remains, person)

#         # person can be added only if there exists (p', q') such that
#         # p' > p or q' > q
#         _p, _q = person
#         if index == len(remains) or _q > remains[index][1]:
#             remains.insert(index, person)
#             index -= 1

#             while index >= 0:
#                 if remains[index][1] < _q:
#                     remains.pop(index)
#                 else:
#                     break
#                 index -= 1

#         answer += len(remains)

#     sys.stdout.write("%d\n" % (answer))
#     return

def solution(people):
    # keep p and q in seperate list
    # ps contains list of p
    # qs contains list of -q to remain ASC order
    ps, qs = [], []
    len_list = 0
    answer = 0

    for person in people:
        p, q = person
        pindex = bisect.bisect(ps, p)

        if pindex == len_list or q > qs[pindex]:
            qindex = bisect.bisect(qs, -q, lo=0, hi=pindex)
            # ps = ps[:qindex] + [p] + ps[pindex:]
            # qs = qs[:qindex] + [-q] + qs[pindex:]
            # len_list = len(ps)

            ps[qindex:pindex] = [p]
            qs[qindex:pindex] = [-q]
            len_list = len(ps)

        answer += len_list

    print(answer)


if __name__ == "__main__":
    C = int(sys.stdin.readline())
    for _ in range(C):
        N = int(sys.stdin.readline())
        people = [0] * N
        for idx in range(N):
            p, q = [int(x) for x in sys.stdin.readline().split()]
            people[idx] = (p, q)

        solution(people)


