# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([(0, root)])
        hmap = defaultdict(list)
        while queue:
            hmap2 = defaultdict(list)
            for i in range(len(queue)):
                count, node = queue.popleft()
                hmap2[count].append(node.val)
                if node.left:
                    queue.append((count - 1, node.left))
                if node.right:
                    queue.append((count + 1, node.right))

            for key in hmap2.keys():
                hmap2[key] = sorted(hmap2[key])
                hmap[key].extend(hmap2[key])
            
        
        return [hmap[key] for key in sorted(hmap.keys())]


