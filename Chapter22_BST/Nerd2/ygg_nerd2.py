import sys


class BST():
    root = None
    length = 0
    def __init__(self, person):
        self.p, self.q = person
        self.parent, self.left, self.right = None, None, None
        
    def is_leaf(self):
        return (not self.left) and (not self.right)
    

    def delete_self(self):
        right_child, left_child, parent = self.right, self.left, self.parent
        if parent.left == self:
            parent.left = None
        elif parent.right == self:
            parent.right = None

        if left_child:
            if right_child:
                left_child_right_child = left_child.right
                left_child.right = right_child
                right_child.insert(left_child_right_child)
                BST.length -= 1
            parent.insert(left_child)
            BST.length -= 1

        elif right_child:
            parent.insert(right_child)
            BST.length -= 1
        
        BST.length -= 1

    def insert(self, node):
        if not node:
            return
        curr = BST.root
        while curr:
            if curr.p > node.p and curr.q > node.q:
                return

            elif curr.p < node.p and curr.q < node.q:
                parent = curr.parent
                curr.delete_self()
                curr = parent
                continue

            else:
                if curr.p < node.p:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = node
                        node.parent = curr
                        BST.length += 1
                        return

                else:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = node
                        node.parent = curr
                        BST.length += 1
                        return


def solution(N, people):
    result = 0
    for person in people:
        BST.root.insert(BST(person))    
        result += BST.length
    return result
    
if __name__ == '__main__':
    sys.stdin = open('input.in', 'r')
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N = int(sys.stdin.readline().rstrip())
        people = [[int(x) for x in sys.stdin.readline().rstrip().split()] for _ in range(N)]
        BST.root = BST([100001, -1])
        BST.length = 0
        print(solution(N, people))


