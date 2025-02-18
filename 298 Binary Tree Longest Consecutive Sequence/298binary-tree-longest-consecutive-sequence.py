# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        maxNum = [1]
        def dfs(node, prev, val):
            maxNum[0] = max(maxNum[0], val)
            if not node:
                return
            
            if node.val - 1 == prev.val:
                dfs(node.right, node, val + 1)
                dfs(node.left, node, val + 1)
            else:
                dfs(node.right, node, 1)
                dfs(node.left, node, 1)

        dfs(root, root, 0)

        return maxNum[0]
            