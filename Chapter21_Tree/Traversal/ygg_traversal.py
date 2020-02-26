import sys

def solution(preorder, inorder):
    if preorder == []:
        return []
    root = preorder[0]
    if len(preorder) == 1:
        return [root]
    in_root_idx = inorder.index(root)
    in_left, in_right = inorder[:in_root_idx], inorder[in_root_idx+1:]
    pre_left, pre_right = preorder[1:in_root_idx+1], preorder[in_root_idx+1:]
    
    return solution(pre_left, in_left) + solution(pre_right, in_right) + [root]
    
if __name__ == '__main__':
    #sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N = int(sys.stdin.readline().rstrip())
        preorder = sys.stdin.readline().rstrip().split()
        inorder = sys.stdin.readline().rstrip().split()
        print(' '.join(solution(preorder, inorder)))


