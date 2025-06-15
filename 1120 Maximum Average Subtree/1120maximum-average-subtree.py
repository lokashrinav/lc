# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:

        maxAvg = float('-inf')

        def dfs(node):
            nonlocal maxAvg
            
            if not node:
                return (0, 0)
            
            val1, count1 = dfs(node.left)
            val2, count2 = dfs(node.right)

            maxAvg = max(maxAvg, (val1 + val2 + node.val) / (1 + count1 + count2))

            return (val1 + val2 + node.val, count1 + count2 + 1)

        val, count = dfs(root)
        
        return maxAvg