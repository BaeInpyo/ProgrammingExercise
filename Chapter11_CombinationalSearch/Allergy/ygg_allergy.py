import sys

minCount = 0

def solution(friendsDict, hungryFriends, foods, currCount):
    global minCount

    if currCount >= minCount:
        return

    if len(hungryFriends) == 0:
        minCount = currCount
        return

    hungryFriend = hungryFriends.pop()

    for foodIdx in friendsDict[hungryFriend]:
        food = foods[foodIdx]
        newHungryFriends = hungryFriends - set(food)
        solution(friendsDict, newHungryFriends, foods, currCount+1)
    return
    

if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        n, m = list(map(int,sys.stdin.readline().rstrip().split()))
        _ = sys.stdin.readline()
        foods = []
        for _ in range(m):
            foods.append(sys.stdin.readline().rstrip().split()[1:])

        minCount = 999

        newFoods = []
        for idx in range(len(foods)):
            food = foods.pop(idx)
            if len(list(filter(lambda x: len(set(food)-set(x)) == 0, foods))) == 0:
                newFoods.append(food)
            foods.insert(idx, food)
        newFoods.sort(key=lambda x: len(x), reverse=True)

        friendsDict = {}
        for idx, food in enumerate(newFoods):
            for person in food:
                friendsDict[person] = friendsDict.get(person, []) + [idx]

        #print(friendsDict.keys())
        solution(friendsDict, set(friendsDict.keys()), newFoods, 0)
        print(minCount)
