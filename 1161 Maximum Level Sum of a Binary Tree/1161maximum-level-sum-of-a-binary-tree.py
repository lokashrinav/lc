# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])
        maxNum = float('-inf')
        count = 0

        while queue:
            sum1 = 0
            count += 1
            for i in range(len(queue)):
                out = queue.popleft()
                sum1 += out.val
                if out.left:
                    queue.append(out.left)
                if out.right:
                    queue.append(out.right)
            if sum1 > maxNum:
                maxNum = sum1
                saved = count
        
        return saved
        