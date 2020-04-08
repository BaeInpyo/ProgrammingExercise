class Trie:
    def __init__(self):
        self.top_freq = 0
        self.top_word = None
        # self.end = False
        self.children = {}
    
    def insert(self, word, freq):
        if (-freq, word) < (-self.top_freq, self.top_word):
            self.top_word, self.top_freq = word, freq
        if not word:
            # self.end = True
            return
        if word[0] not in self.children:
            self.children[word[0]] = Trie()
        self.children[word[0]].insert(word[1:], freq)
    
    def find(self, word):
        if not word: return 0
        if word == self.top_word: return 1
        if word[0] not in self.children: return len(word)
        return 1 + self.children[word[0]].find(word[1:])


for _ in range(int(input())):
    n, m = map(int, input().split())
    root = Trie()
    for _ in range(n):
        word, freq = input().split()
        freq = int(freq)
        root.insert(word, freq)
    root.top_word = None

    print(sum([root.find(word) for word in input().split()]) + m-1)
