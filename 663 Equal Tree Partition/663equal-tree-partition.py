# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        
        def totalSum(node):
            if not node:
                return 0
            
            return node.val + totalSum(node.left) + totalSum(node.right)

        total = totalSum(root)
        saved = False

        def dfs(node):
            nonlocal saved
            if not node:
                return None
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)

            if rightSum is not None and rightSum == (total - rightSum):
                saved = True
            elif leftSum is not None and leftSum == (total - leftSum):
                saved = True
            
            if rightSum is None:
                rightSum = 0
            if leftSum is None :
                leftSum = 0
                
            return node.val + leftSum + rightSum
        
        dfs(root)

        return saved