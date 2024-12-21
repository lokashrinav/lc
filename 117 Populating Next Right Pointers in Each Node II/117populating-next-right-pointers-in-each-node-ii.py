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
        queue = deque()
        queue.append(root)
        
        while queue:
            prev = None
            for i in range(len(queue)):
                out = queue.popleft()
                if not out:
                    continue
                queue.append(out.right)
                queue.append(out.left)
                if i == len(queue):
                    out.next = None
                else:
                    out.next = prev
                prev = out
        return root
        