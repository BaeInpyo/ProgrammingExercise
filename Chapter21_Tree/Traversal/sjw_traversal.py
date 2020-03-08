import sys
import os

abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


"""
preorder = root -> left -> right
inorder = left -> root -> right
postorer = left -> right -> root
"""

def solution(n, preorder, inorder):
    def print_postorder(preorder, inorder):
        if not inorder:
            return

        # preorder[0] is root of tree because it searches root first
        root = preorder[0]

        # inorder traversal searches in left -> root -> right order
        # so we can find left and right subtree
        try:
            index = inorder.index(root)
        except ValueError:
            return

        left = inorder[:index]
        right = inorder[index+1:]

        preorder.pop(0)
        print_postorder(preorder, left)
        print_postorder(preorder, right)
        print(root, end=" ")

    print_postorder(preorder, inorder)
    print()


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(int(input()))
        preorder = [int(x) for x in input().strip().split()]
        inorder = [int(x) for x in input().strip().split()]

        solution(N, preorder, inorder)