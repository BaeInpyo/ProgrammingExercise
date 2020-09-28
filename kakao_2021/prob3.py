from itertools import combinations
import bisect

def solution(info, query):
    table = dict()
    
    for line in info:
        language, position, career, food, score = line.split()
        score = int(score)
        for idx in range(5):
            for comb in combinations(range(4), idx):
                key = [language, position, career, food]
                for jdx in comb:
                    key[jdx] = "-"
                    
                key = tuple(key)
                if key in table:
                    bisect.insort(table[key], score)
                else:
                    table[key] = [score]

    answer = []
    for q in query:
        q = q.split()
        score = int(q[7])
        key = (q[0], q[2], q[4], q[6])
        if key in table:
            count = len(table[key]) - bisect.bisect_left(table[key], score)
            print("key, count, score, lst: {}, {}, {}, {}".format(key, count, score, table[key]))
            answer.append(count)
        else:
            answer.append(0)

    print(answer)
    return answer

                    
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])
