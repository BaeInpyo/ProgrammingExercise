def postorderGen(preorder, inorder):
    if len(preorder) <= 1:
        return preorder
    root = preorder[0]
    rootIndex = inorder.index(root)
    return (postorderGen(preorder[1:rootIndex+1], inorder[:rootIndex]) +
            postorderGen(preorder[rootIndex+1:], inorder[rootIndex+1:]) +
            [root])

def solution():
    ret = ''
    n = int(input())
    preorder = input().split()
    inorder = input().split()
    for s in postorderGen(preorder, inorder):
        ret = ret + ' ' + s
    print(ret[1:])

if __name__ == '__main__':
    for i in range(int(input())):
        solution()
