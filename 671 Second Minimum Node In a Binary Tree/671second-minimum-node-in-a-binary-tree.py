# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root.right and not root.left:
            return -1

        minNum = float('inf')

        def dfs(node, val):
            nonlocal minNum
            
            if not node:
                return 

            if val != node.val:
                minNum = min(minNum, node.val)
            
            dfs(node.left, val)
            dfs(node.right, val)        

        dfs(root, root.val)

        return minNum if minNum != float('inf') else -1
        
        
        