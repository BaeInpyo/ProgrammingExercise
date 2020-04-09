import os
import sys
from collections import deque

# freopen equivalent
abs_dir = os.path.abspath(os.path.dirname(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


class Trie:
    class TrieNode:
        def __init__(self, char, word):
            self.char = char
            self.tab = word
            self.children = {}

    def __init__(self):
        self.root = self.TrieNode("*", "")

    def insert(self, word):
        """
        - insert word to trie
        - assume that insertion order is sorted by (freq desc, word asc)
        """
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                node = self.TrieNode(char, word)
                curr.children[char] = node
                curr = curr.children[char]

    def count_keys(self, word):
        """
        return number of keys to enter for making word
        """
        curr = self.root
        answer = len(word)
        for (idx, char) in enumerate(word[:-1]):
            if char in curr.children:
                curr = curr.children[char]
                if curr.tab == word:
                    return min(idx+2, len(word))    # tab completion
            else:
                break   # new word

        return len(word)    # type whole word

    def print(self):
        """ print trie for debug """
        stack = [(self.root, 0)]
        while stack:
            curr, depth = stack.pop()
            print("{}{}:{}".format("-"*depth, curr.char, curr.tab))
            children = curr.children.values()
            stack.extend([(node, depth+1) for node in children])
        print("end print")


def solution(dict_words, sentence, m):
    # sort by freq DESC, word ASC
    dict_words.sort(key=lambda x: (-x[1], x[0]))

    # insert words to trie
    trie = Trie()
    for (word, freq) in dict_words:
        trie.insert(word)

    # trie.print()
    answer = sum([trie.count_keys(word) for word in sentence.split()])
    answer += m-1   # spaces
    sys.stdout.write(str(answer) + "\n")


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
        solution(words, sentence, M)