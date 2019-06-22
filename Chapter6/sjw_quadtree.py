import sys

def toStr(arr):
    '''
    convert from tree to str
    in original tree, the order is LeftUpper => RightUpper => LeftLower => RightLower
    in up down reversed, the order should be  LeftLower => RightLower => LeftUpper => RightUpper
    '''

    if len(arr) == 1:
        return arr[0]

    result = ''
    e0, e1, e2, e3, e4 = arr

    assert(e0 == 'x')
    result += e0
    result += toStr(e3)
    result += toStr(e4)
    result += toStr(e1)
    result += toStr(e2)

    return result

def toTree(arr):
    '''
    return array that represents tree
    '''

    if len(arr) <= 5:
        return arr

    for i in reversed(range(len(arr))):
        if arr[i] == 'x':
            e1 = arr.pop(i+1)
            e2 = arr.pop(i+1)
            e3 = arr.pop(i+1)
            e4 = arr.pop(i+1)
            arr[i] = ['x', e1, e2, e3, e4]

            return toTree(arr)


if __name__ == '__main__':
    # freopen equivalent
    sys.stdin = open('input.txt', 'r')

    C = int(sys.stdin.readline().strip())
    answers = []
    for _ in range(C):
        arr = [x for x in sys.stdin.readline().strip()]
        tree = toTree(arr)
        answer = toStr(tree)
        answers.append(answer)

    for a in answers:
        print(a)