import sys
def eltWiseSubtraction(l1, l2):
    return [e1-e2 for e1, e2 in zip(l1, l2)]

def solution(rList, pList, currPList):
    rpList = zip(rList, currPList)
    maxProp = 0
    prevProp = currPList[0]/rList[0]
    isDone = True
    for r, p in rpList:
        prop = p/r
        if prevProp != prop:
            isDone = False
        maxProp = max(maxProp, prop)

    if maxProp < 1:
        return eltWiseSubtraction(rList, pList)
    
    if isDone:
        return eltWiseSubtraction(currPList, pList)

    newPList = [int(round(r*maxProp)) for r in rList]
    return solution(rList, pList, newPList)

    
    
if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        n = int(sys.stdin.readline().rstrip())
        rList = [int(x) for x in sys.stdin.readline().rstrip().split()]
        pList = [int(x) for x in sys.stdin.readline().rstrip().split()]

        print(' '.join([str(elt) for elt in solution(rList, pList, pList)]))


