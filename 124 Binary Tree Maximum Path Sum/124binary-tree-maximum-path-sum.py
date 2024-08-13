# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = [root.val]
        def dfs(node):
            if not node:
                return 0
            dfs_right = dfs(node.right)
            dfs_left = dfs(node.left)
            sum1 = max(max(max(node.val + dfs_right + dfs_left, node.val + dfs_right), node.val + dfs_left), node.val)
            maxSum[0] = max(maxSum[0], sum1)
            sum1 = max(max(node.val + dfs_right, node.val + dfs_left), node.val)
            return sum1
            
        dfs(root)
        return maxSum[0]


        