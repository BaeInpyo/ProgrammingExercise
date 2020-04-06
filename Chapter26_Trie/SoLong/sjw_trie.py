from collections import deque

class Trie:
    class TrieNode:
        def __init__(self, char):
            self.char = char
            self.end = False
            self.children = {}

    def __init__(self):
        self.root = Trie.TrieNode("*")

    def print(self):
        """ print trie from root with dfs """
        def _print(node, depth):
            if not node:
                return

            print("-" * depth + node.char, node.end)
            for child in node.children:
                child_node = node.children[child]
                _print(child_node, depth+1)

        _print(self.root, 0)

    def insert(self, string):
        """ add string to trie """
        curr_node = self.root
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                curr_node.children[char] = Trie.TrieNode(char)
                curr_node = curr_node.children[char]

        curr_node.end = True
        return

    def search(self, string):
        """ return if string exists inside trie """
        curr_node = self.root
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        # there can be a case that curr node is not terminal node
        # which means that string does not exist inside trie
        return curr_node.end

    def starts_with(self, prefix):
        """ return list of strings that start with prefix using bfs """

        # same as search
        curr_node = self.root
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return []

        # curr_node is found
        result = []
        if curr_node.end is True:
            result.append("")
        queue = deque()
        for k, v in curr_node.children.items():
            queue.append((v, ""))
        while queue:
            curr_node, acc = queue.pop()
            if curr_node.end:
                result.append(acc + curr_node.char)

            for k, v in curr_node.children.items():
                queue.append((v, acc + curr_node.char))

        return [prefix + item for item in result]



trie = Trie()
trie.insert("radio")
trie.insert("rasong")
trie.insert("audio")
trie.insert("rasongsonggyerantag")
trie.print()
print("word radio:", trie.search("radio"))
print("word ras:", trie.search("ras"))
print("starts with ra:", trie.starts_with("ra"))
print("starts with rasong:", trie.starts_with("rasong"))