"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3386/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # """flatten linked list which starts from head and then return head"""
        # if not head:
        #     return

        # dummy_head = Node(None, None, head, None)
        # curr = dummy_head

        # # loop over linked list horizontally
        # while curr:
        #     # if curr node has child, flatten it and connect it
        #     if curr.child:
        #         flattened_head = self.flatten(curr.child)
        #         flattened_tail = flattened_head
        #         while flattened_tail.next:
        #             flattened_tail = flattened_tail.next

        #         flattened_head.prev = curr
        #         flattened_tail.next = curr.next
        #         if curr.next:
        #             curr.next.prev = flattened_tail
        #         curr.next = flattened_head
        #         curr.child = None

        #     curr = curr.next

        # return dummy_head.next

        """
        Since every recursion can be implemented with stack, we will use stack
        """
        if not head:
            return None

        stack, order = [head], []
        while stack:
            curr = stack.pop()
            order.append(curr)

            # child has precedence to next
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)

        # we traversed whole linked list and re-arrange based on order
        # set next
        for idx in range(len(order)-1):
            order[idx].next = order[idx+1]
        # set prev
        for idx in range(1, len(order)):
            order[idx].prev = order[idx-1]
        # set child
        for idx in range(len(order)):
            order[idx].child = None

        return order[0]