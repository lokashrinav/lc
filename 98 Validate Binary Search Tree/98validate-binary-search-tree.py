# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        saved = True
        def dfs(node):
            nonlocal saved

            if not node:
                return (float('inf'), float('-inf'))
            
            leftMin, leftMax = dfs(node.left)
            rightMin, rightMax = dfs(node.right)

            if leftMax >= node.val or rightMin <= node.val:
                saved = False

            return (min([leftMin, node.val, rightMin]), max([leftMax, node.val, rightMax]))
        
        dfs(root)

        return saved
        