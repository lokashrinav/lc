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
    def connect(self, root: 'Node') -> 'Node':

        curr = root
        while curr:
            next1 = curr
            prev = None
            first = None
            while next1:    
                print(curr.val, next1.val)
                if next1.left and next1.right:
                    if not first:
                        first = next1.left
                    if prev:
                        prev.next = next1.left
                    next1.left.next = next1.right
                    prev = next1.right
                elif next1.left:
                    if not first:
                        first = next1.left
                    if prev:
                        prev.next = next1.left
                    prev = next1.left
                elif next1.right:
                    if not first:
                        first = next1.right
                    if prev:
                        prev.next = next1.right
                    prev = next1.right
                next1 = next1.next
                
            curr = first

        return root
        