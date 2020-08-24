"""
Problem URL: https://leetcode.com/problems/min-stack/
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []

    def push(self, x: int) -> None:
        # stack is empty
        if not self.lst:
            self.lst.append((x, x)) # (value, minNumber)
        else:
            self.lst.append((x, min(x, self.lst[-1][1])))

    def pop(self) -> None:
        self.lst.pop()

    def top(self) -> int:
        return self.lst[-1][0]

    def getMin(self) -> int:
        return self.lst[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()