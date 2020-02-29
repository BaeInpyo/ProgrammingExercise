def travelse(pre_ord, in_ord, res):
    # print(pre_ord, in_ord)
    if not pre_ord: return
    root = pre_ord[0]
    idx = in_ord.index(root)
    travelse(pre_ord[1:1+idx], in_ord[:idx], res) # left subtree
    travelse(pre_ord[1+idx:], in_ord[idx+1:], res) # right subtree
    res.append(root)

for _ in range(int(input())):
    n = int(input())
    pre_ord, in_ord = list(map(int, input().split())), list(map(int, input().split()))
    ret = []
    travelse(pre_ord, in_ord, ret)
    print(*ret)
