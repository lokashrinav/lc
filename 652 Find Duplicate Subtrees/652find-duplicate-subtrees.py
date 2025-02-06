# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        hmap = defaultdict(int)
        res = []

        def dfs(node):
            if not node:
                return '#'

            left = dfs(node.left)
            right = dfs(node.right)
            s = ','.join([left, right, str(node.val)])

            if hmap[s] == 1:
                res.append(node)
            
            hmap[s] += 1
            
            return s
        
        dfs(root)

        return res