from itertools import combinations

def solution(orders, course):
    count = dict()

    # count occurence of each combinations of menu
    for order in orders:
        order = sorted(order)
        for num in course:
            for comb in combinations(order, num):
                count[comb] = count.get(comb, 0) + 1

    answer = dict()
    for (comb, freq) in count.items():
        if freq >= 2:
            if len(comb) in answer:
                answer[len(comb)].append(("".join(comb), freq))
            else:
                answer[len(comb)] = [("".join(comb), freq)]

    final_answer = []
    for length in answer:
        lst = sorted(answer[length], key=lambda x: x[1])
        print("length, lst: {} {}".format(length, lst))
        max_freq = lst[-1][1]
        for (comb, freq) in lst:
            if freq == max_freq:
                final_answer.append(comb)

    print(final_answer)
    final_answer = sorted(final_answer)
    return final_answer

solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
