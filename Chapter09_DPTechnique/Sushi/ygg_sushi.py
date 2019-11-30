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

def cleanSushi(sushis):
    def check(x):
        for sushi in sushis:
            if x == sushi:
                continue
            if x[0] >= sushi[0] and x[1] <= sushi[1]:
                return False
            if x[0] >= sushi[0] and x[0]%sushi[0] == 0 and x[1] <= sushi[1]*(x[0]//sushi[0]):
                return False
        return True
    sushis = list(filter(check, sushis))
    return sushis

def solution(budget, sushis):

    # 전처리 그리디
    currBudget = budget
    sushiIdx = 0
    currPriority = 0

    if budget > 5000000:
        price, priority = sushis[sushiIdx]
        budgetForGreedy = budget-5000000
        currBudget -= price*(budgetForGreedy//price)
        currPriority += priority*(budgetForGreedy//price)

    cache = {0: currPriority}

    sushis.sort(key=lambda x:x[0])
    sushis = cleanSushi(sushis)
    sushis = list(map(lambda x: (x[0]//100, x[1]),sushis))


    for budget in range(1,(currBudget//100)+1):
        maximum = cache[budget-1]
        for price, priority in sushis:
            if budget-price < 0:
                continue
            maximum = max(cache[budget-price] + priority, maximum)
        cache[budget] = maximum

    return cache[currBudget//100]


if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
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
