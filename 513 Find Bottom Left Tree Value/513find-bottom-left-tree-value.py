# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([root])
        last = None
        while queue:
            last = queue[0].val
            for i in range(len(queue)):
                out = queue.popleft()
                if out.left:
                    queue.append(out.left)
                if out.right:
                    queue.append(out.right)
        
        return last
                    