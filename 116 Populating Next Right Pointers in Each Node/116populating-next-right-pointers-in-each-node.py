"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        curr = root
        prev = None
        while curr:
            next1 = curr
            prev = None
            while next1:

                if not next1.left:
                    break

                if prev:
                    prev.next = next1.left
                
                next1.left.next = next1.right

                prev = next1.right

                next1 = next1.next

            curr = curr.left
        
        return root
        