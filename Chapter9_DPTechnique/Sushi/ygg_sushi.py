"""
recursive solution

import sys
envDict = {}

def solution(budget, sushis):
    if envDict.get(budget, -1) != -1:
        return envDict[budget]
    maxPriority = 0
    for price, priority in sushis:
        if price <= budget:
            result = priority + solution(budget-price, sushis)
            maxPriority = max(maxPriority, result)

    envDict[budget] = maxPriority
    return maxPriority

if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        n, m = list(map(int,sys.stdin.readline().rstrip().split()))
        sushis = []
        envDict = {}
        for _ in range(n):
            price, priority = list(map(int,sys.stdin.readline().rstrip().split()))
            sushis.append((price, priority))
        print(solution(m, sushis))
"""

"""
iterative solution

import sys
def solution(budget, sushis):
    cache = {budget: 0}
    unvisitQueue = [budget]

    for budget in unvisitQueue:
        currPriority = cache[budget]
        for price, priority in sushis:
            if budget-price < 0:
                continue
            if cache.get(budget-price, -1) < currPriority + priority:
                cache[budget-price] = currPriority + priority
                unvisitQueue.append(budget-price)
    return max(cache.values())


if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        n, m = list(map(int,sys.stdin.readline().rstrip().split()))
        sushis = []
        for _ in range(n):
            price, priority = list(map(int,sys.stdin.readline().rstrip().split()))
            sushis.append((price, priority))
        sushis.sort(key=lambda x:x[0])
        print(solution(m, sushis))
"""
import sys
def solution(budget, sushis):

    # 전처리 그리디
    currBudget = budget
    sushiIdx = 0
    currPriority = 0

    if budget > 10000000:
        while sushiIdx < len(sushis) and currBudget > int(0.05 * budget):
            price, priority = sushis[sushiIdx]
            if currBudget - 100*price < 0:
                sushiIdx += 1
                continue
            else:
                currBudget -= 100*price
                currPriority += 100*priority

    cache = {currBudget: currPriority}
    unvisitQueue = [currBudget]
    
    sushis.sort(key=lambda x:x[0])

    for budget in unvisitQueue:
        currPriority = cache[budget]
        for price, priority in sushis:
            if budget-price < 0:
                continue
            if cache.get(budget-price, -1) < currPriority + priority:
                cache[budget-price] = currPriority + priority
                unvisitQueue.append(budget-price)

    return max(cache.values())


if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        n, m = list(map(int,sys.stdin.readline().rstrip().split()))
        sushis = []
        for _ in range(n):
            price, priority = list(map(int,sys.stdin.readline().rstrip().split()))
            sushis.append((price, priority))
        sushis.sort(key=lambda x:x[0])
        sushis.sort(key=lambda x:x[1]/x[0], reverse=True)
        print(solution(m, sushis))
