# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        longest = 0

        def dfs(node, curr, left):
            if not node:
                return curr
            
            first = second = None
            if left:
                first = dfs(node.right, 0, False)
            else:
                first = dfs(node.right, curr + 1, True)

            if left:
                second = dfs(node.left, curr + 1, False)
            else:
                second = dfs(node.left, 0, True)
            
            return max(first, second)
        
        return max(dfs(root, 0, True), dfs(root, 0, False)) - 1
        
        