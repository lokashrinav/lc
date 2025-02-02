# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def how():
            queue = deque()
            queue.append(root)
            count = 1
            while queue:
                for i in range(len(queue)):
                    out = queue.popleft()
                    if not out.left and not out.right:
                        return count
                    if out.left:
                        queue.append(out.left)
                    if out.right:
                        queue.append(out.right)
                count += 1
            return count

        return how()


        