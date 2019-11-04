import sys
import math

PI = math.pi

def pointToTheta(y,x):
    if x == 0:
        return (PI/2 + 2*PI if y>0 else PI*3/2 + 2*PI)
    elif y == 0:
        return (2*PI if x>0 else 3*PI)
    
    if x >= 0 and y >= 0:
        return math.atan(y/x) + 2*PI # 2파이 더해주는 이유는 음수범위 없애려고 0 ~ 4pi 범위계로
    elif x <= 0 and y >= 0:
        return PI - math.atan(abs(y/x)) + 2*PI # 2파이 더해주는 이유는 음수범위 없애려고 0 ~ 4pi 범위계로
    elif x <= 0 and y <= 0:
        return math.atan(y/x) + PI + 2*PI # 2파이 더해주는 이유는 음수범위 없애려고 0 ~ 4pi 범위계로
    else:
        return PI - math.atan(abs(y/x)) + PI + 2*PI # 2파이 더해주는 이유는 음수범위 없애려고 0 ~ 4pi 범위계로

def getRange(center, radius):
    theta = 2*math.asin(radius/16)
    return [center-theta, center+theta]

def solution(currFrom, currTo, chosos):
    if currTo - currFrom >= 2*PI:
        return 1

    maxRange = 0
    maxIdx = -1
    result = 0

    for idx, elt in enumerate(chosos):
        chosoPoint, radius = elt
        chosoFrom, chosoTo = chosoPoint
        if currTo >= chosoFrom:
            if maxRange < chosoTo - currTo:
                result = 1
                maxRange = chosoTo - currTo
                maxIdx = idx
        if currFrom <= chosoTo:
            if maxRange < currFrom - chosoFrom:
                result = -1
                maxRange = currFrom - chosoFrom
                maxIdx = idx
    if result != 0:
        if result == -1:
            nextTo = currTo
            nextFrom = currFrom - maxRange
        else:
            nextTo = currTo + maxRange
            nextFrom = currFrom
        del chosos[maxIdx]
        return 1+solution(nextFrom, nextTo, chosos)
    else:
        return -9999  

    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        n = int(sys.stdin.readline().rstrip())
        chosos = []
        for _ in range(n):
            chosos.append(list(map(lambda x: float(x), sys.stdin.readline().rstrip().split())))
        chosos = list(map(lambda x: [getRange(pointToTheta(x[0],x[1]),x[2]),x[2]], chosos)) # chosos = [[from, to], radius]
        maxVal = -1
        maxIdx = -1
        for idx, elt in enumerate(chosos):
            if elt[1] > maxVal:
                maxVal = elt[1]
                maxIdx = idx
        firstPoint = chosos.pop(maxIdx)
        result = solution(firstPoint[0][0], firstPoint[0][1], chosos)
        if result < 0:
            result = 'IMPOSSIBLE'
        print(result)


