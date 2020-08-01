class Solution:
    dp = None
    words = None
    def wordBreakInternal(self, s, i):
        if i >= len(s):
            return []
        
        if i in self.dp:
            return self.dp[i]
        
        result = []
        end = i+1
        while end < len(s):
            if s[i:end] in self.words:
                next_result = self.wordBreakInternal(s, end)
                for sentence in next_result:
                    result.append(s[i:end] + " " + sentence)
            end += 1
        
        if s[i:end] in self.words:
            result.append(s[i:end])
        
        self.dp[i] = result
        return result
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.dp = {}
        self.words = {}
        for word in wordDict:
            self.words[word] = True

        return self.wordBreakInternal(s, 0)
