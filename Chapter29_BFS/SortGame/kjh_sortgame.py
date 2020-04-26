from collections import deque
# here = tuple(range(8))
here = "01234567"
dist_ = {here: 0}
q = deque([here])

while q:
    here = q.popleft()
    for i in range(7):
        for j in range(i+2, 9):
            there = here[:i] + here[i:j][::-1] + here[j:]
            if there not in dist_:
                dist_[there] = dist_[here] + 1
                q.append(there)

for _ in range(int(input())):
    n = int(input())
    seq = list(map(int, input().split()))
    sseq = sorted(seq)
    seq = [sseq.index(s) for s in seq]
    seq.extend(range(len(seq),8))

    # print(dist_[tuple(seq)])
    print(dist_["".join(map(str,seq))])
