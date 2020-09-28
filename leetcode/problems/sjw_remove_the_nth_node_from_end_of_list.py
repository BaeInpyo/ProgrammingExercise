"""
Problem URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """ Second version with dummy """
        dummy = ListNode()
        dummy.next = head
        arr = []

        curr = dummy
        while curr:
            arr.append(curr)
            curr = curr.next

        L = len(arr)
        arr[L-n-1].next = arr[L-n].next
        return arr[0].next

        """ First version wihtout dummy """
        # # Collect all nodes
        # arr = []

        # curr = head
        # while curr:
        #     arr.append(curr)
        #     curr = curr.next

        # # edge case: return empty list
        # if len(arr) == 1:
        #     return None

        # # edge case: remove last one
        # if n == 1:
        #     arr[-2].next = None
        #     return head

        # # edge case: remove first one
        # if n == len(arr):
        #     return arr[1]

        # # normal case
        # arr[-n-1].next = arr[-n+1]
        # return arr[0]