# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        saved = []
        to_delete = set(to_delete)

        def dfs(node, parent, right):
            if not node:
                return

            if node.val in to_delete:
                if parent is None:
                    dfs(node.left, None, 0)
                    dfs(node.right, None, 1) 
                else:
                    if right:
                        parent.right = None
                    else:
                        parent.left = None

                    dfs(node.left, None, 0)
                    dfs(node.right, None, 1)
            else:
                if parent is None:
                    saved.append(node)
                
                dfs(node.left, node, 0)
                dfs(node.right, node, 1)
        
        dfs(root, None, None)

        return saved
        