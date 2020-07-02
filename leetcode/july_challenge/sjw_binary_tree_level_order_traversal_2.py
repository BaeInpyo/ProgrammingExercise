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
"""

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        arr = []
        self.postOrderTraversal(root, 0, arr)
        arr.sort(key=lambda x: x[1], reverse=True) # sort by level DESC

        answer = []
        values = []
        curr_level = arr[0][1]
        for (value, level) in arr:
            if level == curr_level:
                values.append(value)
            else:
                answer.append(values)
                values = [value]

        answer.append(values)
        return answer

    def postOrderTraversal(self, root: TreeNode, level: int, arr: List = []) -> List[List[int]]:
        """Return result of post order traversal"""
        if not root:
            return

        if root.left:
            self.postOrderTraversal(root.left, level+1, arr)
        if root.right:
            self.postOrderTraversal(root.right, level+1, arr)
        arr.append([root.val, level])

        return 
