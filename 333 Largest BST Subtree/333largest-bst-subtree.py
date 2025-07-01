# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        big = 1
        def dfs(node):
            nonlocal big

            if not node:
                return (True, 0, float('inf'), float('-inf'))
            
            boo1, height1, minNum1, maxNum1 = dfs(node.left)
            boo2, height2, minNum2, maxNum2 = dfs(node.right)

            if node.val > maxNum1 and node.val < minNum2 and boo1 and boo2:
                big = max(big, 1 + height1 + height2)
                return (True, 1 + height1 + height2, min([minNum1, minNum2, node.val]), max([maxNum1, maxNum2, node.val]))
            else:
                return (False, 0, float('inf'), float('-inf'))
            
        dfs(root)

        return big
            
        