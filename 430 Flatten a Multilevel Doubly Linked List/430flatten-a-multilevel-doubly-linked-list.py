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
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        dummy = Node(0)
        curr, stack = dummy, []
        stack.append(head)
        while stack:
            out = stack.pop()
            if out.next:
                stack.append(out.next)
            if out.child:
                stack.append(out.child)
            out.child = None
            curr.next = out
            out.prev = curr
            curr = curr.next

        dummy.next.prev = None

        return dummy.next
        