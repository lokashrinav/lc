# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:

        parents = {}

        def dfs(node, prev):
            if not node:
                return

            parents[node.val] = prev

            dfs(node.left, node)
            dfs(node.right, node)
        
        def idk(node, k):
            if not node:
                return None
            
            if node.val == k:
                return node
            
            left = idk(node.left, k)
            if left:
                return left
            right = idk(node.right, k)
            if right:
                return right
            
        dfs(root, None)

        k_node = idk(root, k)

        queue = deque([k_node])
        visited = set()
        visited.add(k)

        while queue:
            out = queue.popleft()

            if not (out.left or out.right):
                return out.val
            
            if parents[out.val]:
                queue.append(parents[out.val])
                visited.add(parents[out.val].val)
            
            if out.left and out.left.val not in visited:
                queue.append(out.left)
                visited.add(out.left.val)

            if out.right and out.right.val not in visited:
                queue.append(out.right)
                visited.add(out.right.val)





        