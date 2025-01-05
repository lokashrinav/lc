# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        heap = []

        hmap = {}

        def dfs(node):
            if not node:
                return
            hmap[node.val] = hmap.get(node.val, 0) + 1
            heapq.heappush(heap, (-hmap[node.val], node.val))
            dfs(node.right)
            dfs(node.left)
            return
        
        dfs(root)

        print(heap)

        res = []

        final = heapq.heappop(heap)
        new = final
        while heap and final[0] == new[0]:
            res.append(new[1])
            new = heapq.heappop(heap)
        else:
            if final[0] == new[0]:
                res.append(new[1])

        return res
                