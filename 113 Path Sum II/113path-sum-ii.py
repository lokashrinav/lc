# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []

        def dfs(node, target, curr):
            if not node:
                return 
            
            if not node.left and not node.right:
                if target + node.val == targetSum:
                    curr.append(node.val)
                    res.append(curr.copy())
                    curr.pop()
                return
            
            curr.append(node.val)
            dfs(node.left, target + node.val, curr)
            dfs(node.right, target + node.val, curr)
            curr.pop()
        
        dfs(root, 0, [])

        return res
        