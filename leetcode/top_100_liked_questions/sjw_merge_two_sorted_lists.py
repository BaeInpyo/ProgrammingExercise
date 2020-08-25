"""
Problem URL: https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode() # dummy head
        answer = head
        while l1 and l2:
            val1, val2 = l1.val, l2.val
            if val1 < val2:
                answer.next = ListNode(val1)
                l1 = l1.next
            else:
                answer.next = ListNode(val2)
                l2 = l2.next

            answer = answer.next

        # extend l1
        if l1:
            while l1:
                answer.next = ListNode(l1.val)
                answer = answer.next
                l1 = l1.next

        # extend l2
        elif l2:
            while l2:
                answer.next = ListNode(l2.val)
                answer = answer.next
                l2 = l2.next

        return head.next