import sys

minCount = 0

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

def getTMinCount(friends, foods, chosen):
    count = 0
    numFriends = len(friends)
    numChosen = len(chosen)
    leftFriends = numFriends - numChosen
    for food in foods:
        if leftFriends <= 0:
            break
        leftFriends -= len(food)
        count += 1
    return count


def solution(friends, foods, chosen, currCount):
    global minCount

    if len(chosen) == len(friends):
        minCount = min(currCount, minCount)
        return

    if getTMinCount(friends, foods, chosen) + currCount >= minCount:
        return

    for foodIdx in range(len(foods)):
        food = foods.pop(foodIdx)
        nextChosen = chosen | set(food)
        solution(friends, foods, nextChosen, currCount+1)
        foods.insert(foodIdx, food)

    return
    

if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        n, m = list(map(int,sys.stdin.readline().rstrip().split()))
        friends = sys.stdin.readline().rstrip().split()
        foods = []
        for _ in range(m):
            foods.append(sys.stdin.readline().rstrip().split()[1:])

        minCount = 999
        # pre-processing
        newFoods = []
        for idx in range(len(foods)):
            food = foods.pop(idx)
            if len(list(filter(lambda x: len(set(food)-set(x)) == 0, foods))) == 0:
                newFoods.append(food)
            foods.insert(idx, food)
        newFoods.sort(key=lambda x: len(x), reverse=True)

        solution(friends, newFoods, set([]), 0)
        print(minCount)
