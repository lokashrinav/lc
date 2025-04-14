# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        hmap = defaultdict(int)
        hmap[0] = 1

        count = 0

        def dfs(node, curr):
            nonlocal count

            if not node:
                return 0
            
            if (curr + node.val) - targetSum in hmap:
                count += hmap[(curr + node.val) - targetSum]
            
            hmap[curr + node.val] += 1

            dfs(node.right, curr + node.val)
            dfs(node.left, curr + node.val)

            hmap[curr + node.val] -= 1
        
        dfs(root, 0)

        return count
        