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
    def flattenInternal(self, head: 'Node', front: 'Node', back: 'Node') -> 'Node':
        # Append front node to the current head.
        if front is not None:
            front.next = head;
            head.prev = front;
        
        current = head;
        prev = None;
        while current is not None:
            if current.child:
                next = self.flattenInternal(current.child, current, current.next);
                current.child = None;
                prev = next.prev;
                current = next;
            else:
                prev = current;
                current = current.next;
        
        current = prev;
        # Append back node to the last node.
        if back is not None:
            current.next = back;
            back.prev = current;
            current = back;
        
        return current;
    
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return None;
        self.flattenInternal(head, None, None);
        return head;
