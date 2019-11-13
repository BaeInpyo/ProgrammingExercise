import sys

def findMaxFood(foods, chosen):
    retIdx = []
    maxVal = 0
    for idx, food in enumerate(foods):
        diffFoodLen = len(set(food)-chosen)
        if maxVal < diffFoodLen:
            maxVal = diffFoodLen
            retIdx = [idx]
        elif maxVal == diffFoodLen and maxVal != 0:
            retIdx.append(idx)
    return retIdx


def solution(friends, foods, chosen):
    if len(chosen) == len(friends):
        return 0
    result = 999
    maxFoods = findMaxFood(foods, chosen)
    for maxFoodIdx in maxFoods:
        maxFood = foods.pop(maxFoodIdx)
        nextChosen = chosen | set(maxFood)
        result = min(result, 1+solution(friends, foods, nextChosen))
        foods.insert(maxFoodIdx, maxFood)
    return result
    
if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        n, m = list(map(int,sys.stdin.readline().rstrip().split()))
        friends = sys.stdin.readline().rstrip().split()
        foods = []
        for _ in range(m):
            foods.append(sys.stdin.readline().rstrip().split()[1:])
        print(solution(friends, foods, set([])))

