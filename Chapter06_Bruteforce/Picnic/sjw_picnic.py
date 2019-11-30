import sys

def pick(pairList, numStudent, currStudentList):
    if len(currStudentList) == numStudent:
        return 1
    if not pairList:
        return 0

    result = 0
    for i in range(len(pairList)):
        a, b = pairList[i]
        if a not in currStudentList and b not in currStudentList:
            # print('l1:', a, b, currStudentList)
            result += pick(pairList[i+1:], numStudent, currStudentList[:] + [a, b])

    return result


if __name__ == '__main__':
    C = int(sys.stdin.readline().strip())
    for _ in range(C):
        n, m = [int(x) for x in sys.stdin.readline().strip().split()]
        line = [int(x) for x in sys.stdin.readline().strip().split()]
        pairList = []
        for i in range(m):
            pairList.append((line[2*i], line[2*i+1]))

        answer = pick(pairList, n, [])
        sys.stdout.write('{}\n'.format(answer))