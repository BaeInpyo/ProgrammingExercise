def solution(cook_times, order, k):
    dic = dict()    # key: 단계, value: 필요한 이전단계

    # init dict
    for i in range(1, len(cook_times)+1):
        dic[i] = set()

    # fill dict
    for o in order:
        src, dst = o
        dic[src].add(dst)

    tree = [set(range(1, k+1))]
    for _ in range(k):
        curr = tree[-1]
        new_curr = set(curr)
        nexts = set()
        for src in curr:
            dst = dic[src]
            for d in dst:
                if d in new_curr:
                    new_curr.remove(d)
                    nexts.add(d)

        tree[-1] = new_curr
        if nexts:
            tree.append(nexts)

    pre = []
    for level in reversed(range(len(tree))):
        curr = tree[level]
        if k in curr:
            break

    if level == 0:
        return [0, cook_times[k-1]]








if __name__ == '__main__':
    # cook_times = [5, 30, 15, 30, 35, 20, 4]
    # order = [[2,4],[2,5],[3,4],[3,5],[1,6],[4,6],[5,6],[6,7]]
    # k = 6
    #
    # solution(cook_times, order, k)

    cook_times = [5, 30, 15, 30, 35, 20, 4, 50, 40]
    order = [[2,4],[2,5],[3,4],[3,5],[1,6],[4,6],[5,6],[6,7],[8,9]]
    k = 9

    solution(cook_times, order, k)