# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        res = []
        while queue:
            res.append(queue[-1].val)
            for i in range(len(queue)):
                out = queue.popleft()
                if out.left:
                    queue.append(out.left)
                if out.right:
                    queue.append(out.right)
        
        return res
                