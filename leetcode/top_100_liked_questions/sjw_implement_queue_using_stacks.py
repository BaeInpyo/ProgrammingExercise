"""
Problem URL: https://leetcode.com/problems/implement-queue-using-stacks/
"""

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, x):
        self._stack.append(x)

    def pop(self):
        return self._stack.pop()

    def peek(self):
        return self._stack[-1]

    def empty(self):
        return not bool(self._stack)

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        queue = Stack()
        queue.push(x)

        # reverse the order of stack
        reversed = Stack()
        while not self._stack.empty():
            reversed.push(self._stack.pop())

        # push reversed order of stack to another stack
        while not reversed.empty():
            queue.push(reversed.pop())

        self._stack = queue

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self._stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self._stack.peek()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self._stack.empty()


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
print(obj._queue._stack)
obj.push(2)
print(obj._queue._stack)
param_2 = obj.pop()
print(param_2, obj._queue._stack)
param_3 = obj.peek()
print(param_3, obj._queue._stack)
param_4 = obj.empty()
print(param_4, obj._queue._stack)