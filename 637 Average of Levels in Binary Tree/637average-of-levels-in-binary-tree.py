# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []

        queue = deque()

        queue.append(root)

        while queue:
            total = 0
            count = len(queue)
            for i in range(len(queue)):
                out = queue.popleft()
                if out.left:
                    queue.append(out.left)
                if out.right:
                    queue.append(out.right)
                total += out.val
            res.append(total / count)

        return res

        