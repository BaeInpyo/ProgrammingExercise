"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3385/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
To solve this problem, we can traverse whole tree nodes with level and index.
"""

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        store = dict()  # key: level, value: list of indexes
        self.traverse(root, 0, 0, store)    # root has level:0, index:0
        widths = [row[-1] - row[0] + 1 for row in store.values()]
        return max(widths)

    def traverse(self, node, level, index, store):
        """Traverse whole tree and add nodes into store"""
        if level in store:
            store[level].append(index)
        else:
            store[level] = [index]

        # traver children
        if node.left:
            self.traverse(node.left, level+1, 2*index+1, store)
        if node.right:
            self.traverse(node.right, level+1, 2*index+2, store)

        return