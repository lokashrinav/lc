# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        total = [0]
        def dfs(node):
            if not node:
                return True
            
            val1 = dfs(node.left)
            val2 = dfs(node.right)

            curr = True

            if node.left:   
                curr = curr and node.val == node.left.val
            
            if node.right:
                curr = curr and node.val == node.right.val

            if val1 and val2 and curr:
                total[0] += 1

            return (val1 and val2 and curr)

        dfs(root)

        return total[0]
        