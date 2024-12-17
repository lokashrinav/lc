# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def backtrack(node):
            if not node:
                return [0, 0]

            minList = backtrack(node.right)
            maxList = backtrack(node.left)

            minNode = node.val + minList[1] + maxList[1]
            maxNode = max(minList) + max(maxList)
            print(node.val, minNode, maxNode)
            return [minNode, maxNode]
        
        return max(backtrack(root))
        