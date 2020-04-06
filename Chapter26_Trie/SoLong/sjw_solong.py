import os
import sys
from collections import deque

# freopen equivalent
abs_dir = os.path.abspath(os.path.dirname(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")

class Trie:
    class TrieNode:
        def __init__(self, char):
            self.char = char
            self.end = False
            self.freq = 0
            self.children = {}

    def __init__(self):
        self.root = Trie.TrieNode("*")

    def print(self):
        stack = []
        stack.append((self.root, 0))    # (node, depth)
        while stack:
            node, depth = stack.pop()
            print("{}{},{},{}".format("-"*depth, node.char, node.freq, node.end))
            # print("-"*depth + node.char + ":" + node.end)
            for k, v in node.children.items():
                stack.append((v, depth+1))

    def insert(self, string, freq):
        curr = self.root
        for char in string:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = Trie.TrieNode(char)
                curr = curr.children[char]

        curr.end = True
        curr.freq = freq

    def search(self, string):
        curr = self.root
        for char in string:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False

        return curr.end

    def tab(self, string):
        """ return recommended word with given string as prefix """
        # similart with search
        curr = self.root
        for char in string:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return None

        candidates = []
        if curr.end is True:
            candidates.append((string, curr.freq))

        queue = deque()
        for (k, v) in curr.children.items():
            queue.append((v, ""))
        while queue:
            node, acc = queue.pop()
            if node.end is True:
                candidates.append((string + acc + node.char, node.freq))
            else:
                for k, v in node.children.items():
                    queue.append((v, acc + node.char))

        # sort by freq DESC string ASC
        candidates.sort(key=lambda x: (-x[1], x[0]))
        return candidates[0][0]


def solution(words, sentence):
    trie = Trie()

    # build trie
    for (word, freq) in words:
        trie.insert(word, freq)

    # trie.print()
    answer = sentence.count(" ")
    for word in sentence.split():
        # word does not exist inside trie
        if trie.search(word) is False:
            answer += len(word)

        else:
            for end in range(1, len(word)):
                curr = word[:end]
                # print("tab word: {}, result: {}".format(curr, trie.tab(curr)))
                if trie.tab(curr) == word:
                    # print("add: {} -> {}".format(curr, trie.tab(curr)))
                    answer += (end + 1) # we can type tab
                    break
            else:
                # if we reach end of word, we don't need to type tab
                answer += len(word)

    sys.stdout.write(str(answer) + "\n")
    # print("answer:", answer)


if __name__ == "__main__":
    C = int(sys.stdin.readline())
    for _ in range(C):
        N, M = [int(x) for x in sys.stdin.readline().split()]
        words = [None] * N
        for idx in range(N):
            word, freq = sys.stdin.readline().split()
            freq = int(freq)
            words[idx] = (word, freq)

        sentence = sys.stdin.readline()
        solution(words, sentence)