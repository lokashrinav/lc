# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        
        res = []
        def dfs(node, curr):
            if not node:
                return ""
            
            if not node.left and not node.right:
                curr += chr(node.val + 97)
                curr = curr[::-1]
                res.append(curr)
            else:
                dfs(node.left, curr + chr(node.val + 97))
                dfs(node.right, curr + chr(node.val + 97))

        dfs(root, "")

        print(res)

        return min(res)
        