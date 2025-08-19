# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def dfs(node, val):
            nonlocal count
            if not node:
                return
            if node.val == val:
                return node
            return dfs(node.left, val) or dfs(node.right, val)
        
        p_node = dfs(root, p)

        if p == q:
            return 0

        def dfs2(node, val):
            nonlocal count
            if not node:
                return None
            if node.val == val:
                return 0
            val1 = dfs2(node.left, val)
            val2 = dfs2(node.right, val)
            if val1:
                return 1 + val1
            elif val2:
                return 1 + val2
            else:
                return None
        
        count = dfs2(p_node, q)

        if count:
            return count
        
        parents = {}

        def dfs3(node, parent):
            if not node:
                return
            parents[node] = parent
            dfs3(node.left, node)
            dfs3(node.right, node)
        
        dfs3(root, None)

        visited = set()
        def dfs4(node):
            if not node:
                return None
            if node in visited:
                return None
            minNum = None            
            if node.val == q:
                return 0
            visited.add(node)
            
            calc1 = dfs4(parents[node])
            calc2 = dfs4(node.left)
            calc3 = dfs4(node.right)
            if calc1 is not None:
                minNum = 1 + calc1
            if calc2 is not None:
                minNum = 1 + calc2
            if calc3 is not None:
                minNum = 1 + calc3
            return minNum
        
        return dfs4(p_node)


