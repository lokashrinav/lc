# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        queue = deque([root])

        while queue:
            res.append(max(elem.val for elem in queue))
            for i in range(len(queue)):
                out = queue.popleft()
                if out.left:
                    queue.append(out.left)
                if out.right:
                    queue.append(out.right)
        
        return res