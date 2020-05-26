# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

def print_list(node):
    ret = []
    while node:
        ret.append(node.val)
        node = node.next
        
    print(ret)

class Solution:
    """
    In every step, pop number A from heap and restore it from list that originally contains number A
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()    # dummy node
        curr = head
        
        # initialize heap
        # pop first number from all LinkedList
        heap = []
        for (idx, node) in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx))
                lists[idx] = node.next
                  
        # while numbers are remaining
        while heap:
            val, idx = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[idx]:
                # pop node from idxth LinkedList
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
                
        return head.next