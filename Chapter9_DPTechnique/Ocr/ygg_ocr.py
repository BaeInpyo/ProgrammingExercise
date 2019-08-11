import sys
wordToIdx = {}
idxToWord = {-1: 'BOS'} # BOS : Beginning of sentence
firstAppProb = [[]]
JAfterIProb = [[]]
recogIAsJProb = [[]]
result = {}
M = 0
envDict = {}

def solution(sentence, prevWord, currIdx):

    if currIdx >= len(sentence):
        return 1

    if envDict.get((prevWord, currIdx), -1) != -1:
        return envDict[(prevWord, currIdx)]

    currIdxWord = sentence[currIdx]
    maxProb = 0.0

    # 모든 단어셋을 돌며 확률가지를 만들어나가고, max값을 구함
    for word in range(M):
        if currIdx == 0:
            currWordProb = firstAppProb[word]*recogIAsJProb[word][currIdxWord]
        else:
            currWordProb = JAfterIProb[prevWord][word]*recogIAsJProb[word][currIdxWord]
        
        # ************ 시간단축을 위해 현재 확률이 0이면 더 깊이 들어가지 않음 ***********
        # 내경우에 이부분을 추가하고 나서 시간초과가 
        if currWordProb == 0.0:
            continue
        totalProb = currWordProb * solution(sentence, word, currIdx+1)

        if totalProb > maxProb:
            maxProb = totalProb
            # 이전 단어가 prevWord 일때, max 확률을 만들어낼때의 currIdx의 단어를 기억함.(출력용)
            result[(prevWord, currIdx)] = word
    
    # DP를 위해 해당환경의 확률을 기억        
    envDict[(prevWord, currIdx)] = maxProb
    return maxProb

if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    M, Q = list(map(int,sys.stdin.readline().rstrip().split()))
    for idx, word in enumerate(sys.stdin.readline().rstrip().split()):
        wordToIdx[word] = idx
        idxToWord[idx] = word
    firstAppProb = list(map(float,sys.stdin.readline().rstrip().split()))
    JAfterIProb = [list(map(float,sys.stdin.readline().rstrip().split())) for _ in range(M)]
    recogIAsJProb = [list(map(float,sys.stdin.readline().rstrip().split())) for _ in range(M)]

    for _ in range(Q):
        result = {}
        envDict = {}
        sentence = list(map(lambda x: wordToIdx[x],sys.stdin.readline().rstrip().split()[1:]))
        resultString = ''
        prevWord = -1
        solution(sentence, -1, 0)
        for currIdx in range(len(sentence)):
            resultString += idxToWord[result[(prevWord, currIdx)]]+' '
            prevWord = result[(prevWord, currIdx)]
        print(resultString.rstrip())
