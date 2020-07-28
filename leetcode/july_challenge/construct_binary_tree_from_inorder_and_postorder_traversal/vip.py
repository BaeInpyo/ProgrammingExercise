# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTreeInternal(self, inorder, postorder, s_i, e_i, s_p, e_p):
        if s_i >= e_i:
            return None
        root = TreeNode(postorder[e_p - 1])
        root_idx = inorder.index(root.val, s_i, e_i)
        root.left = self.buildTreeInternal(inorder, postorder, s_i, root_idx, s_p, s_p + (root_idx - s_i))
        root.right = self.buildTreeInternal(inorder, postorder, root_idx+1, e_i, s_p + (root_idx - s_i), e_p - 1)
        return root
        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.buildTreeInternal(inorder, postorder, 0, len(inorder), 0, len(postorder))
