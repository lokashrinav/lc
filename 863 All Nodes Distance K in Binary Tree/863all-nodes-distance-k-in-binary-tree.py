# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        parents = {}

        def dfs(node, parent):
            if not node:
                return

            parents[node] = parent
            dfs(node.right, node)
            dfs(node.left, node)

        dfs(root, None)

        queue = deque()
        queue.append((target, 0))
        
        count = 0
        res = []
        visited = set()
        visited.add(target)
        while queue:
            if count == k:
                res = [queue.popleft()[0].val for i in range(len(queue))]
                break

            for i in range(len(queue)):
                node, count = queue.popleft()
                if node in parents and parents[node] and parents[node] not in visited:
                    queue.append((parents[node], count + 1))
                    visited.add(parents[node])

                if node.left and node.left not in visited:
                    queue.append((node.left, count + 1))
                    visited.add(node.left)
                
                if node.right and node.right not in visited:
                    queue.append((node.right, count + 1))
                    visited.add(node.right)
                
            count += 1
        
        return res




        

        
        