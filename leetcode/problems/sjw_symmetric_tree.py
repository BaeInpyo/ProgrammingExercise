"""
Problem URL: https://leetcode.com/problems/symmetric-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        nodes = dict()  # key: level, value: list of nodes
        queue = deque()
        queue.append((0, root)) # (level, node)
        while queue:
            level, node = queue.popleft()
            value = node.val if node else None
            if level in nodes:
                nodes[level].append(value)
            else:
                nodes[level] = [value]

            # we add empty node to queue
            if node:
                queue.append((level+1, node.left))
                queue.append((level+1, node.right))

        for lst in nodes.values():
            if not lst == lst[::-1]:
                return False

        return True