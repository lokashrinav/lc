# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:

        sum1 = 0

        if root.right:
            sum1 += root.right.val
        
        if root.left:
            sum1 += root.left.val
        
        return sum1 == root.val
        