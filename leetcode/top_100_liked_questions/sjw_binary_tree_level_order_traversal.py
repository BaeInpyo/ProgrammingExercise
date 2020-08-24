"""
Problem URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0)])  # (node, level)
        answer = dict() # key: level, value: list of values
        while queue:
            node, level = queue.pop()

            # add node.val to answer
            if level in answer:
                answer[level].append(node.val)
            else:
                answer[level] = [node.val]

            # add children to queue
            if node.left:
                queue.appendleft((node.left, level+1))
            if node.right:
                queue.appendleft((node.right, level+1))

        return list(answer.values())