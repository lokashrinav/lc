# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        hmap = defaultdict(int)
        maxHeap = []
        def dfs(node):
            if not node:
                return 0
            
            val = node.val + dfs(node.left) + dfs(node.right)

            hmap[val] += 1

            maxHeap.append((-hmap[val], val))

            return val

        dfs(root)

        heapify(maxHeap)

        prev = None
        res = []
        print(maxHeap)
        while maxHeap:
            num, out = heappop(maxHeap)
            if prev is not None and num != prev:
                break
            res.append(out)
            prev = num

        return res

        