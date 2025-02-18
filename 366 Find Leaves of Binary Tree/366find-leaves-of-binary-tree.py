# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node):
            if not node:
                return 0
            
            maxNum = max(dfs(node.right), dfs(node.left))
            if maxNum == len(res):
                res.append([])

            res[maxNum].append(node.val)

            return maxNum + 1
        
        dfs(root)

        return res