# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        hmap = {}
        for i in range(len(inorder)):
            hmap[inorder[i]] = i

        def dfs(i1, i2, j1, j2):
            print(i1, i2, j1, j2)
            if j2 < j1 or i2 < i1:
                return None
            if i1 == i2:
                return TreeNode(inorder[i1])

            curr = TreeNode(postorder[j2])
            loc = hmap[postorder[j2]]
            
            left_count = abs(i1 - (loc - 1))
            right_count = i2 - (loc + 1)
            curr.left = dfs(i1, loc - 1, j1, j1 + left_count)
            curr.right = dfs(loc + 1, i2, j2 - right_count - 1, j2 - 1)

            return curr

        return dfs(0, len(postorder) - 1, 0, len(postorder) - 1)