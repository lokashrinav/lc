# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return None

            if target.val == node.val:
                return node
            
            calc1 = dfs(node.left) 
            calc2 = dfs(node.right)

            return calc1 if calc1 else calc2
        
        return dfs(cloned)
        