"""
Problem URL: https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # # recursive solution
        # if not root:
        #     return []

        # result = []
        # result.extend(self.inorderTraversal(root.left))
        # result.append(root.val)
        # result.extend(self.inorderTraversal(root.right))

        # return result

        # iterative solution
        stack = [(False, root)] # (visited, node)
        result = []
        while stack:
            visited, node = stack.pop()

            # skip empty node
            if not node:
                continue

            # if already visited, add it's value
            if visited:
                result.append(node.val)

            # it not visited yet, push stack in `inorder`
            else:
                # NOTE: since this is stack, append in reversed order
                stack.append((False, node.right))
                stack.append((True, node))
                stack.append((False, node.left))

        return result