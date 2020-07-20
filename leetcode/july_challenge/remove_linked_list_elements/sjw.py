"""
Problem URL: https://leetcode.com/explore/featured/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3396/

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode()
        dummy_head.next = head
        prev = dummy_head
        
        while prev.next:
            curr = prev.next
            if curr and curr.val == val:
                # remove curr
                prev.next = curr.next
            elif curr and curr.val != val:
                # jump to next node
                prev = curr
            elif not curr:
                # prev is last node of linked list
                break
                
        return dummy_head.next
                
                
