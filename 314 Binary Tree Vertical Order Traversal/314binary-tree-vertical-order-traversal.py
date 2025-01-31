# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0)])
        hmap = defaultdict(list)
        while queue:
            src, num = queue.popleft()
            hmap[num].append(src.val)
            if src.left:
                queue.append((src.left, -1 + num))
            if src.right:
                queue.append((src.right, 1 + num))
        
        return [hmap[key] for key in sorted(hmap.keys())]