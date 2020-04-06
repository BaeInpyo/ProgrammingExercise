def solution(case_num, n, activities):
    # fill dummy job at first
    cameron = [(0, 0)]
    jamie = [(0, 0)]

    # (start, end, idx)
    activities = [(*item, idx) for (idx, item) in enumerate(activities)]
    activities.sort(key=lambda x: (x[0]))
    answers = []

    # print("activities:", activities)
    for act in activities:
        cameron_end = cameron[-1][1]
        jamie_end = jamie[-1][1]
        curr_start = act[0]
        act_idx = act[2]
        # print("cameron:", cameron)
        # print("jamie:", jamie)
        # print("curr_act:", act)

        if curr_start >= cameron_end:
            cameron.append(act)
            answers.append((act_idx, "C"))
        elif curr_start >= jamie_end:
            jamie.append(act)
            answers.append((act_idx, "J"))
        else:
            print("Case #{}: IMPOSSIBLE".format(case_num))
            return

    answers.sort(key=lambda x: x[0])    # sort by idx
    answer = "".join([item[1] for item in answers])
    print("Case #{}: {}".format(case_num, answer))


if __name__ == "__main__":
    T = int(input())
    for case_num in range(1, T+1):
        N = int(input())
        activities = [0] * N
        for idx in range(N):
            start, end = [int(x) for x in input().split()]
            activities[idx] = (start, end)

        solution(case_num, N, activities)