import sys
envDict = {}

def solution(prevBlockNum, remainBlocks):
    result = 0

    if envDict.get((prevBlockNum, remainBlocks), False):
        return envDict[(prevBlockNum, remainBlocks)]

    if remainBlocks == 0:
        envDict[(prevBlockNum, remainBlocks)] = 1%10000000
        return 1%10000000

    # 이전 콜(층)에서 놓은 블럭수를 인자로 받아와서 현재 층 아래로 모양의 경우의 수에 이전 층 블럭수가 적절히 곱해져 나가도록. 
    for pickedBlockNum in range(1, remainBlocks+1):
        result += (prevBlockNum + pickedBlockNum-1)*solution(pickedBlockNum, remainBlocks-pickedBlockNum)

    envDict[(prevBlockNum, remainBlocks)] = result%10000000
    return result%10000000

if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline())
    for _ in range(C):
        N = int(sys.stdin.readline())
        # envDict은 케이스에 관계없이 캐쉬값이 같기때문에 매번 초기화할필요가 없다

        result = 0
        for i in range(1, N+1):
            result += solution(i, N-i)
        print(result%10000000)
