# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                    curr = curr.next
                else:
                    head = head.next
                    curr = head
            else:
                prev = curr
                curr = curr.next
       
        return head
