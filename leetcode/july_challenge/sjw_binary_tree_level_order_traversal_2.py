"""
Problem URL: https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3378/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Since there is no special traversal from left right, bottom to top,
1. Do post order traversal and save it's level. In the given example, we can
save as [[9,1], [15,2], [7,2], [20,1], [3,0]].
2. Do stable sort to remain left-to-right attribute.
--> There is no need to sort. Just insert in to result list.
"""

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.MAX_LEVEL = 0
        if not root:
            return []

        arr = []    # list of [value, level]
        self.postOrderTraversal(root, 0, arr)
        answer = [[] for _ in range(self.MAX_LEVEL+1)]

        # collect by level
        for [value, level] in arr:
            answer[level].append(value)

        return reversed(answer)

    def postOrderTraversal(self, root: TreeNode, level: int, arr: List = []) -> List[List[int]]:
        """Return result of post order traversal"""
        if not root:
            return

        self.MAX_LEVEL = max(self.MAX_LEVEL, level)
        if root.left:
            self.postOrderTraversal(root.left, level+1, arr)
        if root.right:
            self.postOrderTraversal(root.right, level+1, arr)
        arr.append([root.val, level])

        return 
