"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])

        arr = [[]]
        while queue:
            for i in range(len(queue)):
                out = queue.popleft()
                arr[-1].append(out.val)
                for child in out.children:
                    queue.append(child)
            arr.append([])

        return arr[:-1]
        