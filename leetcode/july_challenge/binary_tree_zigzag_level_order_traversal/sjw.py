"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3398/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        tree = dict()
        queue = deque([(root, 0)])    # (node, level)
        max_level = 0
        while queue:
            node, level = queue.popleft()
            max_level = max(max_level, level)
            if level in tree:
                tree[level].append(node.val)
            else:
                tree[level] = [node.val]

            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))

        answer = []
        for level in range(max_level+1):
            # left to right order
            if level%2 == 0:
                answer.append(tree[level])
            # right to left order
            else:
                answer.append(tree[level][::-1])

        return answer