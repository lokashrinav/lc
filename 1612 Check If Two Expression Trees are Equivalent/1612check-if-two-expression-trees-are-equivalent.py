# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        
        hmap1 = defaultdict(int)
        hmap2 = defaultdict(int)

        def dfs(node, hmap):
            if not node:
                return
            
            if node.val.isalpha():
                hmap[node.val] += 1
                return
            
            dfs(node.left, hmap)
            dfs(node.right, hmap)
        
        dfs(root1, hmap1)
        dfs(root2, hmap2)

        return hmap1 == hmap2