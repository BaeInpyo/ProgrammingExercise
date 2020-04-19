# current codes can solve only test set1 and test set2

def solution(patterns):
    # remove duplicate patterns
    patterns = set(patterns)

    # remove consecutive *
    patterns = [p.split("*") for p in patterns]

    starts, mids, ends = [], [], []
    for pattern in patterns:
        starts.append(pattern[0])
        ends.append(pattern[-1])
        mids.extend([x for x in list(enumerate(pattern))[1:-1]])

    starts.sort(key=len)
    ends.sort(key=len)
    # print()
    # print("starts:", starts)
    # print("ends:", ends)

    curr = starts[0]
    for s in starts:
        if not s.startswith(curr):
            print("*")
            return

    curr = ends[0]
    for e in ends:
        if not e.endswith(curr):
            print("*")
            return

    mids.sort(key=lambda x: x[0])
    mids = [x[1] for x in mids]
    # print("mids:", mids)
    m = ""
    for x in mids:
        if x in m:
            continue
        else:
            m += x
    answer = starts[-1] + m + ends[-1]
    if answer == "":
        answer = "A"
    if len(answer) > 10**4:
        answer = "*"

    print(answer)
    

if __name__ == "__main__":
    T = int(input())
    for case_num in range(1, T+1):
        N = int(input())
        patterns = [None] * N
        for idx in range(N):
            patterns[idx] = input()

        print("Case #{}: ".format(case_num), end="")
        solution(patterns)
